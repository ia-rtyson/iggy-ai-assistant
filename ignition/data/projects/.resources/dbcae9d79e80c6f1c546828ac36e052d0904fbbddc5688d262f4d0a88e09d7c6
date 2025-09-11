def read_tag_history(tagPath, startDate, endDate):
    """
    Queries the tag historian for raw data points for a single tag within a specified date range.

    Note: The original hardcoded paths and dates inside this function have been commented out
    to allow the passed arguments to be used as intended.

    Args:
        tagPath (str): The full path of the tag to query (e.g., '[default]Motors/Motor 1/rpm_feedback').
        startDate (java.util.Date): The starting timestamp for the history query.
        endDate (java.util.Date): The ending timestamp for the history query.

    Returns:
        com.inductiveautomation.ignition.common.Dataset: A dataset containing the tag's history,
        with columns for timestamp, value, and quality.
    """
    # The following lines were likely for testing and are now commented out.
    # tagPaths = '[default]Motors/Motor 1/rpm_feedback'
    # endDate = system.date.now()
    # startDate = system.date.addMinutes(endDate, -1)
    
    res = system.historian.queryRawPoints([tagPath], startDate, endDate)
    
    return res

def read_values(tagPath='[default]Motors/Motor 1/rpm_feedback'):
    """
    Reads the current value, quality, and timestamp of a single tag.

    Args:
        tagPath (str, optional): The full path of the tag to read. 
                                 Defaults to '[default]Motors/Motor 1/rpm_feedback'.

    Returns:
        dict: A dictionary containing a JSON string representation of the read operation result.
              The JSON object includes the tag's value, quality, and timestamp.
    """
    ret = system.tag.readBlocking([tagPath])
    print type(ret)
    encoded = system.util.jsonEncode(ret)
    print type(encoded)
    return {'json': encoded}

def write_value(tagPath='[default]Writeable Tag', value=1):
    """
    Writes a value to a single tag synchronously.

    Args:
        tagPath (str, optional): The full path of the tag to write to. 
                                 Defaults to '[default]Writeable Tag'.
        value (any, optional): The value to write to the tag. Defaults to 1.
                               The data type should match the tag's expected data type.

    Returns:
        dict: A dictionary containing a JSON string representation of the write operation's
              quality code, which indicates if the write was successful.
    """
    ret = system.tag.writeBlocking([tagPath], [value])
    return {'json': system.util.jsonEncode(ret)}

def get_tag_paths():
    """
    Browses the '[default]' tag provider to retrieve the full paths of all tags.

    Returns:
        dict: A dictionary containing a JSON string representation of a list of tag paths.
              Example: {'json': "[{'tagPath': '[default]path/to/tag1'}, ...]" }
    """
    results = system.tag.browse(path='[default]', filter={})
    ret = []
    for tag in results:
	    if tag['name'] != '_types_':
	        ret.append({'tagPath': str(tag['fullPath'])})
    return {'json': system.util.jsonEncode(ret)}

def get_active_alarms():
    """
    Queries the alarm system for all currently active alarms (both acknowledged and unacknowledged).

    Returns:
        dict: A dictionary containing a JSON string representation of a list of alarms.
              Each item in the list is a dictionary containing the source tag path of the alarm.
    """
    alarms = system.alarm.queryStatus(state=["ActiveUnacked", "ActiveAcked"])
    ret = []
    
    for alarm in alarms:
        print alarm
        ret.append({
            'source': str(alarm.getSource())
        })
    return {'json': system.util.jsonEncode(ret)}