# home_connect_sdk.ImagesApi

All URIs are relative to *https://api.home-connect.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_image**](ImagesApi.md#get_image) | **GET** /homeappliances/{haid}/images/{imagekey} | Get a specific image
[**get_images**](ImagesApi.md#get_images) | **GET** /homeappliances/{haid}/images | Get a list of available images


# **get_image**
> get_image(haid, imagekey)

Get a specific image

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
    api_instance = home_connect_sdk.ImagesApi(api_client)
    haid = 'haid_example' # str | ID of home appliance
imagekey = 'imagekey_example' # str | ID of the image

    try:
        # Get a specific image
        api_instance.get_image(haid, imagekey)
    except ApiException as e:
        print("Exception when calling ImagesApi->get_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 
 **imagekey** | **str**| ID of the image | 

### Return type

void (empty response body)

### Authorization

[homeconnect_auth](../README.md#homeconnect_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpeg

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns image successfully |  -  |
**401** | Unauthorized - No or invalid access token |  -  |
**403** | Forbidden - Scope has not been granted |  -  |
**404** | The requested image was not found |  -  |
**406** | The resource identified by the request is only capable of generating response entities which have content characteristics not acceptable according to the accept headers sent in the request. |  -  |
**408** | API Server failed to produce an answer or has no connection to backend service |  -  |
**429** | The number of requests for a specific endpoint exceeded the quota of the client.  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_images**
> ArrayOfImages get_images(haid, accept_language=accept_language)

Get a list of available images

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
    api_instance = home_connect_sdk.ImagesApi(api_client)
    haid = 'haid_example' # str | ID of home appliance
accept_language = 'accept_language_example' # str | Language for localized assets (optional)

    try:
        # Get a list of available images
        api_response = api_instance.get_images(haid, accept_language=accept_language)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ImagesApi->get_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **haid** | **str**| ID of home appliance | 
 **accept_language** | **str**| Language for localized assets | [optional] 

### Return type

[**ArrayOfImages**](ArrayOfImages.md)

### Authorization

[homeconnect_auth](../README.md#homeconnect_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.bsh.sdk.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Available images |  -  |
**401** | Unauthorized - No or invalid access token |  -  |
**403** | Forbidden - Scope has not been granted |  -  |
**406** | The resource identified by the request is only capable of generating response entities which have content characteristics not acceptable according to the accept headers sent in the request. |  -  |
**408** | API Server failed to produce an answer or has no connection to backend service |  -  |
**429** | The number of requests for a specific endpoint exceeded the quota of the client.  |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

