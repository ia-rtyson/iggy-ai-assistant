def doGet(request, session):
	from java.lang import Exception as JException
	query = request['params'].get('query', None)
	
	# ---- Validation ----------------------------------------------------
	if not query:
		# id is required – return a plain‑text 400 error
		request['servletResponse'].setStatus(400)
		request['servletResponse'].getWriter().print(
			"HTTP 400: Missing required query parameter 'query'.")
		return   # End the request
	
	queryName   = 'Exchange/Iggy/Instructions/search_instructions'
	queryParams = {'query': query}
	
	# ---- Execute the named query -------------------------------------
	try:
		# system.db.execQuery returns a list of dictionaries (rows)
		results = system.db.execQuery(queryName, queryParams)
		instructions = []
		for r in results:
			instruction = {}
			for k in results.columnNames:
				instruction[k] = r[k]
			instructions.append(instruction)
	except Exception as e:
		# If the database throws an exception we return a 500 error
		request['servletResponse'].setStatus(500)
		request['servletResponse'].getWriter().print(
			"HTTP 500: Database error – " + str(e))
		# Log the exception for troubleshooting
		system.util.getLogger('instruction-endpoint').error(
			"Query '%s' failed for id=%s: %s" % (queryName, query, e))
		return
	except JException as e:
		# If the database throws an exception we return a 500 error
		request['servletResponse'].setStatus(500)
		request['servletResponse'].getWriter().print(
			"HTTP 500: Database error – " + str(e))
		# Log the exception for troubleshooting
		system.util.getLogger('instruction-endpoint').error(
			"Query '%s' failed for id=%s: %s" % (queryName, query, e))
		return
	
	# ---- Build the JSON response --------------------------------------
	# We wrap the list of rows in a top‑level key so the caller can
	# always expect a JSON object.
#	responsePayload = {'instructions': results}
	
	# (Optional) Log what we returned – useful when debugging
	system.util.getLogger('instruction-endpoint').info(
		"Returned %d instruction rows for query=%s" %
		(len(results), query))
	
	# ---- Return the response ------------------------------------------
	# The framework will automatically JSON‑encode dictionaries,
	# so we simply return the payload.
	return {'json': instructions}