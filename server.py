import tools, socket, thread
from errors import InvalidActionError

class StockzServer():
	"""A TCP server for routing actions to methods"""

	def __init__(self):
		"""Create a StockzServer instance"""
		self._actions = {}
		self._error_action = None

	def action(self, action):
		"""A decorator that is used to register an action."""
		
		if not isinstance(action, basestring):
			raise TypeError('action must be a string')

		# Create a dummy decorator to save the action
		def decorator(func):
			if not callable(func):
				raise TypeError('func must be a callable')

			# Retrieve the action's name and argument count
			name = func.__name__
			argc = tools.arity(func, include_optional = True)

			if argc != 2:
				raise InvalidActionError(name, 'action must accept 2 arguments')

			# Save the action
			self._actions[name] = func
			
			return func
		return decorator

	def error_action(self, func):
		"""A decorator that is used to define the error action."""

		if callable(self._error_action):
			raise InvalidActionError(None, 'error action already defined')

		if not callable(func):
			raise TypeError('func must be a callable')

		name = func.__name__
		argc = tools.arity(func, include_optional = True)

		if argc != 1:
			raise InvalidActionError(name, 'action must accept 1 argument')

		self._error_action = func

		return func

	def has_action(self, action):
		if not isinstance(action, basestring):
			raise TypeError('action must be a string')

		return action in self._actions

	def call_action(self, action, sender, data):
		"""Call an action with the provided values and return it's response."""

		if not isinstance(action, basestring):
			raise TypeError('action must be a string')

		if not isinstance(sender, basestring):
			raise TypeError('sender must be a string')

		if data is not None and not isinstance(data, basestring):
			raise TypeError('data must be a string or None')

		# Ensure the action exists
		if not self.has_action(action):
			raise InvalidActionError(action)

		# Run the action
		result = self._actions[action](sender, data)

		# Enforce action return type
		if result is not None and not isinstance(result, basestring):
			raise ActionError(action, 'action must return a string or None')

		return result

	def call_error_action(self, exception):
		"""Call the error action with the provided Exception and return it's response."""

		if not isinstance(exception, Exception):
			raise TypeError('exception must be an Exception')

		# Ensure the action exists
		if not callable(self._error_action):
			raise InvalidActionError(None, 'missing error action')

		# Run the action
		result = self._error_action(exception)

		# Enforce action return type
		if result is not None and not isinstance(result, basestring):
			raise ActionError(None, 'action must return a string or None')

		return result

	def handle(self, sock, addr):
		"""Handle client connections and parsing."""

		try:
			# Read up to 2048 bytes from the client
			raw = sock.recv(2048)

			if len(raw) == 0:
				raise InvalidActionError(None, 'no data received')

			# Split the data using space as a delimeter
			split = raw.split()

			if len(split) < 2:
				raise InvalidActionError(None, 'missing sender or action')

			# action and sender are always the first two elements
			action = split[0]
			sender = split[1]

			# If there is any other data, join it together
			if len(split) > 2:
				data = (' ').join(split[2:])
			else:
				data = None

			# Call the appropriate action and generate a response
			response = self.call_action(action, sender, data)

			# If there is a response, send it to the client
			if response is not None:
				sock.sendall(response)

		except Exception as ex:
			response = self.call_error_action(ex)

			# If there is a response, send it to the client
			if response is not None:
				sock.sendall(response)
		finally:
			sock.close()

	def run(self, host = '0.0.0.0', port = 1337):
		if not isinstance(host, basestring):
			raise TypeError('host must be a string')

		if not isinstance(port, int):
			raise TypeError('port must be an int')
		
		# Create and configure socket
		self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self._socket.bind((host, port))
		self._socket.listen(5)

		print((' * Listening on {0}:{1}').format(host, port))

		# Listen for connections and dispatch them to the handle method (in a new thread)
		while True:
			sock, addr = self._socket.accept()
			thread.start_new_thread(self.handle, (sock, addr))
