def getHourlyAverageHistory(tagPaths, hoursBack=8):
    try:
        endDate = system.date.now()
        startDate = system.date.addHours(endDate, -hoursBack)

        historicalData = system.tag.queryTagHistory(
            paths=tagPaths,
            startDate=startDate,
            endDate=endDate,
            aggregationMode="Average",
            intervalHours=1,
            returnFormat="Wide"
        )

        return historicalData

    except Exception as e:
        print "Error querying tag history: " + str(e)
        return None