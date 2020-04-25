# home_connect_sdk.DefaultApi

All URIs are relative to *https://api.home-connect.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_home_appliances**](DefaultApi.md#get_home_appliances) | **GET** /homeappliances | Get all home appliances which are paired with the logged-in user account.
[**get_specific_appliance**](DefaultApi.md#get_specific_appliance) | **GET** /homeappliances/{haid} | Get a specfic home appliances which are paired with the logged-in user account.


# **get_home_appliances**
> ArrayOfHomeAppliances get_home_appliances()

Get all home appliances which are paired with the logged-in user account.

This endpoint returns a list of all home appliances which are paired with the logged-in user account. All paired home appliances are returned independent of their current connection state. The connection state can be retrieved within the field 'connected' of the respective home appliance. The haId is the primary access key for further API access to a specific home appliance. 

### Example

* OAuth Authentication (homeconnect_auth):
```python
from __future__ import print_function
import time
import home_connect_sdk
from home_connect_sdk.rest import ApiException
from pprint import pprint
configuration = home_connect_sdk.Configuration()
# Configure OAuth2 access token for authorization: homeconnect_auth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.home-connect.com/api
configuration.host = "https://api.home-connect.com/api"

# Enter a context with an instance of the API client
with home_connect_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = home_connect_sdk.DefaultApi(api_client)
    
    try:
        # Get all home appliances which are paired with the logged-in user account.
        api_response = api_instance.get_home_appliances()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_home_appliances: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ArrayOfHomeAppliances**](ArrayOfHomeAppliances.md)

### Authorization

[homeconnect_auth](../README.md#homeconnect_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.bsh.sdk.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of home appliances |  -  |
**401** | Unauthorized - No or invalid access token |  -  |
**403** | Forbidden - Scope has not been granted |  -  |
**406** | The resource identified by the request is only capable of generating response entities which have content characteristics not acceptable according to the accept headers sent in the request. |  -  |
**429** | The number of requests for a specific endpoint exceeded the quota of the client.  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_specific_appliance**
> HomeAppliance get_specific_appliance(haid)

Get a specfic home appliances which are paired with the logged-in user account.

This endpoint returns a specific home appliance which is paired with the logged-in user account. It is returned independent of their current connection state. The connection state can be retrieved within the field 'connected' of the respective home appliance. The haId is the primary access key for further API access to a specific home appliance. 

### Example

* OAuth Authentication (homeconnect_auth):
```python
from __future__ import print_function
import time
import home_connect_sdk
from home_connect_sdk.rest import ApiException
from pprint import pprint
configuration = home_connect_sdk.Configuration()
# Configure OAuth2 access token for authorization: homeconnect_auth
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.home-connect.com/api
configuration.host = "https://api.home-connect.com/api"

# Enter a context with an instance of the API client
with home_connect_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = home_connect_sdk.DefaultApi(api_client)
    haid = 'haid_example' # str | ID of home appliance

    try:
        # Get a specfic home appliances which are paired with the logged-in user account.
        api_response = api_instance.get_specific_appliance(haid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_specific_appliance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 

### Return type

[**HomeAppliance**](HomeAppliance.md)

### Authorization

[homeconnect_auth](../README.md#homeconnect_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.bsh.sdk.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of requested home appliance |  -  |
**401** | Unauthorized - No or invalid access token |  -  |
**403** | Forbidden - Scope has not been granted |  -  |
**406** | The resource identified by the request is only capable of generating response entities which have content characteristics not acceptable according to the accept headers sent in the request. |  -  |
**429** | The number of requests for a specific endpoint exceeded the quota of the client.  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

