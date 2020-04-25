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


class PutSettingDataConstraints(object):
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
        'min': 'int',
        'max': 'int',
        'stepsize': 'int',
        'allowedvalues': 'list[str]',
        'displayvalues': 'list[str]'
    }

    attribute_map = {
        'min': 'min',
        'max': 'max',
        'stepsize': 'stepsize',
        'allowedvalues': 'allowedvalues',
        'displayvalues': 'displayvalues'
    }

    def __init__(self, min=None, max=None, stepsize=None, allowedvalues=None, displayvalues=None, local_vars_configuration=None):  # noqa: E501
        """PutSettingDataConstraints - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._min = None
        self._max = None
        self._stepsize = None
        self._allowedvalues = None
        self._displayvalues = None
        self.discriminator = None

        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if stepsize is not None:
            self.stepsize = stepsize
        if allowedvalues is not None:
            self.allowedvalues = allowedvalues
        if displayvalues is not None:
            self.displayvalues = displayvalues

    @property
    def min(self):
        """Gets the min of this PutSettingDataConstraints.  # noqa: E501

        minimum value of the option, e.g. 70  # noqa: E501

        :return: The min of this PutSettingDataConstraints.  # noqa: E501
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this PutSettingDataConstraints.

        minimum value of the option, e.g. 70  # noqa: E501

        :param min: The min of this PutSettingDataConstraints.  # noqa: E501
        :type: int
        """

        self._min = min

    @property
    def max(self):
        """Gets the max of this PutSettingDataConstraints.  # noqa: E501

        maximum value of the option, e.g. 270  # noqa: E501

        :return: The max of this PutSettingDataConstraints.  # noqa: E501
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this PutSettingDataConstraints.

        maximum value of the option, e.g. 270  # noqa: E501

        :param max: The max of this PutSettingDataConstraints.  # noqa: E501
        :type: int
        """

        self._max = max

    @property
    def stepsize(self):
        """Gets the stepsize of this PutSettingDataConstraints.  # noqa: E501

        allowed step-size of the option, e.g. 5  # noqa: E501

        :return: The stepsize of this PutSettingDataConstraints.  # noqa: E501
        :rtype: int
        """
        return self._stepsize

    @stepsize.setter
    def stepsize(self, stepsize):
        """Sets the stepsize of this PutSettingDataConstraints.

        allowed step-size of the option, e.g. 5  # noqa: E501

        :param stepsize: The stepsize of this PutSettingDataConstraints.  # noqa: E501
        :type: int
        """

        self._stepsize = stepsize

    @property
    def allowedvalues(self):
        """Gets the allowedvalues of this PutSettingDataConstraints.  # noqa: E501

        list of allowed enumeration values  # noqa: E501

        :return: The allowedvalues of this PutSettingDataConstraints.  # noqa: E501
        :rtype: list[str]
        """
        return self._allowedvalues

    @allowedvalues.setter
    def allowedvalues(self, allowedvalues):
        """Sets the allowedvalues of this PutSettingDataConstraints.

        list of allowed enumeration values  # noqa: E501

        :param allowedvalues: The allowedvalues of this PutSettingDataConstraints.  # noqa: E501
        :type: list[str]
        """

        self._allowedvalues = allowedvalues

    @property
    def displayvalues(self):
        """Gets the displayvalues of this PutSettingDataConstraints.  # noqa: E501

        localized list of allowed enumeration values  # noqa: E501

        :return: The displayvalues of this PutSettingDataConstraints.  # noqa: E501
        :rtype: list[str]
        """
        return self._displayvalues

    @displayvalues.setter
    def displayvalues(self, displayvalues):
        """Sets the displayvalues of this PutSettingDataConstraints.

        localized list of allowed enumeration values  # noqa: E501

        :param displayvalues: The displayvalues of this PutSettingDataConstraints.  # noqa: E501
        :type: list[str]
        """

        self._displayvalues = displayvalues

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
        if not isinstance(other, PutSettingDataConstraints):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PutSettingDataConstraints):
            return True

        return self.to_dict() != other.to_dict()
