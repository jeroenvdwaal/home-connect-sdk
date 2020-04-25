# home_connect_sdk.CommandsApi

All URIs are relative to *https://api.home-connect.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_available_commands**](CommandsApi.md#get_available_commands) | **GET** /homeappliances/{haid}/commands | Get a list of supported commands of the home appliance
[**put_command**](CommandsApi.md#put_command) | **PUT** /homeappliances/{haid}/commands/{commandkey} | Execute a specific command of the home appliance


# **get_available_commands**
> get_available_commands(haid, accept_language=accept_language)

Get a list of supported commands of the home appliance

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
    api_instance = home_connect_sdk.CommandsApi(api_client)
    haid = 'haid_example' # str | ID of home appliance
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

    try:
        # Get a list of supported commands of the home appliance
        api_instance.get_available_commands(haid, accept_language=accept_language)
    except ApiException as e:
        print("Exception when calling CommandsApi->get_available_commands: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 
 **accept_language** | **str**| Language for localized assets | [optional] 

### Return type

void (empty response body)

### Authorization

[homeconnect_auth](../README.md#homeconnect_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.bsh.sdk.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The request was successful. Return a list of commands. |  -  |
**401** | Unauthorized - No or invalid access token |  -  |
**403** | Forbidden - Scope has not been granted |  -  |
**406** | The resource identified by the request is only capable of generating response entities which have content characteristics not acceptable according to the accept headers sent in the request. |  -  |
**408** | API Server failed to produce an answer or has no connection to backend service |  -  |
**429** | The number of requests for a specific endpoint exceeded the quota of the client.  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_command**
> put_command(haid, commandkey, body, accept_language=accept_language)

Execute a specific command of the home appliance

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
    api_instance = home_connect_sdk.CommandsApi(api_client)
    haid = 'haid_example' # str | ID of home appliance
commandkey = 'commandkey_example' # str | feature key of the command
body = home_connect_sdk.Command() # Command | description of the command to send
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

    try:
        # Execute a specific command of the home appliance
        api_instance.put_command(haid, commandkey, body, accept_language=accept_language)
    except ApiException as e:
        print("Exception when calling CommandsApi->put_command: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 
 **commandkey** | **str**| feature key of the command | 
 **body** | [**Command**](Command.md)| description of the command to send | 
 **accept_language** | **str**| Language for localized assets | [optional] 

### Return type

void (empty response body)

### Authorization

[homeconnect_auth](../README.md#homeconnect_auth)

### HTTP request headers

 - **Content-Type**: application/vnd.bsh.sdk.v1+json
 - **Accept**: application/vnd.bsh.sdk.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request was successful. |  -  |
**401** | Unauthorized - No or invalid access token |  -  |
**403** | Forbidden - Scope has not been granted |  -  |
**406** | The resource identified by the request is only capable of generating response entities which have content characteristics not acceptable according to the accept headers sent in the request. |  -  |
**408** | API Server failed to produce an answer or has no connection to backend service |  -  |
**429** | The number of requests for a specific endpoint exceeded the quota of the client.  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

