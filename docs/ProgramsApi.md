# home_connect_sdk.ProgramsApi

All URIs are relative to *https://api.home-connect.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_active_program**](ProgramsApi.md#get_active_program) | **GET** /homeappliances/{haid}/programs/active | Get program which is currently executed
[**get_active_program_option**](ProgramsApi.md#get_active_program_option) | **GET** /homeappliances/{haid}/programs/active/options/{optionkey} | Get one specific option of the active program, e.g. the duration.
[**get_active_program_options**](ProgramsApi.md#get_active_program_options) | **GET** /homeappliances/{haid}/programs/active/options | Get all options of the active program like temperature or duration.
[**get_all_programs**](ProgramsApi.md#get_all_programs) | **GET** /homeappliances/{haid}/programs | Get all programs of a given home appliance
[**get_available_program**](ProgramsApi.md#get_available_program) | **GET** /homeappliances/{haid}/programs/available/{programkey} | Get specific available program
[**get_available_programs**](ProgramsApi.md#get_available_programs) | **GET** /homeappliances/{haid}/programs/available | Get all programs which are currently available on the given home appliance
[**get_selected_program**](ProgramsApi.md#get_selected_program) | **GET** /homeappliances/{haid}/programs/selected | Get the program which is currently selected 
[**get_selected_program_option**](ProgramsApi.md#get_selected_program_option) | **GET** /homeappliances/{haid}/programs/selected/options/{optionkey} | Get specific option of selected program
[**get_selected_program_options**](ProgramsApi.md#get_selected_program_options) | **GET** /homeappliances/{haid}/programs/selected/options | Get all options of selected program
[**set_active_program_option**](ProgramsApi.md#set_active_program_option) | **PUT** /homeappliances/{haid}/programs/active/options/{optionkey} | Set one specific option of the active program
[**set_active_program_options**](ProgramsApi.md#set_active_program_options) | **PUT** /homeappliances/{haid}/programs/active/options | Set all options of the active program, e.g. to switch from preheating to the actual program options.
[**set_selected_program**](ProgramsApi.md#set_selected_program) | **PUT** /homeappliances/{haid}/programs/selected | Select a program
[**set_selected_program_option**](ProgramsApi.md#set_selected_program_option) | **PUT** /homeappliances/{haid}/programs/selected/options/{optionkey} | Set specific option of selected program
[**set_selected_program_options**](ProgramsApi.md#set_selected_program_options) | **PUT** /homeappliances/{haid}/programs/selected/options | Set all options of selected program
[**start_program**](ProgramsApi.md#start_program) | **PUT** /homeappliances/{haid}/programs/active | Start the given program
[**stop_program**](ProgramsApi.md#stop_program) | **DELETE** /homeappliances/{haid}/programs/active | Stop the program which is currently executed


# **get_active_program**
> Program get_active_program(haid, accept_language=accept_language)

Get program which is currently executed

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
    api_instance = home_connect_sdk.ProgramsApi(api_client)
    haid = 'haid_example' # str | ID of home appliance
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

    try:
        # Get program which is currently executed
        api_response = api_instance.get_active_program(haid, accept_language=accept_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProgramsApi->get_active_program: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 
 **accept_language** | **str**| Language for localized assets | [optional] 

### Return type

[**Program**](Program.md)

### Authorization

[homeconnect_auth](../README.md#homeconnect_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.bsh.sdk.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | active program |  -  |
**401** | Unauthorized - No or invalid access token |  -  |
**403** | Forbidden - Scope has not been granted |  -  |
**404** | No program is currently active |  -  |
**406** | The resource identified by the request is only capable of generating response entities which have content characteristics not acceptable according to the accept headers sent in the request. |  -  |
**409** | An error occured during communication with the home appliance or the home appliance itself answered with an error, e.g. because the issued command was unacceptable in the current state.  |  -  |
**429** | The number of requests for a specific endpoint exceeded the quota of the client.  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_program_option**
> Option get_active_program_option(haid, optionkey, accept_language=accept_language)

Get one specific option of the active program, e.g. the duration.

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
    api_instance = home_connect_sdk.ProgramsApi(api_client)
    haid = 'haid_example' # str | ID of home appliance
optionkey = 'optionkey_example' # str | Key of the option, e.g. BSH.Common.Option.Duration
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

    try:
        # Get one specific option of the active program, e.g. the duration.
        api_response = api_instance.get_active_program_option(haid, optionkey, accept_language=accept_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProgramsApi->get_active_program_option: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 
 **optionkey** | **str**| Key of the option, e.g. BSH.Common.Option.Duration | 
 **accept_language** | **str**| Language for localized assets | [optional] 

### Return type

[**Option**](Option.md)

### Authorization

[homeconnect_auth](../README.md#homeconnect_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.bsh.sdk.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Option of active program |  -  |
**401** | Unauthorized - No or invalid access token |  -  |
**403** | Forbidden - Scope has not been granted |  -  |
**404** | No program is currently active |  -  |
**406** | The resource identified by the request is only capable of generating response entities which have content characteristics not acceptable according to the accept headers sent in the request. |  -  |
**429** | The number of requests for a specific endpoint exceeded the quota of the client.  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_program_options**
> ArrayOfOptions get_active_program_options(haid, accept_language=accept_language)

Get all options of the active program like temperature or duration.

You can retrieve a list of options of the currently running program.  For detailed documentation of the available options, visit the appliance-specific programs pages: * [Oven](https://developer.home-connect.com/docs/oven/supported_programs_and_options) * [Dishwasher](https://developer.home-connect.com/docs/dishwasher/supported_programs_options) * [Washer](https://developer.home-connect.com/docs/washing-machine/supported_programs_and_options) * [Dryer](https://developer.home-connect.com/docs/dryer/supported_programs_and_options) * [Coffee Machine](https://developer.home-connect.com/docs/coffee-maker/supported_programs_and_options) * [Hood](https://developer.home-connect.com/docs/hood/supported_programs_and_options) * [Cleaning Robot](https://developer.home-connect.com/docs/cleaningrobot/supported_programs_and_options) 

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
    api_instance = home_connect_sdk.ProgramsApi(api_client)
    haid = 'haid_example' # str | ID of home appliance
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

    try:
        # Get all options of the active program like temperature or duration.
        api_response = api_instance.get_active_program_options(haid, accept_language=accept_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProgramsApi->get_active_program_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 
 **accept_language** | **str**| Language for localized assets | [optional] 

### Return type

[**ArrayOfOptions**](ArrayOfOptions.md)

### Authorization

[homeconnect_auth](../README.md#homeconnect_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.bsh.sdk.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of options of active program |  -  |
**401** | Unauthorized - No or invalid access token |  -  |
**403** | Forbidden - Scope has not been granted |  -  |
**404** | No program is currently active |  -  |
**406** | The resource identified by the request is only capable of generating response entities which have content characteristics not acceptable according to the accept headers sent in the request. |  -  |
**429** | The number of requests for a specific endpoint exceeded the quota of the client.  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_programs**
> ArrayOfPrograms get_all_programs(haid, accept_language=accept_language)

Get all programs of a given home appliance

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
    api_instance = home_connect_sdk.ProgramsApi(api_client)
    haid = 'haid_example' # str | ID of home appliance
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

    try:
        # Get all programs of a given home appliance
        api_response = api_instance.get_all_programs(haid, accept_language=accept_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProgramsApi->get_all_programs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 
 **accept_language** | **str**| Language for localized assets | [optional] 

### Return type

[**ArrayOfPrograms**](ArrayOfPrograms.md)

### Authorization

[homeconnect_auth](../README.md#homeconnect_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.bsh.sdk.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All programs |  -  |
**401** | Unauthorized - No or invalid access token |  -  |
**403** | Forbidden - Scope has not been granted |  -  |
**406** | The resource identified by the request is only capable of generating response entities which have content characteristics not acceptable according to the accept headers sent in the request. |  -  |
**409** | Command/Query cannot be executed for the home appliance, the error response contains the error details |  -  |
**429** | The number of requests for a specific endpoint exceeded the quota of the client.  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_program**
> ProgramDefinition get_available_program(haid, programkey, accept_language=accept_language)

Get specific available program

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
    api_instance = home_connect_sdk.ProgramsApi(api_client)
    haid = 'haid_example' # str | ID of home appliance
programkey = 'programkey_example' # str | key of specific program to return
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

    try:
        # Get specific available program
        api_response = api_instance.get_available_program(haid, programkey, accept_language=accept_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProgramsApi->get_available_program: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 
 **programkey** | **str**| key of specific program to return | 
 **accept_language** | **str**| Language for localized assets | [optional] 

### Return type

[**ProgramDefinition**](ProgramDefinition.md)

### Authorization

[homeconnect_auth](../README.md#homeconnect_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.bsh.sdk.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Available program |  -  |
**401** | Unauthorized - No or invalid access token |  -  |
**403** | Forbidden - Scope has not been granted |  -  |
**406** | The resource identified by the request is only capable of generating response entities which have content characteristics not acceptable according to the accept headers sent in the request. |  -  |
**409** | The requested program is not available |  -  |
**429** | The number of requests for a specific endpoint exceeded the quota of the client.  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_programs**
> ArrayOfAvailablePrograms get_available_programs(haid, accept_language=accept_language)

Get all programs which are currently available on the given home appliance

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
    api_instance = home_connect_sdk.ProgramsApi(api_client)
    haid = 'haid_example' # str | ID of home appliance
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

    try:
        # Get all programs which are currently available on the given home appliance
        api_response = api_instance.get_available_programs(haid, accept_language=accept_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProgramsApi->get_available_programs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 
 **accept_language** | **str**| Language for localized assets | [optional] 

### Return type

[**ArrayOfAvailablePrograms**](ArrayOfAvailablePrograms.md)

### Authorization

[homeconnect_auth](../README.md#homeconnect_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.bsh.sdk.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Available programs |  -  |
**401** | Unauthorized - No or invalid access token |  -  |
**403** | Forbidden - Scope has not been granted |  -  |
**406** | The resource identified by the request is only capable of generating response entities which have content characteristics not acceptable according to the accept headers sent in the request. |  -  |
**409** | Request cannot be performed since the OperationState is wrong |  -  |
**429** | The number of requests for a specific endpoint exceeded the quota of the client.  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_selected_program**
> Program get_selected_program(haid, accept_language=accept_language)

Get the program which is currently selected 

In most cases the selected program is the program which is currently shown on the display of the home appliance. This program can then be manually adjusted or started on the home appliance itself. 

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
    api_instance = home_connect_sdk.ProgramsApi(api_client)
    haid = 'haid_example' # str | ID of home appliance
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

    try:
        # Get the program which is currently selected 
        api_response = api_instance.get_selected_program(haid, accept_language=accept_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProgramsApi->get_selected_program: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 
 **accept_language** | **str**| Language for localized assets | [optional] 

### Return type

[**Program**](Program.md)

### Authorization

[homeconnect_auth](../README.md#homeconnect_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.bsh.sdk.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Selected program |  -  |
**401** | Unauthorized - No or invalid access token |  -  |
**403** | Forbidden - Scope has not been granted |  -  |
**404** | No program is currently selected |  -  |
**406** | The resource identified by the request is only capable of generating response entities which have content characteristics not acceptable according to the accept headers sent in the request. |  -  |
**429** | The number of requests for a specific endpoint exceeded the quota of the client.  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_selected_program_option**
> Option get_selected_program_option(haid, optionkey, accept_language=accept_language)

Get specific option of selected program

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
    api_instance = home_connect_sdk.ProgramsApi(api_client)
    haid = 'haid_example' # str | ID of home appliance
optionkey = 'optionkey_example' # str | Feature Key of the option as defined in FMF, e.g. BSH.Common.Option.Duration
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

    try:
        # Get specific option of selected program
        api_response = api_instance.get_selected_program_option(haid, optionkey, accept_language=accept_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProgramsApi->get_selected_program_option: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 
 **optionkey** | **str**| Feature Key of the option as defined in FMF, e.g. BSH.Common.Option.Duration | 
 **accept_language** | **str**| Language for localized assets | [optional] 

### Return type

[**Option**](Option.md)

### Authorization

[homeconnect_auth](../README.md#homeconnect_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.bsh.sdk.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Option of selected program |  -  |
**401** | Unauthorized - No or invalid access token |  -  |
**403** | Forbidden - Scope has not been granted |  -  |
**404** | No program is currently selected |  -  |
**406** | The resource identified by the request is only capable of generating response entities which have content characteristics not acceptable according to the accept headers sent in the request. |  -  |
**429** | The number of requests for a specific endpoint exceeded the quota of the client.  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_selected_program_options**
> ArrayOfOptions get_selected_program_options(haid, accept_language=accept_language)

Get all options of selected program

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
    api_instance = home_connect_sdk.ProgramsApi(api_client)
    haid = 'haid_example' # str | ID of home appliance
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

    try:
        # Get all options of selected program
        api_response = api_instance.get_selected_program_options(haid, accept_language=accept_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProgramsApi->get_selected_program_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 
 **accept_language** | **str**| Language for localized assets | [optional] 

### Return type

[**ArrayOfOptions**](ArrayOfOptions.md)

### Authorization

[homeconnect_auth](../README.md#homeconnect_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.bsh.sdk.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of options of selected program |  -  |
**401** | Unauthorized - No or invalid access token |  -  |
**403** | Forbidden - Scope has not been granted |  -  |
**404** | No program is currently selected |  -  |
**406** | The resource identified by the request is only capable of generating response entities which have content characteristics not acceptable according to the accept headers sent in the request. |  -  |
**429** | The number of requests for a specific endpoint exceeded the quota of the client.  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_active_program_option**
> set_active_program_option(haid, optionkey, body, accept_language=accept_language)

Set one specific option of the active program

This operation can be used to modify one specific option of the active program, e.g. to extend the duration of the active program by another 5 minutes.  Please note that changing options of the running program is currently only supported by ovens. 

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
    api_instance = home_connect_sdk.ProgramsApi(api_client)
    haid = 'haid_example' # str | ID of home appliance
optionkey = 'optionkey_example' # str | Key of the option, e.g. BSH.Common.Option.Duration
body = home_connect_sdk.Option() # Option | option of the active program to set
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

    try:
        # Set one specific option of the active program
        api_instance.set_active_program_option(haid, optionkey, body, accept_language=accept_language)
    except ApiException as e:
        print("Exception when calling ProgramsApi->set_active_program_option: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 
 **optionkey** | **str**| Key of the option, e.g. BSH.Common.Option.Duration | 
 **body** | [**Option**](Option.md)| option of the active program to set | 
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
**204** | The request was successful |  -  |
**401** | Unauthorized - No or invalid access token |  -  |
**403** | Forbidden - Scope has not been granted |  -  |
**406** | The resource identified by the request is only capable of generating response entities which have content characteristics not acceptable according to the accept headers sent in the request. |  -  |
**408** | API Server failed to produce an answer or has no connection to backend service |  -  |
**409** | No program is currently active |  -  |
**415** | The request&#39;s Content-Type is not supported. |  -  |
**429** | The number of requests for a specific endpoint exceeded the quota of the client.  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_active_program_options**
> set_active_program_options(haid, body, accept_language=accept_language)

Set all options of the active program, e.g. to switch from preheating to the actual program options.

Update the options for the currently running program. With this API endpoint, you have to provide all options with their new values. If you want to update only one option, you can use the endpoint specific to that option.  Please note that changing options of the running program is currently only supported by ovens. 

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
    api_instance = home_connect_sdk.ProgramsApi(api_client)
    haid = 'haid_example' # str | ID of home appliance
body = home_connect_sdk.ArrayOfOptions() # ArrayOfOptions | list of options
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

    try:
        # Set all options of the active program, e.g. to switch from preheating to the actual program options.
        api_instance.set_active_program_options(haid, body, accept_language=accept_language)
    except ApiException as e:
        print("Exception when calling ProgramsApi->set_active_program_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 
 **body** | [**ArrayOfOptions**](ArrayOfOptions.md)| list of options | 
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
**204** | OK |  -  |
**401** | Unauthorized - No or invalid access token |  -  |
**403** | Forbidden - Scope has not been granted |  -  |
**406** | The resource identified by the request is only capable of generating response entities which have content characteristics not acceptable according to the accept headers sent in the request. |  -  |
**408** | API Server failed to produce an answer or has no connection to backend service |  -  |
**409** | No program is currently active |  -  |
**415** | The request&#39;s Content-Type is not supported. |  -  |
**429** | The number of requests for a specific endpoint exceeded the quota of the client.  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_selected_program**
> set_selected_program(haid, body, accept_language=accept_language)

Select a program

In most cases the selected program is the program which is currently shown on the display of the home appliance. This program can then be manually adjusted or started on the home appliance itself.  A selected program will not be started automatically. You don't have to set a program as selected first if you intend to start it via API - you can set it directly as active program.  Selecting a program will update the available options and constraints directly from the home appliance. Any changes to the available options due to the state of the appliance is only reflected in the selected program. 

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
    api_instance = home_connect_sdk.ProgramsApi(api_client)
    haid = 'haid_example' # str | ID of home appliance
body = home_connect_sdk.Program() # Program | program to select
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

    try:
        # Select a program
        api_instance.set_selected_program(haid, body, accept_language=accept_language)
    except ApiException as e:
        print("Exception when calling ProgramsApi->set_selected_program: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 
 **body** | [**Program**](Program.md)| program to select | 
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
**204** | OK |  -  |
**401** | Unauthorized - No or invalid access token |  -  |
**403** | Forbidden - Scope has not been granted |  -  |
**406** | The resource identified by the request is only capable of generating response entities which have content characteristics not acceptable according to the accept headers sent in the request. |  -  |
**408** | API Server failed to produce an answer or has no connection to backend service |  -  |
**409** | An error occured during communication with the home appliance or the home appliance itself answered with an error, e.g. because the issued command was unacceptable in the current state.  |  -  |
**415** | The request&#39;s Content-Type is not supported. |  -  |
**429** | The number of requests for a specific endpoint exceeded the quota of the client.  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_selected_program_option**
> set_selected_program_option(haid, optionkey, body, accept_language=accept_language)

Set specific option of selected program

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
    api_instance = home_connect_sdk.ProgramsApi(api_client)
    haid = 'haid_example' # str | ID of home appliance
optionkey = 'optionkey_example' # str | Feature Key of the option as defined in FMF, e.g. BSH.Common.Option.Duration
body = home_connect_sdk.Option() # Option | description of the program to activate
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

    try:
        # Set specific option of selected program
        api_instance.set_selected_program_option(haid, optionkey, body, accept_language=accept_language)
    except ApiException as e:
        print("Exception when calling ProgramsApi->set_selected_program_option: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 
 **optionkey** | **str**| Feature Key of the option as defined in FMF, e.g. BSH.Common.Option.Duration | 
 **body** | [**Option**](Option.md)| description of the program to activate | 
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
**204** | The request was successful |  -  |
**401** | Unauthorized - No or invalid access token |  -  |
**403** | Forbidden - Scope has not been granted |  -  |
**406** | The resource identified by the request is only capable of generating response entities which have content characteristics not acceptable according to the accept headers sent in the request. |  -  |
**408** | API Server failed to produce an answer or has no connection to backend service |  -  |
**409** | No program is currently selected |  -  |
**415** | The request&#39;s Content-Type is not supported. |  -  |
**429** | The number of requests for a specific endpoint exceeded the quota of the client.  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_selected_program_options**
> set_selected_program_options(haid, body, accept_language=accept_language)

Set all options of selected program

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
    api_instance = home_connect_sdk.ProgramsApi(api_client)
    haid = 'haid_example' # str | ID of home appliance
body = home_connect_sdk.ArrayOfOptions() # ArrayOfOptions | description of the program to activate
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

    try:
        # Set all options of selected program
        api_instance.set_selected_program_options(haid, body, accept_language=accept_language)
    except ApiException as e:
        print("Exception when calling ProgramsApi->set_selected_program_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 
 **body** | [**ArrayOfOptions**](ArrayOfOptions.md)| description of the program to activate | 
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
**204** | The request was successful |  -  |
**401** | Unauthorized - No or invalid access token |  -  |
**403** | Forbidden - Scope has not been granted |  -  |
**406** | The resource identified by the request is only capable of generating response entities which have content characteristics not acceptable according to the accept headers sent in the request. |  -  |
**408** | API Server failed to produce an answer or has no connection to backend service |  -  |
**409** | No program is currently selected |  -  |
**415** | The request&#39;s Content-Type is not supported. |  -  |
**429** | The number of requests for a specific endpoint exceeded the quota of the client.  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_program**
> start_program(haid, body, accept_language=accept_language)

Start the given program

By putting a program object to this endpoint, the system will try to start it if all preconditions are fulfilled: * Home appliance is connected * *Remote Control* and *Remote Control Start Allowed* is enabled * No other program is currently active  Furthermore, the program must exist on the home appliance and its options must be set correctly. Keys of program, which can be exected on an oven, are for instance: * *Cooking.Oven.Program.HeatingMode.HotAir* * *Cooking.Oven.Program.HeatingMode.TopBottomHeating* * *Cooking.Oven.Program.HeatingMode.PizzaSetting* * *Cooking.Oven.Program.HeatingMode.PreHeating*  Keys for options of these oven programs are: * *Cooking.Oven.Option.SetpointTemperature*: 30 - 250 °C * *BSH.Common.Option.Duration*: 1 - 86340 seconds  For further documentation, visit the appliance-specific programs pages: * [Oven](https://developer.home-connect.com/docs/oven/supported_programs_and_options) * [Dishwasher](https://developer.home-connect.com/docs/dishwasher/supported_programs_options) * [Washer](https://developer.home-connect.com/docs/washing-machine/supported_programs_and_options) * [Dryer](https://developer.home-connect.com/docs/dryer/supported_programs_and_options) * [Coffee Machine](https://developer.home-connect.com/docs/coffee-maker/supported_programs_and_options) * [Hood](https://developer.home-connect.com/docs/hood/supported_programs_and_options) * [Cleaning Robot](https://developer.home-connect.com/docs/cleaningrobot/supported_programs_and_options)  There are no programs available for fridges and hobs. 

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
    api_instance = home_connect_sdk.ProgramsApi(api_client)
    haid = 'haid_example' # str | ID of home appliance
body = home_connect_sdk.Program() # Program | description of the program to activate
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

    try:
        # Start the given program
        api_instance.start_program(haid, body, accept_language=accept_language)
    except ApiException as e:
        print("Exception when calling ProgramsApi->start_program: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 
 **body** | [**Program**](Program.md)| description of the program to activate | 
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
**204** | Program has been started successfully |  -  |
**401** | Unauthorized - No or invalid access token |  -  |
**403** | Forbidden - Scope has not been granted |  -  |
**406** | The resource identified by the request is only capable of generating response entities which have content characteristics not acceptable according to the accept headers sent in the request. |  -  |
**408** | API Server failed to produce an answer or has no connection to backend service |  -  |
**409** | An error occured during communication with the home appliance or the home appliance itself answered with an error, e.g. because the issued command was unacceptable in the current state.  |  -  |
**415** | The request&#39;s Content-Type is not supported. |  -  |
**429** | The number of requests for a specific endpoint exceeded the quota of the client.  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_program**
> stop_program(haid, accept_language=accept_language)

Stop the program which is currently executed

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
    api_instance = home_connect_sdk.ProgramsApi(api_client)
    haid = 'haid_example' # str | ID of home appliance
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

    try:
        # Stop the program which is currently executed
        api_instance.stop_program(haid, accept_language=accept_language)
    except ApiException as e:
        print("Exception when calling ProgramsApi->stop_program: %s\n" % e)
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
**204** | OK. Program stopped successfully |  -  |
**401** | Unauthorized - No or invalid access token |  -  |
**403** | Forbidden - Scope has not been granted |  -  |
**406** | The resource identified by the request is only capable of generating response entities which have content characteristics not acceptable according to the accept headers sent in the request. |  -  |
**408** | API Server failed to produce an answer or has no connection to backend service |  -  |
**409** | Request cannot be performed since the OperationState is wrong |  -  |
**429** | The number of requests for a specific endpoint exceeded the quota of the client.  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

