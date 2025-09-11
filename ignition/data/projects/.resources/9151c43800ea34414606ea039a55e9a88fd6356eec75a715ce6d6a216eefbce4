def doPost(request, session):
#	system.util.getLogger('webdev: chat_recieve').info(str(request['data']))

	system.perspective.sendMessage(
		messageType =  'refresh',
		payload = request['data'],
		scope='session',
		sessionID = request['data']['session_id']
		)
	return {'html': 'Post Success!'}