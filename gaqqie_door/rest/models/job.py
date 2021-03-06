# coding: utf-8

"""
    gaqqie user API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.2.0
    Contact: tknstyk@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Job(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'status': 'str',
        'provider_name': 'str',
        'device_name': 'str',
        'create_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'provider_name': 'provider_name',
        'device_name': 'device_name',
        'create_time': 'create_time',
        'end_time': 'end_time'
    }

    def __init__(self, id=None, name=None, status=None, provider_name=None, device_name=None, create_time=None, end_time=None):  # noqa: E501
        """Job - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._status = None
        self._provider_name = None
        self._device_name = None
        self._create_time = None
        self._end_time = None
        self.discriminator = None
        self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if provider_name is not None:
            self.provider_name = provider_name
        if device_name is not None:
            self.device_name = device_name
        if create_time is not None:
            self.create_time = create_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def id(self):
        """Gets the id of this Job.  # noqa: E501

        a unique id of job  # noqa: E501

        :return: The id of this Job.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Job.

        a unique id of job  # noqa: E501

        :param id: The id of this Job.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Job.  # noqa: E501


        :return: The name of this Job.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Job.


        :param name: The name of this Job.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this Job.  # noqa: E501


        :return: The status of this Job.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Job.


        :param status: The status of this Job.  # noqa: E501
        :type: str
        """
        allowed_values = ["QUEUED", "RUNNING", "SUCCEEDED", "CANCELLED", "FAILED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def provider_name(self):
        """Gets the provider_name of this Job.  # noqa: E501


        :return: The provider_name of this Job.  # noqa: E501
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """Sets the provider_name of this Job.


        :param provider_name: The provider_name of this Job.  # noqa: E501
        :type: str
        """

        self._provider_name = provider_name

    @property
    def device_name(self):
        """Gets the device_name of this Job.  # noqa: E501


        :return: The device_name of this Job.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this Job.


        :param device_name: The device_name of this Job.  # noqa: E501
        :type: str
        """

        self._device_name = device_name

    @property
    def create_time(self):
        """Gets the create_time of this Job.  # noqa: E501


        :return: The create_time of this Job.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Job.


        :param create_time: The create_time of this Job.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def end_time(self):
        """Gets the end_time of this Job.  # noqa: E501


        :return: The end_time of this Job.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this Job.


        :param end_time: The end_time of this Job.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(Job, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Job):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
