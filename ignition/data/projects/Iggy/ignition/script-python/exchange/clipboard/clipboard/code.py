def copyTo(text, gatewayAddress=None):
	"""Copy to clipboard function, formats an endpoint url to be passed into an iframe for perspective
	
	Args:
		text: text to be copied to the clipboard
		gatewayAddress: address of the gateway where the endpoint is located, optional property if left as None
			will use the system.util.getGatewayAddress() function (default: None)
	Returns:
		endpoint url for the the copy to clipboard perspective functionality
	"""
	endpoint = '{gatewayAddress}/system/webdev/{projectName}/exchange/copy-to-clipboard/resource?toCopy={text}'
	if gatewayAddress is None:
		gatewayAddress = system.util.getGatewayAddress()
	props = {'gatewayAddress': gatewayAddress, 'projectName': system.util.getProjectName(), 'text': text}
	return endpoint.format(**props)

def copyToHubspot(text, gatewayAddress=None):
	"""Copy to clipboard function, formats an endpoint url to be passed into an iframe for perspective
	
	Args:
		text: text to be copied to the clipboard
		gatewayAddress: address of the gateway where the endpoint is located, optional property if left as None
			will use the system.util.getGatewayAddress() function (default: None)
	Returns:
		endpoint url for the the copy to clipboard perspective functionality
	"""
	endpoint = '{gatewayAddress}/system/webdev/{projectName}/exchange/copy-to-clipboard/resource_hubspot?toCopy={text}'
	if gatewayAddress is None:
		gatewayAddress = system.util.getGatewayAddress()
	props = {'gatewayAddress': gatewayAddress, 'projectName': system.util.getProjectName(), 'text': text}
	return endpoint.format(**props)