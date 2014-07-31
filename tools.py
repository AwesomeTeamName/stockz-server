import inspect

def arity(method, ignore = ['self'], include_optional = False):
	if not callable(method):
		raise TypeError('method must be a callable')

	if ignore is None:
		ignore = []

	if isinstance(ignore, basestring):
		ignore = [ ignore ]

	if not isinstance(ignore, list):
		raise TypeError('ignore must be a list')

	args, varargs, varkw, defaults = inspect.getargspec(method)

	argc = len(args)

	if defaults is not None:
		optc = len(defaults)
	else:
		optc = 0

	if optc > 0 and not include_optional:
		for _ in range(optc):
			args.pop()

	count = 0

	for arg in args:
		if not arg in ignore:
			count += 1

	return count
