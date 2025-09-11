def doPost(request, session):
	system.util.getLogger('web dev: tag.write_value').info(str(request['data']['tagPath']))
	tagPath = request['data']['tagPath']
	value = request['data']['value']
	return exchange.iggy.web_dev.tag.write_value(tagPath, value)