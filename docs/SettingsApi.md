# home_connect_sdk.SettingsApi

All URIs are relative to *https://api.home-connect.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setting**](SettingsApi.md#get_setting) | **GET** /homeappliances/{haid}/settings/{settingkey} | Get a specific setting
[**get_settings**](SettingsApi.md#get_settings) | **GET** /homeappliances/{haid}/settings | Get a list of available settings
[**set_setting**](SettingsApi.md#set_setting) | **PUT** /homeappliances/{haid}/settings/{settingkey} | Set a specific setting


# **get_setting**
> GetSetting get_setting(haid, settingkey, accept_language=accept_language)

Get a specific setting

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
    api_instance = home_connect_sdk.SettingsApi(api_client)
    haid = 'haid_example' # str | ID of home appliance
settingkey = 'settingkey_example' # str | ID of the setting
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

    try:
        # Get a specific setting
        api_response = api_instance.get_setting(haid, settingkey, accept_language=accept_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SettingsApi->get_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 
 **settingkey** | **str**| ID of the setting | 
 **accept_language** | **str**| Language for localized assets | [optional] 

### Return type

[**GetSetting**](GetSetting.md)

### Authorization

[homeconnect_auth](../README.md#homeconnect_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.bsh.sdk.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns setting successfully |  -  |
**401** | Unauthorized - No or invalid access token |  -  |
**403** | Forbidden - Scope has not been granted |  -  |
**404** | The requested resource was not found |  -  |
**406** | The resource identified by the request is only capable of generating response entities which have content characteristics not acceptable according to the accept headers sent in the request. |  -  |
**408** | API Server failed to produce an answer or has no connection to backend service |  -  |
**409** | An error occured during communication with the home appliance or the home appliance itself answered with an error, e.g. because the issued command was unacceptable in the current state.  |  -  |
**429** | The number of requests for a specific endpoint exceeded the quota of the client.  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings**
> ArrayOfSettings get_settings(haid, accept_language=accept_language)

Get a list of available settings

Get a list of available setting of the home appliance.  Further documentation can be found here: * [Power state](https://developer.home-connect.com/docs/settings/power_state) * [Fridge temperature](https://developer.home-connect.com/docs/api/settings/fridgetemperature) * [Fridge super mode](https://developer.home-connect.com/docs/api/settings/fridgesupermode) * [Freezer temperature](https://developer.home-connect.com/docs/api/settings/freezertemperature) * [Freezer super mode](https://developer.home-connect.com/docs/api/settings/freezersupermode) 

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
    api_instance = home_connect_sdk.SettingsApi(api_client)
    haid = 'haid_example' # str | ID of home appliance
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

    try:
        # Get a list of available settings
        api_response = api_instance.get_settings(haid, accept_language=accept_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SettingsApi->get_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 
 **accept_language** | **str**| Language for localized assets | [optional] 

### Return type

[**ArrayOfSettings**](ArrayOfSettings.md)

### Authorization

[homeconnect_auth](../README.md#homeconnect_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.bsh.sdk.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Available settings |  -  |
**401** | Unauthorized - No or invalid access token |  -  |
**403** | Forbidden - Scope has not been granted |  -  |
**408** | API Server failed to produce an answer or has no connection to backend service |  -  |
**429** | The number of requests for a specific endpoint exceeded the quota of the client.  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_setting**
> set_setting(haid, settingkey, body, accept_language=accept_language)

Set a specific setting

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
    api_instance = home_connect_sdk.SettingsApi(api_client)
    haid = 'haid_example' # str | ID of home appliance
settingkey = 'settingkey_example' # str | ID of the setting
body = home_connect_sdk.PutSetting() # PutSetting | description of the setting
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

    try:
        # Set a specific setting
        api_instance.set_setting(haid, settingkey, body, accept_language=accept_language)
    except ApiException as e:
        print("Exception when calling SettingsApi->set_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 
 **settingkey** | **str**| ID of the setting | 
 **body** | [**PutSetting**](PutSetting.md)| description of the setting | 
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
**204** | Setting updated successfully |  -  |
**401** | Unauthorized - No or invalid access token |  -  |
**403** | Forbidden - Scope has not been granted |  -  |
**404** | The requested resource was not found |  -  |
**406** | The resource identified by the request is only capable of generating response entities which have content characteristics not acceptable according to the accept headers sent in the request. |  -  |
**408** | API Server failed to produce an answer or has no connection to backend service |  -  |
**409** | An error occured during communication with the home appliance or the home appliance itself answered with an error, e.g. because the issued command was unacceptable in the current state.  |  -  |
**415** | The request&#39;s Content-Type is not supported. |  -  |
**429** | The number of requests for a specific endpoint exceeded the quota of the client.  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

