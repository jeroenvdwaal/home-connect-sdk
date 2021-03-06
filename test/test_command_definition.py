# coding: utf-8

"""
    Home Connect API

    This API provides access to home appliances enabled by Home Connect (https://home-connect.com). Through the API programs can be started and stopped, or home appliances configured and monitored. For instance, you can start a cotton program on a washer and get a notification when the cycle is complete.  To get started with this web client, visit https://developer.home-connect.com and register an account. An application with a client ID for this API client will be automatically generated for you.  In order to use this API in your own client, you need an OAuth 2 client implementing the authorization code grant flow (https://developer.home-connect.com/docs/authorization/flow).   More details can be found here: https://www.rfc-editor.org/rfc/rfc6749.txt  Authorization URL: https://api.home-connect.com/security/oauth/authorize  Token URL: https://api.home-connect.com/security/oauth/token   # noqa: E501

    The version of the OpenAPI document: 1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import home_connect_sdk
from home_connect_sdk.models.command_definition import CommandDefinition  # noqa: E501
from home_connect_sdk.rest import ApiException

class TestCommandDefinition(unittest.TestCase):
    """CommandDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CommandDefinition
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = home_connect_sdk.models.command_definition.CommandDefinition()  # noqa: E501
        if include_optional :
            return CommandDefinition(
                data = [
                    home_connect_sdk.models.command_definition_data.CommandDefinition_data(
                        key = '0', 
                        description = home_connect_sdk.models.description.description(), )
                    ]
            )
        else :
            return CommandDefinition(
                data = [
                    home_connect_sdk.models.command_definition_data.CommandDefinition_data(
                        key = '0', 
                        description = home_connect_sdk.models.description.description(), )
                    ],
        )

    def testCommandDefinition(self):
        """Test CommandDefinition"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
