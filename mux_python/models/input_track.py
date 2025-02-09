# coding: utf-8

"""
    Mux API

    Mux is how developers build online video. This API encompasses both Mux Video and Mux Data functionality to help you build your video-related projects better and faster than ever before.   # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from mux_python.configuration import Configuration


class InputTrack(object):
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
        'type': 'str',
        'duration': 'float',
        'encoding': 'str',
        'width': 'int',
        'height': 'int',
        'frame_rate': 'float',
        'sample_rate': 'int',
        'sample_size': 'int',
        'channels': 'int'
    }

    attribute_map = {
        'type': 'type',
        'duration': 'duration',
        'encoding': 'encoding',
        'width': 'width',
        'height': 'height',
        'frame_rate': 'frame_rate',
        'sample_rate': 'sample_rate',
        'sample_size': 'sample_size',
        'channels': 'channels'
    }

    def __init__(self, type=None, duration=None, encoding=None, width=None, height=None, frame_rate=None, sample_rate=None, sample_size=None, channels=None, local_vars_configuration=None):  # noqa: E501
        """InputTrack - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._duration = None
        self._encoding = None
        self._width = None
        self._height = None
        self._frame_rate = None
        self._sample_rate = None
        self._sample_size = None
        self._channels = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if duration is not None:
            self.duration = duration
        if encoding is not None:
            self.encoding = encoding
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if frame_rate is not None:
            self.frame_rate = frame_rate
        if sample_rate is not None:
            self.sample_rate = sample_rate
        if sample_size is not None:
            self.sample_size = sample_size
        if channels is not None:
            self.channels = channels

    @property
    def type(self):
        """Gets the type of this InputTrack.  # noqa: E501


        :return: The type of this InputTrack.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InputTrack.


        :param type: The type of this InputTrack.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def duration(self):
        """Gets the duration of this InputTrack.  # noqa: E501


        :return: The duration of this InputTrack.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this InputTrack.


        :param duration: The duration of this InputTrack.  # noqa: E501
        :type duration: float
        """

        self._duration = duration

    @property
    def encoding(self):
        """Gets the encoding of this InputTrack.  # noqa: E501


        :return: The encoding of this InputTrack.  # noqa: E501
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this InputTrack.


        :param encoding: The encoding of this InputTrack.  # noqa: E501
        :type encoding: str
        """

        self._encoding = encoding

    @property
    def width(self):
        """Gets the width of this InputTrack.  # noqa: E501


        :return: The width of this InputTrack.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this InputTrack.


        :param width: The width of this InputTrack.  # noqa: E501
        :type width: int
        """

        self._width = width

    @property
    def height(self):
        """Gets the height of this InputTrack.  # noqa: E501


        :return: The height of this InputTrack.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this InputTrack.


        :param height: The height of this InputTrack.  # noqa: E501
        :type height: int
        """

        self._height = height

    @property
    def frame_rate(self):
        """Gets the frame_rate of this InputTrack.  # noqa: E501


        :return: The frame_rate of this InputTrack.  # noqa: E501
        :rtype: float
        """
        return self._frame_rate

    @frame_rate.setter
    def frame_rate(self, frame_rate):
        """Sets the frame_rate of this InputTrack.


        :param frame_rate: The frame_rate of this InputTrack.  # noqa: E501
        :type frame_rate: float
        """

        self._frame_rate = frame_rate

    @property
    def sample_rate(self):
        """Gets the sample_rate of this InputTrack.  # noqa: E501


        :return: The sample_rate of this InputTrack.  # noqa: E501
        :rtype: int
        """
        return self._sample_rate

    @sample_rate.setter
    def sample_rate(self, sample_rate):
        """Sets the sample_rate of this InputTrack.


        :param sample_rate: The sample_rate of this InputTrack.  # noqa: E501
        :type sample_rate: int
        """

        self._sample_rate = sample_rate

    @property
    def sample_size(self):
        """Gets the sample_size of this InputTrack.  # noqa: E501


        :return: The sample_size of this InputTrack.  # noqa: E501
        :rtype: int
        """
        return self._sample_size

    @sample_size.setter
    def sample_size(self, sample_size):
        """Sets the sample_size of this InputTrack.


        :param sample_size: The sample_size of this InputTrack.  # noqa: E501
        :type sample_size: int
        """

        self._sample_size = sample_size

    @property
    def channels(self):
        """Gets the channels of this InputTrack.  # noqa: E501


        :return: The channels of this InputTrack.  # noqa: E501
        :rtype: int
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this InputTrack.


        :param channels: The channels of this InputTrack.  # noqa: E501
        :type channels: int
        """

        self._channels = channels

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InputTrack):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputTrack):
            return True

        return self.to_dict() != other.to_dict()
