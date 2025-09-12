def doPut(request, session):
	from java.lang import Exception as JException
	name = request['data'].get('name', None)
	description = request['data'].get('description', None)
	content = request['data'].get('content', None)
	
	# ---- Validation ----------------------------------------------------
	if not name or not description or not content:
		# id is required – return a plain‑text 400 error
		request['servletResponse'].setStatus(400)
		request['servletResponse'].getWriter().print(
			"HTTP 400: Missing required data 'name' or 'description' or 'content'.")
		return   # End the request
	
	queryName   = 'Exchange/Iggy/Instructions/upsert_instruction'
	queryParams = {
		'name': name,
		'description': description,
		'content': content
	}
	
	# ---- Execute the named query -------------------------------------
	try:
		# system.db.execQuery returns a list of dictionaries (rows)
		results = system.db.execQuery(queryName, queryParams)
	except Exception as e:
		# If the database throws an exception we return a 500 error
		request['servletResponse'].setStatus(500)
		request['servletResponse'].getWriter().print(
			"HTTP 500: Database error – " + str(e))
		# Log the exception for troubleshooting
		system.util.getLogger('instruction-endpoint').error(
			"Query '%s' failed for name=%s: %s" % (queryName, name, e))
		return
	except JException as e:
		# If the database throws an exception we return a 500 error
		request['servletResponse'].setStatus(500)
		request['servletResponse'].getWriter().print(
			"HTTP 500: Database error – " + str(e))
		# Log the exception for troubleshooting
		system.util.getLogger('instruction-endpoint').error(
			"Query '%s' failed for name=%s: %s" % (queryName, name, e))
		return
	
	# (Optional) Log what we returned – useful when debugging
	system.util.getLogger('instruction-endpoint').info(
		"Upserted instruction for name=%s" %
		(name,))
	
	# ---- Return the response ------------------------------------------
	# The framework will automatically JSON‑encode dictionaries,
	# so we simply return the payload.
	return {'response': 'ok'}