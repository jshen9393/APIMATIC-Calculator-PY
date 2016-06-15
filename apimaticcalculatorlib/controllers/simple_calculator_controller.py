# -*- coding: utf-8 -*-

"""
    apimaticcalculatorlib.controllers.simple_calculator_controller

    This file was automatically generated by APIMATIC BETA v2.0 on 06/15/2016
"""
from apimaticcalculatorlib.api_helper import APIHelper
from apimaticcalculatorlib.api_exception import APIException
from apimaticcalculatorlib.configuration import Configuration
from apimaticcalculatorlib.http.http_request import HttpRequest
from apimaticcalculatorlib.http.http_response import HttpResponse
from apimaticcalculatorlib.http.requests_client import RequestsClient
from apimaticcalculatorlib.controllers.base_controller import BaseController



class SimpleCalculatorController(BaseController):

    """A Controller to access Endpoints in the apimaticcalculatorlib API."""

    def __init__(self, http_client = None, http_call_back = None):
        """Constructor which allows a different HTTP client for this controller."""
        BaseController.__init__(self, http_client, http_call_back)

    def get_calculate(self,
                      options=dict()):
        """Does a GET request to /{operation}.

        Calculates the expression using the specified operation.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    operation -- OperationTypeEnum -- The operator to apply on
                        the variables
                    x -- float -- The LHS value
                    y -- float -- The RHS value

        Returns:
            float: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # The base uri for api requests
        _query_builder = Configuration.BASE_URI
 
        # Prepare query string for API call
        _query_builder += "/{operation}"

        # Process optional template parameters
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            "operation": options.get('operation', None)
        })

        # Process optional query parameters
        _query_parameters = {
            "x": options.get('x', None),
            "y": options.get('y', None)
        }
        
        # Validate and preprocess url
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            "user-agent": "APIMATIC 2.0"
        }

        # Prepare the API call.
        _http_request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters)

        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_before_request(_http_request)

        # Invoke the API call  to fetch the response.
        _response = self.http_client.execute_as_string(_http_request)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back != None:
            self.http_call_back.on_after_response(_response)

        # Global error handling using HTTP status codes.
        self.validate_response(_response)    

        # Return appropriate type
        return float(_response.raw_body)


