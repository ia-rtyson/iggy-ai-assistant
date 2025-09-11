def doPost(request, session):
	sessionId = request["data"].get('sessionId', None)
	pageId = request["data"].get('pageId', None)
	text = request["data"].get('text', None)
	
	system.util.getLogger('speech-process').info('%s: %s: %s' %(sessionId, pageId, text))
	if sessionId and pageId and text:
		system.perspective.sendMessage('enter', {'text': text}, 'page', sessionId, pageId)
	return {"json": {"status": "OK"}}