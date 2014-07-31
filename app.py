from server import StockzServer

server = StockzServer()

@server.error_action
def error(ex):
	name = ex.__class__.__name__
	message = ex.message
	formatted = ('{0}: {1}').format(name, message)
	print(' - ' + formatted)

	return formatted

@server.action('hello')
def hello(sender, data):
	return 'Hello, ' + sender

if __name__ == '__main__':
	server.run()
