# coding: utf-8

"""
    gaqqie user API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: tknsryk@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Device(object):
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
        'name': 'str',
        'provider_name': 'str',
        'status': 'str',
        'num_qubits': 'int',
        'max_shots': 'int',
        'queued_jobs': 'int'
    }

    attribute_map = {
        'name': 'name',
        'provider_name': 'provider_name',
        'status': 'status',
        'num_qubits': 'num_qubits',
        'max_shots': 'max_shots',
        'queued_jobs': 'queued_jobs'
    }

    def __init__(self, name=None, provider_name=None, status=None, num_qubits=None, max_shots=None, queued_jobs=None):  # noqa: E501
        """Device - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._provider_name = None
        self._status = None
        self._num_qubits = None
        self._max_shots = None
        self._queued_jobs = None
        self.discriminator = None
        self.name = name
        if provider_name is not None:
            self.provider_name = provider_name
        if status is not None:
            self.status = status
        if num_qubits is not None:
            self.num_qubits = num_qubits
        if max_shots is not None:
            self.max_shots = max_shots
        if queued_jobs is not None:
            self.queued_jobs = queued_jobs

    @property
    def name(self):
        """Gets the name of this Device.  # noqa: E501

        a unique name of device  # noqa: E501

        :return: The name of this Device.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Device.

        a unique name of device  # noqa: E501

        :param name: The name of this Device.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def provider_name(self):
        """Gets the provider_name of this Device.  # noqa: E501


        :return: The provider_name of this Device.  # noqa: E501
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """Sets the provider_name of this Device.


        :param provider_name: The provider_name of this Device.  # noqa: E501
        :type: str
        """

        self._provider_name = provider_name

    @property
    def status(self):
        """Gets the status of this Device.  # noqa: E501


        :return: The status of this Device.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Device.


        :param status: The status of this Device.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "SUBMITTABLE", "UNSUBMITTABLE"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def num_qubits(self):
        """Gets the num_qubits of this Device.  # noqa: E501


        :return: The num_qubits of this Device.  # noqa: E501
        :rtype: int
        """
        return self._num_qubits

    @num_qubits.setter
    def num_qubits(self, num_qubits):
        """Sets the num_qubits of this Device.


        :param num_qubits: The num_qubits of this Device.  # noqa: E501
        :type: int
        """

        self._num_qubits = num_qubits

    @property
    def max_shots(self):
        """Gets the max_shots of this Device.  # noqa: E501


        :return: The max_shots of this Device.  # noqa: E501
        :rtype: int
        """
        return self._max_shots

    @max_shots.setter
    def max_shots(self, max_shots):
        """Sets the max_shots of this Device.


        :param max_shots: The max_shots of this Device.  # noqa: E501
        :type: int
        """

        self._max_shots = max_shots

    @property
    def queued_jobs(self):
        """Gets the queued_jobs of this Device.  # noqa: E501


        :return: The queued_jobs of this Device.  # noqa: E501
        :rtype: int
        """
        return self._queued_jobs

    @queued_jobs.setter
    def queued_jobs(self, queued_jobs):
        """Sets the queued_jobs of this Device.


        :param queued_jobs: The queued_jobs of this Device.  # noqa: E501
        :type: int
        """

        self._queued_jobs = queued_jobs

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
        if issubclass(Device, dict):
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
        if not isinstance(other, Device):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
