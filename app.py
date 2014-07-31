from server import StockzServer

server = StockzServer()

@server.error_action
def error(ex):
	print(' - ' + repr(ex))
	return 'An error occurred'

@server.action('hello')
def hello(sender, data):
	return 'Hello, ' + sender

if __name__ == '__main__':
	server.run()
