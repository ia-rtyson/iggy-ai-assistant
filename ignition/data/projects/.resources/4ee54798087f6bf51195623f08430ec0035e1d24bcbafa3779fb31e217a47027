def n8n_post(url,postData):
    """
    Sends a POST request with JSON data to the n8n webhook,
    """
    logger = system.util.getLogger("n8n_integration")
    contentType = "application/json"
    
    jsonData = system.util.jsonEncode(postData)
    res = system.net.httpPost(url, contentType,jsonData)
#    logger.info(res)
    return None
