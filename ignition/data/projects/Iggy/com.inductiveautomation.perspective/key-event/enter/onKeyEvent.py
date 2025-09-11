def onKeyEvent(page, event):
	logger = system.util.getLogger('testing')
#	logger.info(str(dir(page.name)))
#	logger.info(str(page.id))
	
#	page.name
	system.perspective.sendMessage(
		messageType='enter',
		payload={},
		scope='page',
		pageId=page.id
	)