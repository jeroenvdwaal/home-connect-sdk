# coding: utf-8

"""
    Home Connect API

    This API provides access to home appliances enabled by Home Connect (https://home-connect.com). Through the API programs can be started and stopped, or home appliances configured and monitored. For instance, you can start a cotton program on a washer and get a notification when the cycle is complete.  To get started with this web client, visit https://developer.home-connect.com and register an account. An application with a client ID for this API client will be automatically generated for you.  In order to use this API in your own client, you need an OAuth 2 client implementing the authorization code grant flow (https://developer.home-connect.com/docs/authorization/flow).   More details can be found here: https://www.rfc-editor.org/rfc/rfc6749.txt  Authorization URL: https://api.home-connect.com/security/oauth/authorize  Token URL: https://api.home-connect.com/security/oauth/token   # noqa: E501

    The version of the OpenAPI document: 1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from home_connect_sdk.configuration import Configuration


class HomeApplianceData(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'ha_id': 'str',
        'name': 'str',
        'type': 'str',
        'brand': 'str',
        'vib': 'str',
        'enumber': 'str',
        'connected': 'bool'
    }

    attribute_map = {
        'ha_id': 'haId',
        'name': 'name',
        'type': 'type',
        'brand': 'brand',
        'vib': 'vib',
        'enumber': 'enumber',
        'connected': 'connected'
    }

    def __init__(self, ha_id=None, name=None, type=None, brand=None, vib=None, enumber=None, connected=None, local_vars_configuration=None):  # noqa: E501
        """HomeApplianceData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ha_id = None
        self._name = None
        self._type = None
        self._brand = None
        self._vib = None
        self._enumber = None
        self._connected = None
        self.discriminator = None

        if ha_id is not None:
            self.ha_id = ha_id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if brand is not None:
            self.brand = brand
        if vib is not None:
            self.vib = vib
        if enumber is not None:
            self.enumber = enumber
        if connected is not None:
            self.connected = connected

    @property
    def ha_id(self):
        """Gets the ha_id of this HomeApplianceData.  # noqa: E501

        Unique identifier representing a specific home appliance.  # noqa: E501

        :return: The ha_id of this HomeApplianceData.  # noqa: E501
        :rtype: str
        """
        return self._ha_id

    @ha_id.setter
    def ha_id(self, ha_id):
        """Sets the ha_id of this HomeApplianceData.

        Unique identifier representing a specific home appliance.  # noqa: E501

        :param ha_id: The ha_id of this HomeApplianceData.  # noqa: E501
        :type: str
        """

        self._ha_id = ha_id

    @property
    def name(self):
        """Gets the name of this HomeApplianceData.  # noqa: E501

        User-friendly name of the home appliance (e.g. \"My Oven\")  # noqa: E501

        :return: The name of this HomeApplianceData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HomeApplianceData.

        User-friendly name of the home appliance (e.g. \"My Oven\")  # noqa: E501

        :param name: The name of this HomeApplianceData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this HomeApplianceData.  # noqa: E501

        Type of home appliance, e.g.  \"oven\".  # noqa: E501

        :return: The type of this HomeApplianceData.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HomeApplianceData.

        Type of home appliance, e.g.  \"oven\".  # noqa: E501

        :param type: The type of this HomeApplianceData.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def brand(self):
        """Gets the brand of this HomeApplianceData.  # noqa: E501

        Brand of the home appliance, e.g. \"BOSCH\"  # noqa: E501

        :return: The brand of this HomeApplianceData.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this HomeApplianceData.

        Brand of the home appliance, e.g. \"BOSCH\"  # noqa: E501

        :param brand: The brand of this HomeApplianceData.  # noqa: E501
        :type: str
        """

        self._brand = brand

    @property
    def vib(self):
        """Gets the vib of this HomeApplianceData.  # noqa: E501

        The type code (VIB) of the home appliance.  # noqa: E501

        :return: The vib of this HomeApplianceData.  # noqa: E501
        :rtype: str
        """
        return self._vib

    @vib.setter
    def vib(self, vib):
        """Sets the vib of this HomeApplianceData.

        The type code (VIB) of the home appliance.  # noqa: E501

        :param vib: The vib of this HomeApplianceData.  # noqa: E501
        :type: str
        """

        self._vib = vib

    @property
    def enumber(self):
        """Gets the enumber of this HomeApplianceData.  # noqa: E501

        Combination of VIB and customer index (VIB/KI)  # noqa: E501

        :return: The enumber of this HomeApplianceData.  # noqa: E501
        :rtype: str
        """
        return self._enumber

    @enumber.setter
    def enumber(self, enumber):
        """Sets the enumber of this HomeApplianceData.

        Combination of VIB and customer index (VIB/KI)  # noqa: E501

        :param enumber: The enumber of this HomeApplianceData.  # noqa: E501
        :type: str
        """

        self._enumber = enumber

    @property
    def connected(self):
        """Gets the connected of this HomeApplianceData.  # noqa: E501

        Current connection state of the home appliance. True if the home appliance is online, false otherwise.  # noqa: E501

        :return: The connected of this HomeApplianceData.  # noqa: E501
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """Sets the connected of this HomeApplianceData.

        Current connection state of the home appliance. True if the home appliance is online, false otherwise.  # noqa: E501

        :param connected: The connected of this HomeApplianceData.  # noqa: E501
        :type: bool
        """

        self._connected = connected

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HomeApplianceData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HomeApplianceData):
            return True

        return self.to_dict() != other.to_dict()
