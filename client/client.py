import socket

class StockzClient():
	"""A client for StockzServer"""

	def __init__(self, host = '0.0.0.0', port = 1337):
		"""Create a StockzClient to connect to the provided address"""

		if not isinstance(host, basestring):
			raise TypeError('host must be a string')

		if not isinstance(port, int):
			raise TypeError('port must be an int')

		self._address = (host, port)

	def execute(self, request, timeout = 1):
		"""Execute a request and get a response from the server"""

		if not isinstance(request, basestring):
			raise TypeError('request must be a string')

		if not isinstance(timeout, int):
			raise TypeError('timeout must be an int')

		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			sock.connect(self._address)
			sock.settimeout(timeout)

			sock.sendall(request)

			response = sock.recv(2048)
		finally:
			sock.close()

		if len(response) == 0:
			return None

		return response
