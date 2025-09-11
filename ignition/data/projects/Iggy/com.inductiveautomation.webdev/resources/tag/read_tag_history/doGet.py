def doGet(request, session):
	system.util.getLogger('web dev: tag/read_values').info(request['postData'])
	return {'html': '<html><body>Hello World</body></html>'}