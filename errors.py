class StockzError(Exception):
	""" A base exception class that should not be raised """

	def __init__(self, *args):
		super(StockzError, self).__init__(*args)

class ActionError(StockzError):
	""" An Exception related to an action """

	def __init__(self, action, *args):
		if isinstance(action, basestring):
			if len(args) == 0:
				args = (action, )
			else:
				arg = args

				if len(args) == 1:
					arg = args[0]

				args = (('{0}: {1}').format(action, arg), )

		super(ActionError, self).__init__(*args)
		self._action = action

	@property
	def action(self):
		""" The action that this Exception is related to """

		if not hasattr(self, '_action'):
			return ''

		attr = getattr(self, '_action')

		if not isinstance(attr, basestring):
			return ''

		return attr

class InvalidActionError(ActionError):
	""" An Exception related to a missing or invalid action """

	def __init__(self, action = None, *args):
		super(InvalidActionError, self).__init__(action, *args)


class CreditsError(StockzError):
	""" An Exception describing not enough credits """

class StockError(StockzError):
	""" An Exception describing not enough stock """

class InvalidStockError(StockError):
	"""" An exception describing a missing or invalid stock"""
