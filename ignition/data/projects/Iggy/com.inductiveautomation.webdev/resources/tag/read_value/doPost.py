def doPost(request, session):
	tagPath = request['data']['tagPath']
	return exchange.iggy.web_dev.tag.read_values(tagPath)