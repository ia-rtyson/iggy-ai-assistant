def doPut(request, session):
	import os, shutil
	
	viewJson = request["data"]["view"] if "view" in request["data"] else None
	viewPath = request["data"]["path"] if "path" in request["data"] else None
	project = request["data"]["project"] if "project" in request["data"] else None
	
	if not viewJson or not viewPath or not project:
		request['servletResponse'].setStatus(400)
		request['servletResponse'].getWriter().print("HTTP 400: Missing view JSON, view path, or project name.")
		return
	
	directoryPath = "data/projects/%s/com.inductiveautomation.perspective/views/%s" %(project, viewPath)

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
	      "timestamp": str(system.date.now().toInstant())
	    }
#	    "lastModificationSignature": "49b6635d2ea5de25faa08d67abac4bb97c9aa406faa744acdc7cbb060aa6e8ea"
	  }
	}
	system.util.getLogger('testviewwrite').info(viewJson)
	
	
	if os.path.exists(directoryPath):
		if os.path.exists(directoryPath + '_previous'):
			if os.path.exists(directoryPath + '_previousBAK'):
				shutil.rmtree(directoryPath + '_previousBAK', ignore_errors=True)
			os.rename(directoryPath + '_previous', directoryPath + '_previousBAK')
		try:
			os.rename(directoryPath, directoryPath + '_previous')
			if os.path.exists(directoryPath + '_previousBAK'):
				shutil.rmtree(directoryPath + '_previousBAK', ignore_errors=True)
		except:
			if os.path.exists(directoryPath + '_previousBAK'):
				shutil.rmtree(directoryPath + '_previousBAK', directoryPath + '_previous', ignore_errors=True)
			request['servletResponse'].setStatus(500)
			request['servletResponse'].getWriter().print("HTTP 500: Failed to write View JSON.")
			return
	
	system.file.writeFile(directoryPath + "/view.json", system.util.jsonEncode(system.util.jsonDecode(viewJson), 2))
#	system.util.getLogger('testviewwrite').info(system.util.jsonEncode(resourceJson, 2))
	system.file.writeFile(directoryPath + "/resource.json", system.util.jsonEncode(resourceJson, 2))
	system.project.requestScan()

	return {'html': 'OK'}