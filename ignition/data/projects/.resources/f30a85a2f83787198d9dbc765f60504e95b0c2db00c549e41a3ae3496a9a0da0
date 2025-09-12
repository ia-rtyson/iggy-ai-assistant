def doGet(request, session):
	import os
	
	widgetsPath   = "Exchange/Staging/Widgets"
	directoryPath = "data/projects/%s/com.inductiveautomation.perspective/views/%s/" % (
	                    system.project.getProjectName(), widgetsPath)
	
	widgets = []
	logger  = system.util.getLogger('get-widgets')
	
	for root, dirs, files in os.walk(directoryPath):
	    if 'view.json' not in files:
	        continue
	
	    view_path = os.path.join(root, 'view.json')
	    try:
	        with open(view_path, 'r') as f:
	            json_text = f.read()
	
	        data = system.util.jsonDecode(json_text)
	
	        widgetInfo = None
	        if isinstance(data, dict):
	            custom = data.get('custom')
	            if isinstance(custom, dict):
	                widgetInfo = custom.get('widgetInfo')
	
	        if widgetInfo is not None:
	            widgets.append(widgetInfo)
	        else:
	            logger.warn("view.json %s does not contain custom.widgetInfo", view_path)
	
	    except Exception as e:
	        msg = str(e)
	
	        if "doesn't exist" in msg or "No such file" in msg:
	            request['servletResponse'].setStatus(404)
	            request['servletResponse'].getWriter().print(
	                "HTTP 404: View not found.")
	        else:
	            logger.error("Error reading %s: %s", view_path, msg)
	            request['servletResponse'].setStatus(500)
	            request['servletResponse'].getWriter().print(
	                "HTTP 500: IOError reading file.")
	
	        return {'json': {'widgets': widgets}}
	
	return {'json': {'widgets': widgets}}