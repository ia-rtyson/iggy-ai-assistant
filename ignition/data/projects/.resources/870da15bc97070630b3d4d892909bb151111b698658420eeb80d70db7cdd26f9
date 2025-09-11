def stream(session_id, pageId, chat_id, chat, username):
	import json
	from java.net import URL, HttpURLConnection
	from java.io import BufferedReader, InputStreamReader, OutputStreamWriter
	
	log = system.util.getLogger('streaming-n8n-chat')
	
	payload = {
		"chat": chat, #self.view.custom.chat,
		"session_id": session_id,
		"chat_id": chat_id
	}
	log.info("Streaming chat: %s" %payload)
	payload_json = json.dumps(payload)
	

	url = URL("http://n8n:5678/webhook/chat-stream")
	conn = url.openConnection()
	conn.setRequestMethod("POST")
	conn.setDoOutput(True)
	conn.setUseCaches(False)
	conn.setRequestProperty("Content-Type", "application/json")
	conn.setRequestProperty("Accept", "application/json")
	
	out = conn.getOutputStream()
	writer = OutputStreamWriter(out, "UTF-8")
	writer.write(payload_json)
	writer.flush()
	writer.close()
	
	assistant = ""
	
	try:
		reader = BufferedReader(InputStreamReader(conn.getInputStream(), "UTF-8"))
	
		while True:
			
			line = reader.readLine()
			log.info(line)
			if line is None:
				break
			line = line.strip()
			if not line:
				continue
	
			try:
				obj = json.loads(line)
			except ValueError:
				continue
			log.info(str(obj))
			content = obj.get("content", "")
			
			assistant += content
			log.info('streaming content: %s' %content)
			if session_id and pageId:
				system.perspective.sendMessage(messageType='chat-stream', payload={'token': content, 'full': assistant, 'chatId': chat_id}, scope='page', sessionId=session_id, pageId=pageId)
	
	except Exception as e:
		log.error('error: %s' %e)
		return {'success': False, 'Error': str(e)}
	
	finally:
		try:
			reader.close()
		except Exception:
			pass
		conn.disconnect()
	
	return {'success': True}
	
	