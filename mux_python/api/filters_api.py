# coding: utf-8

"""
    Mux API

    Mux is how developers build online video. This API encompasses both Mux Video and Mux Data functionality to help you build your video-related projects better and faster than ever before.   # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mux_python.api_client import ApiClient
from mux_python.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class FiltersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_filter_values(self, filter_id, **kwargs):  # noqa: E501
        """Lists values for a specific filter  # noqa: E501

        Deprecated: The API has been replaced by the list-dimension-values API call.  Lists the values for a filter along with a total count of related views.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_filter_values(filter_id, async_req=True)
        >>> result = thread.get()

        :param filter_id: ID of the Filter (required)
        :type filter_id: str
        :param limit: Number of items to include in the response
        :type limit: int
        :param page: Offset by this many pages, of the size of `limit`
        :type page: int
        :param filters: Filter key:value pairs. Must be provided as an array query string parameter (e.g. filters[]=operating_system:windows&filters[]=country:US). Possible filter names are the same as returned by the List Filters endpoint. 
        :type filters: list[str]
        :param timeframe: Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=). Accepted formats are...   * array of epoch timestamps e.g. timeframe[]=1498867200&timeframe[]=1498953600   * duration string e.g. timeframe[]=24:hours or timeframe[]=7:days. 
        :type timeframe: list[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ListFilterValuesResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.list_filter_values_with_http_info(filter_id, **kwargs)  # noqa: E501

    def list_filter_values_with_http_info(self, filter_id, **kwargs):  # noqa: E501
        """Lists values for a specific filter  # noqa: E501

        Deprecated: The API has been replaced by the list-dimension-values API call.  Lists the values for a filter along with a total count of related views.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_filter_values_with_http_info(filter_id, async_req=True)
        >>> result = thread.get()

        :param filter_id: ID of the Filter (required)
        :type filter_id: str
        :param limit: Number of items to include in the response
        :type limit: int
        :param page: Offset by this many pages, of the size of `limit`
        :type page: int
        :param filters: Filter key:value pairs. Must be provided as an array query string parameter (e.g. filters[]=operating_system:windows&filters[]=country:US). Possible filter names are the same as returned by the List Filters endpoint. 
        :type filters: list[str]
        :param timeframe: Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]=). Accepted formats are...   * array of epoch timestamps e.g. timeframe[]=1498867200&timeframe[]=1498953600   * duration string e.g. timeframe[]=24:hours or timeframe[]=7:days. 
        :type timeframe: list[str]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ListFilterValuesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'filter_id',
            'limit',
            'page',
            'filters',
            'timeframe'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_filter_values" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'filter_id' is set
        if self.api_client.client_side_validation and ('filter_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['filter_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `filter_id` when calling `list_filter_values`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'filter_id' in local_var_params:
            path_params['FILTER_ID'] = local_var_params['filter_id']  # noqa: E501

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'filters' in local_var_params and local_var_params['filters'] is not None:  # noqa: E501
            query_params.append(('filters[]', local_var_params['filters']))  # noqa: E501
            collection_formats['filters[]'] = 'multi'  # noqa: E501
        if 'timeframe' in local_var_params and local_var_params['timeframe'] is not None:  # noqa: E501
            query_params.append(('timeframe[]', local_var_params['timeframe']))  # noqa: E501
            collection_formats['timeframe[]'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken']  # noqa: E501
        
        response_types_map = {
            200: "ListFilterValuesResponse",
        }

        return self.api_client.call_api(
            '/data/v1/filters/{FILTER_ID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def list_filters(self, **kwargs):  # noqa: E501
        """List Filters  # noqa: E501

        Deprecated: The API has been replaced by the list-dimensions API call.  Lists all the filters broken out into basic and advanced.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_filters(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ListFiltersResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.list_filters_with_http_info(**kwargs)  # noqa: E501

    def list_filters_with_http_info(self, **kwargs):  # noqa: E501
        """List Filters  # noqa: E501

        Deprecated: The API has been replaced by the list-dimensions API call.  Lists all the filters broken out into basic and advanced.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_filters_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ListFiltersResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_filters" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken']  # noqa: E501
        
        response_types_map = {
            200: "ListFiltersResponse",
        }

        return self.api_client.call_api(
            '/data/v1/filters', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
