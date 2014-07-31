from client import StockzClient

def build_request(action, sender, data = None):
	"""Build a request from an action, sender and data"""

	# Create request array with required fields
	request = [action, sender]

	# Add data if provided
	if data is not None:
		request.append(data)

	return (' ').join(request)

client = StockzClient()

request = build_request("hello", "Jack")

print(('Request: {0}').format(request))

response = client.execute(request)

print(('Response: {0}').format(response))