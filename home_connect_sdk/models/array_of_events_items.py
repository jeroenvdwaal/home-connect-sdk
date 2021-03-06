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


class ArrayOfEventsItems(object):
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
        'key': 'str',
        'name': 'str',
        'uri': 'str',
        'timestamp': 'int',
        'level': 'str',
        'handling': 'str',
        'unit': 'str'
    }

    attribute_map = {
        'key': 'key',
        'name': 'name',
        'uri': 'uri',
        'timestamp': 'timestamp',
        'level': 'level',
        'handling': 'handling',
        'unit': 'unit'
    }

    def __init__(self, key=None, name=None, uri=None, timestamp=None, level=None, handling=None, unit=None, local_vars_configuration=None):  # noqa: E501
        """ArrayOfEventsItems - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._key = None
        self._name = None
        self._uri = None
        self._timestamp = None
        self._level = None
        self._handling = None
        self._unit = None
        self.discriminator = None

        self.key = key
        if name is not None:
            self.name = name
        if uri is not None:
            self.uri = uri
        self.timestamp = timestamp
        self.level = level
        self.handling = handling
        if unit is not None:
            self.unit = unit

    @property
    def key(self):
        """Gets the key of this ArrayOfEventsItems.  # noqa: E501

        The type of the event  # noqa: E501

        :return: The key of this ArrayOfEventsItems.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ArrayOfEventsItems.

        The type of the event  # noqa: E501

        :param key: The key of this ArrayOfEventsItems.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and key is None:  # noqa: E501
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def name(self):
        """Gets the name of this ArrayOfEventsItems.  # noqa: E501

        User-friendly name of the feature key  # noqa: E501

        :return: The name of this ArrayOfEventsItems.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ArrayOfEventsItems.

        User-friendly name of the feature key  # noqa: E501

        :param name: The name of this ArrayOfEventsItems.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def uri(self):
        """Gets the uri of this ArrayOfEventsItems.  # noqa: E501

        URI of the resource that changed  # noqa: E501

        :return: The uri of this ArrayOfEventsItems.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this ArrayOfEventsItems.

        URI of the resource that changed  # noqa: E501

        :param uri: The uri of this ArrayOfEventsItems.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def timestamp(self):
        """Gets the timestamp of this ArrayOfEventsItems.  # noqa: E501

        Creation time of event as unix timestamp  # noqa: E501

        :return: The timestamp of this ArrayOfEventsItems.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ArrayOfEventsItems.

        Creation time of event as unix timestamp  # noqa: E501

        :param timestamp: The timestamp of this ArrayOfEventsItems.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def level(self):
        """Gets the level of this ArrayOfEventsItems.  # noqa: E501

        Level of the event, possible values: critical, alert, warning, hint, info   # noqa: E501

        :return: The level of this ArrayOfEventsItems.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this ArrayOfEventsItems.

        Level of the event, possible values: critical, alert, warning, hint, info   # noqa: E501

        :param level: The level of this ArrayOfEventsItems.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and level is None:  # noqa: E501
            raise ValueError("Invalid value for `level`, must not be `None`")  # noqa: E501

        self._level = level

    @property
    def handling(self):
        """Gets the handling of this ArrayOfEventsItems.  # noqa: E501

        Expected activity, possible values: none, acknowledge, decision   # noqa: E501

        :return: The handling of this ArrayOfEventsItems.  # noqa: E501
        :rtype: str
        """
        return self._handling

    @handling.setter
    def handling(self, handling):
        """Sets the handling of this ArrayOfEventsItems.

        Expected activity, possible values: none, acknowledge, decision   # noqa: E501

        :param handling: The handling of this ArrayOfEventsItems.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and handling is None:  # noqa: E501
            raise ValueError("Invalid value for `handling`, must not be `None`")  # noqa: E501

        self._handling = handling

    @property
    def unit(self):
        """Gets the unit of this ArrayOfEventsItems.  # noqa: E501

        Unit of the value  # noqa: E501

        :return: The unit of this ArrayOfEventsItems.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ArrayOfEventsItems.

        Unit of the value  # noqa: E501

        :param unit: The unit of this ArrayOfEventsItems.  # noqa: E501
        :type: str
        """

        self._unit = unit

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
        if not isinstance(other, ArrayOfEventsItems):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ArrayOfEventsItems):
            return True

        return self.to_dict() != other.to_dict()
