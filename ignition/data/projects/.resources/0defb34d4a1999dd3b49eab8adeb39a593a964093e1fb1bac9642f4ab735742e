logger = system.util.getLogger('api')

def _data_api_v1_scan_projects():
	base_url = 'http://central:8088'
	apiKey = 'es_testing:ysG_Rz1hmiRoZd8I6NOaILLN3sa2PqyldXhy6iHgLSk'
	headers = {"X-Ignition-API-Token": apiKey, "Content-Type":"application/json"}
	api_version = 'v1'
	
	url = base_url+'/data/api/'+api_version+'/scan/projects'
	client = system.net.httpClient(1000, bypassCertValidation=True)
	data = {}
	res = client.post(url, headers = headers, data = data)
	return res.json
	

import json

class api(object):
    """
    A base class for Ignition's API
    """

    # --- Class Variables for API Interaction Defaults ---
    API_BASE_URL = 'http://central:8088'
    API_TOKEN = 'es_testing:ysG_Rz1hmiRoZd8I6NOaILLN3sa2PqyldXhy6iHgLSk' #generated on the gateway
    API_VERSION = 'v1'

    def __init__(self, api_base_url=None, api_token=None, api_version=None):
        """
        Initializes the ProjectScanner instance.
        Allows overriding default API configuration settings.

        Args:
            api_base_url (str, optional): Base URL for the Ignition API.
                                          Defaults to ProjectScanner.API_BASE_URL.
            api_token (str, optional): API token for authentication.
                                       Defaults to ProjectScanner.API_TOKEN.
            api_version (str, optional): Version of the API to use.
                                         Defaults to ProjectScanner.API_VERSION.
        """
        self.api_base_url = api_base_url if api_base_url is not None else api.API_BASE_URL
        self.api_token = api_token if api_token is not None else api.API_TOKEN
        self.api_version = api_version if api_version is not None else api.API_VERSION

    def _data_api_v1_scan_projects(self):
        """
        Calls the '/data/api/v1/scan/projects' endpoint on an Ignition gateway
        to initiate a scan of all projects.

        Returns:
            dict: The JSON response from the API if the call is successful.

        Raises:
            Exception: If the API call fails (e.g., network error, non-2xx response).
        """
        url = "{}/data/api/{}/scan/projects".format(self.api_base_url, self.api_version)
        headers = {
            "X-Ignition-API-Token": self.api_token,
            "Content-Type": "application/json"
        }
        data = {}
        logger.info("Attempting to trigger project scan: POST %s" % url)
        client = system.net.httpClient(timeout=10000, bypassCertValidation=True)
        
        try:
            response = client.post(url, headers=headers, data=data)
            
            if response.good:
                return response.json
                logger.info("Successfully triggered project scan. Response: " + str(response_data))
            else:
                error_message = "API call to scan projects failed. Status: {}, URL: {}, Response: {}".format(
                    response.statusCode, url, response.text
                )
                raise Exception(error_message)
        except Exception as e:
            detailed_error_message = "Error during project scan operation for URL {}: {}".format(url, str(e))
            raise Exception(detailed_error_message)
    
    def _data_api_v1_scan_config(self):
        """
        Calls the '/data/api/v1/scan/congig' endpoint on an Ignition gateway
        to initiate a scan of gateway files.

        Returns:
            dict: The JSON response from the API if the call is successful.

        Raises:
            Exception: If the API call fails (e.g., network error, non-2xx response).
        """
        url = "{}/data/api/{}/scan/config".format(self.api_base_url, self.api_version)
        headers = {
            "X-Ignition-API-Token": self.api_token,
            "Content-Type": "application/json"
        }
        data = {}
        logger.info("Attempting to trigger config scan: POST %s" % url)
        client = system.net.httpClient(timeout=10000, bypassCertValidation=True)
        
        try:
            response = client.post(url, headers=headers, data=data)
            
            if response.good:
                return response.json
                logger.info("Successfully triggered config scan. Response: " + str(response_data))
            else:
                error_message = "API call to scan config failed. Status: {}, URL: {}, Response: {}".format(
                    response.statusCode, url, response.text
                )
                raise Exception(error_message)
        except Exception as e:
            detailed_error_message = "Error during config scan operation for URL {}: {}".format(url, str(e))
            raise Exception(detailed_error_message)
            
def example_call():
    try:
        apiInstance = api() 
        response_data = apiInstance._data_api_v1_scan_config(api_base_url='http://10.10.85.18:8088')
        logger.info("Successfull call. Response: " + str(response_data))
    except Exception as e:
        logger.error("Failed call: %s" % str(e)) # Use logger.error for errors
    return
	