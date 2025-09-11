def doGet(request, session):
#	viewJson = request["data"]["view"] if "view" in request["data"] else None
	viewPath = request["data"]["path"] if "path" in request["data"] else None
	project = request["data"]["project"] if "project" in request["data"] else None
	
	if not viewPath or not project:
		request['servletResponse'].setStatus(400)
		request['servletResponse'].getWriter().print("HTTP 400: Missing view path and project name.")
		return
	
	directoryPath = "data/projects/%s/com.inductiveautomation.perspective/views/%s/" %(project, viewPath)

	try:
		viewJson = system.util.jsonDecode(system.file.readFileAsString(directoryPath + "view.json"))
	except Exception as e:
		if "doesn't exist or isn't a file" in e.message:
			request['servletResponse'].setStatus(404)
			request['servletResponse'].getWriter().print("HTTP 404: View not found.")
		else:
			request['servletResponse'].setStatus(500)
			request['servletResponse'].getWriter().print("HTTP 500: IOError reading file.")
#	system.util.getLogger('testviewwrite').info(system.util.jsonEncode(resourceJson, 2))
	return {'json': {'view': viewJson, 'path': viewPath, 'project': project, 'status': '200'}}