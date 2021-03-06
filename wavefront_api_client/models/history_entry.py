# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class HistoryEntry(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        HistoryEntry - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'in_trash': 'bool',
            'version': 'int',
            'update_user': 'str',
            'update_time': 'int',
            'change_description': 'list[str]'
        }

        self.attribute_map = {
            'id': 'id',
            'in_trash': 'inTrash',
            'version': 'version',
            'update_user': 'updateUser',
            'update_time': 'updateTime',
            'change_description': 'changeDescription'
        }

        self._id = None
        self._in_trash = None
        self._version = None
        self._update_user = None
        self._update_time = None
        self._change_description = None

    @property
    def id(self):
        """
        Gets the id of this HistoryEntry.


        :return: The id of this HistoryEntry.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this HistoryEntry.


        :param id: The id of this HistoryEntry.
        :type: str
        """
        self._id = id

    @property
    def in_trash(self):
        """
        Gets the in_trash of this HistoryEntry.


        :return: The in_trash of this HistoryEntry.
        :rtype: bool
        """
        return self._in_trash

    @in_trash.setter
    def in_trash(self, in_trash):
        """
        Sets the in_trash of this HistoryEntry.


        :param in_trash: The in_trash of this HistoryEntry.
        :type: bool
        """
        self._in_trash = in_trash

    @property
    def version(self):
        """
        Gets the version of this HistoryEntry.


        :return: The version of this HistoryEntry.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this HistoryEntry.


        :param version: The version of this HistoryEntry.
        :type: int
        """
        self._version = version

    @property
    def update_user(self):
        """
        Gets the update_user of this HistoryEntry.


        :return: The update_user of this HistoryEntry.
        :rtype: str
        """
        return self._update_user

    @update_user.setter
    def update_user(self, update_user):
        """
        Sets the update_user of this HistoryEntry.


        :param update_user: The update_user of this HistoryEntry.
        :type: str
        """
        self._update_user = update_user

    @property
    def update_time(self):
        """
        Gets the update_time of this HistoryEntry.


        :return: The update_time of this HistoryEntry.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """
        Sets the update_time of this HistoryEntry.


        :param update_time: The update_time of this HistoryEntry.
        :type: int
        """
        self._update_time = update_time

    @property
    def change_description(self):
        """
        Gets the change_description of this HistoryEntry.


        :return: The change_description of this HistoryEntry.
        :rtype: list[str]
        """
        return self._change_description

    @change_description.setter
    def change_description(self, change_description):
        """
        Sets the change_description of this HistoryEntry.


        :param change_description: The change_description of this HistoryEntry.
        :type: list[str]
        """
        self._change_description = change_description

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

