# coding: utf-8

"""
    Home Connect API

    This API provides access to home appliances enabled by Home Connect (https://home-connect.com). Through the API programs can be started and stopped, or home appliances configured and monitored. For instance, you can start a cotton program on a washer and get a notification when the cycle is complete.  To get started with this web client, visit https://developer.home-connect.com and register an account. An application with a client ID for this API client will be automatically generated for you.  In order to use this API in your own client, you need an OAuth 2 client implementing the authorization code grant flow (https://developer.home-connect.com/docs/authorization/flow).   More details can be found here: https://www.rfc-editor.org/rfc/rfc6749.txt  Authorization URL: https://api.home-connect.com/security/oauth/authorize  Token URL: https://api.home-connect.com/security/oauth/token   # noqa: E501

    The version of the OpenAPI document: 1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from home_connect_sdk.api_client import ApiClient
from home_connect_sdk.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class SettingsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_setting(self, haid, settingkey, **kwargs):  # noqa: E501
        """Get a specific setting  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_setting(haid, settingkey, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str haid: ID of home appliance (required)
        :param str settingkey: ID of the setting (required)
        :param str accept_language: Language for localized assets
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: GetSetting
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_setting_with_http_info(haid, settingkey, **kwargs)  # noqa: E501

    def get_setting_with_http_info(self, haid, settingkey, **kwargs):  # noqa: E501
        """Get a specific setting  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_setting_with_http_info(haid, settingkey, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str haid: ID of home appliance (required)
        :param str settingkey: ID of the setting (required)
        :param str accept_language: Language for localized assets
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(GetSetting, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'haid',
            'settingkey',
            'accept_language'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_setting" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'haid' is set
        if self.api_client.client_side_validation and ('haid' not in local_var_params or  # noqa: E501
                                                        local_var_params['haid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `haid` when calling `get_setting`")  # noqa: E501
        # verify the required parameter 'settingkey' is set
        if self.api_client.client_side_validation and ('settingkey' not in local_var_params or  # noqa: E501
                                                        local_var_params['settingkey'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `settingkey` when calling `get_setting`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'haid' in local_var_params:
            path_params['haid'] = local_var_params['haid']  # noqa: E501
        if 'settingkey' in local_var_params:
            path_params['settingkey'] = local_var_params['settingkey']  # noqa: E501

        query_params = []

        header_params = {}
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.bsh.sdk.v1+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['homeconnect_auth']  # noqa: E501

        return self.api_client.call_api(
            '/homeappliances/{haid}/settings/{settingkey}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetSetting',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_settings(self, haid, **kwargs):  # noqa: E501
        """Get a list of available settings  # noqa: E501

        Get a list of available setting of the home appliance.  Further documentation can be found here: * [Power state](https://developer.home-connect.com/docs/settings/power_state) * [Fridge temperature](https://developer.home-connect.com/docs/api/settings/fridgetemperature) * [Fridge super mode](https://developer.home-connect.com/docs/api/settings/fridgesupermode) * [Freezer temperature](https://developer.home-connect.com/docs/api/settings/freezertemperature) * [Freezer super mode](https://developer.home-connect.com/docs/api/settings/freezersupermode)   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_settings(haid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str haid: ID of home appliance (required)
        :param str accept_language: Language for localized assets
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ArrayOfSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_settings_with_http_info(haid, **kwargs)  # noqa: E501

    def get_settings_with_http_info(self, haid, **kwargs):  # noqa: E501
        """Get a list of available settings  # noqa: E501

        Get a list of available setting of the home appliance.  Further documentation can be found here: * [Power state](https://developer.home-connect.com/docs/settings/power_state) * [Fridge temperature](https://developer.home-connect.com/docs/api/settings/fridgetemperature) * [Fridge super mode](https://developer.home-connect.com/docs/api/settings/fridgesupermode) * [Freezer temperature](https://developer.home-connect.com/docs/api/settings/freezertemperature) * [Freezer super mode](https://developer.home-connect.com/docs/api/settings/freezersupermode)   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_settings_with_http_info(haid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str haid: ID of home appliance (required)
        :param str accept_language: Language for localized assets
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ArrayOfSettings, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'haid',
            'accept_language'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_settings" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'haid' is set
        if self.api_client.client_side_validation and ('haid' not in local_var_params or  # noqa: E501
                                                        local_var_params['haid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `haid` when calling `get_settings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'haid' in local_var_params:
            path_params['haid'] = local_var_params['haid']  # noqa: E501

        query_params = []

        header_params = {}
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.bsh.sdk.v1+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['homeconnect_auth']  # noqa: E501

        return self.api_client.call_api(
            '/homeappliances/{haid}/settings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ArrayOfSettings',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def set_setting(self, haid, settingkey, body, **kwargs):  # noqa: E501
        """Set a specific setting  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_setting(haid, settingkey, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str haid: ID of home appliance (required)
        :param str settingkey: ID of the setting (required)
        :param PutSetting body: description of the setting (required)
        :param str accept_language: Language for localized assets
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.set_setting_with_http_info(haid, settingkey, body, **kwargs)  # noqa: E501

    def set_setting_with_http_info(self, haid, settingkey, body, **kwargs):  # noqa: E501
        """Set a specific setting  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_setting_with_http_info(haid, settingkey, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str haid: ID of home appliance (required)
        :param str settingkey: ID of the setting (required)
        :param PutSetting body: description of the setting (required)
        :param str accept_language: Language for localized assets
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'haid',
            'settingkey',
            'body',
            'accept_language'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_setting" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'haid' is set
        if self.api_client.client_side_validation and ('haid' not in local_var_params or  # noqa: E501
                                                        local_var_params['haid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `haid` when calling `set_setting`")  # noqa: E501
        # verify the required parameter 'settingkey' is set
        if self.api_client.client_side_validation and ('settingkey' not in local_var_params or  # noqa: E501
                                                        local_var_params['settingkey'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `settingkey` when calling `set_setting`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in local_var_params or  # noqa: E501
                                                        local_var_params['body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `body` when calling `set_setting`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'haid' in local_var_params:
            path_params['haid'] = local_var_params['haid']  # noqa: E501
        if 'settingkey' in local_var_params:
            path_params['settingkey'] = local_var_params['settingkey']  # noqa: E501

        query_params = []

        header_params = {}
        if 'accept_language' in local_var_params:
            header_params['Accept-Language'] = local_var_params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.bsh.sdk.v1+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/vnd.bsh.sdk.v1+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['homeconnect_auth']  # noqa: E501

        return self.api_client.call_api(
            '/homeappliances/{haid}/settings/{settingkey}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
