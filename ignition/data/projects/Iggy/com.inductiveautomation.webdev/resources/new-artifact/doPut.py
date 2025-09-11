def doPut(request, session):
#	dataJson = request["data"]["dataJson"] if "dataJson" in request["data"] else None
#	uuid = request["data"]["uuid"] if "uuid" in request["data"] else None
#	sessionId = request["data"]["sessionId"] if "sessionId" in request["data"] else None
#	artifactType = request["data"]["artifactType"] if "artifactType" in request["data"] else None
	import random, string, os, json, errno
	import java.time.temporal.ChronoUnit as ChronoUnit
	log = system.util.getLogger('new artifact')
	ignition_chat_history_id = request["data"]["ignition_chat_history_id"] if "ignition_chat_history_id" in request["data"] else None
	artifact_type_id = request["data"]["artifact_type_id"] if "artifact_type_id" in request["data"] else None
	data = request["data"]["data"] if "data" in request["data"] else None
	description = request["data"]["description"] if "description" in request["data"] else None
	
	if not ignition_chat_history_id or not artifact_type_id or not data or not description:
		request['servletResponse'].setStatus(400)
		request['servletResponse'].getWriter().print("HTTP 400: Missing data JSON, artifact ID, chat history ID, or description.")
		return
	
#	artifact_type_ids = {
#		"form": 1,
#		"script": 2,
#		"view": 3
#	}
	log.info('creating new artifact with id: %s' %artifact_type_id)
	if str(artifact_type_id) == '3':
		log.info('creating new view: %s' %description)
		stagingPath = "Exchange/Staging/Views"
		viewName = ''.join(random.choice(string.ascii_uppercase)+random.choice(string.digits) for _ in range(5))
		basePath = "data/projects/Iggy/com.inductiveautomation.perspective/views/%s" %stagingPath
		destPath = os.path.join(basePath, viewName)
		
		try:
			os.makedirs(destPath)
		except OSError as exc:
			# If the directory exists we ignore the error; otherwise re‑raise
			if exc.errno != errno.EEXIST:
				raise
		
		
		viewFile     = os.path.join(destPath, 'view.json')
		resourceFile = os.path.join(destPath, 'resource.json')
		log.info('writing new view file to staging')
		with open(viewFile, 'w') as f:
			f.write(data)
		
		resourceJson = {
		  "scope": "G",
		  "version": 1,
		  "restricted": False,
		  "overridable": True,
		  "files": [
		    "view.json"
		  ],
		  "attributes": {
		    "lastModification": {
		      "actor": "external",
		      "timestamp": str(system.date.now().toInstant().truncatedTo(ChronoUnit.SECONDS))
		    }
		  }
		}
		log.info('adding resource file')
		with open(resourceFile, 'w') as f:
			json.dump(resourceJson, f, indent=2)
		
		log.info('files written, requesting project scan')
		data = "%s/%s" %(stagingPath, viewName)
		system.project.requestScan()
		log.info('created new view: %s' %data)
	
	parameters = {
#		"uuid": uuid,
		"ignition_chat_history_id": ignition_chat_history_id,
		"ignition_chat_history_chat_id": ignition_chat_history_id,
		"artifact_type_id": artifact_type_id,
		"data": data,
		"description": description
	}
	
	
#	system.db.execUpdate("ICC2025/AI/Artifacts/Insert", parameters)
	system.db.execQuery("Exchange/Iggy/Artifact/insert_artifact", parameters)
	system.util.getLogger('new-artifact').info(system.util.jsonEncode(data, 2))
	parameters = {
		"session_id": ignition_chat_history_id,
		"message": system.util.jsonEncode({"type": "ai", "additional_kwargs": {}, "response_metadata": {}, "content": "## Artifact <type: %s>\n%s" %(artifact_type_id, str(data))}),
		"hide": True
	}
	system.db.execUpdate("Exchange/Iggy/Artifact/insert_artifact_memory", parameters)

	return {'html': 'OK'}
	