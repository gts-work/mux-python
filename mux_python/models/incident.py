# coding: utf-8

"""
Mux Python - Copyright 2019 Mux Inc.

NOTE: This class is auto generated. Do not edit the class manually.
"""


import pprint
import re  # noqa: F401
import six

class Incident(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'threshold': 'float',
        'status': 'str',
        'started_at': 'str',
        'severity': 'str',
        'sample_size_unit': 'str',
        'sample_size': 'float',
        'resolved_at': 'str',
        'notifications': 'list[IncidentNotification]',
        'notification_rules': 'list[IncidentNotificationRule]',
        'measurement': 'str',
        'measured_value_on_close': 'float',
        'measured_value': 'float',
        'incident_key': 'str',
        'impact': 'str',
        'id': 'str',
        'error_description': 'str',
        'description': 'str',
        'breakdowns': 'list[IncidentBreakdown]',
        'affected_views_per_hour_on_open': 'float',
        'affected_views_per_hour': 'float',
        'affected_views': 'float'
    }

    attribute_map = {
        'threshold': 'threshold',
        'status': 'status',
        'started_at': 'started_at',
        'severity': 'severity',
        'sample_size_unit': 'sample_size_unit',
        'sample_size': 'sample_size',
        'resolved_at': 'resolved_at',
        'notifications': 'notifications',
        'notification_rules': 'notification_rules',
        'measurement': 'measurement',
        'measured_value_on_close': 'measured_value_on_close',
        'measured_value': 'measured_value',
        'incident_key': 'incident_key',
        'impact': 'impact',
        'id': 'id',
        'error_description': 'error_description',
        'description': 'description',
        'breakdowns': 'breakdowns',
        'affected_views_per_hour_on_open': 'affected_views_per_hour_on_open',
        'affected_views_per_hour': 'affected_views_per_hour',
        'affected_views': 'affected_views'
    }

    def __init__(self, threshold=None, status=None, started_at=None, severity=None, sample_size_unit=None, sample_size=None, resolved_at=None, notifications=None, notification_rules=None, measurement=None, measured_value_on_close=None, measured_value=None, incident_key=None, impact=None, id=None, error_description=None, description=None, breakdowns=None, affected_views_per_hour_on_open=None, affected_views_per_hour=None, affected_views=None):  # noqa: E501
        """Incident - a model defined in OpenAPI"""  # noqa: E501

        self._threshold = None
        self._status = None
        self._started_at = None
        self._severity = None
        self._sample_size_unit = None
        self._sample_size = None
        self._resolved_at = None
        self._notifications = None
        self._notification_rules = None
        self._measurement = None
        self._measured_value_on_close = None
        self._measured_value = None
        self._incident_key = None
        self._impact = None
        self._id = None
        self._error_description = None
        self._description = None
        self._breakdowns = None
        self._affected_views_per_hour_on_open = None
        self._affected_views_per_hour = None
        self._affected_views = None
        self.discriminator = None

        if threshold is not None:
            self.threshold = threshold
        if status is not None:
            self.status = status
        if started_at is not None:
            self.started_at = started_at
        if severity is not None:
            self.severity = severity
        if sample_size_unit is not None:
            self.sample_size_unit = sample_size_unit
        if sample_size is not None:
            self.sample_size = sample_size
        if resolved_at is not None:
            self.resolved_at = resolved_at
        if notifications is not None:
            self.notifications = notifications
        if notification_rules is not None:
            self.notification_rules = notification_rules
        if measurement is not None:
            self.measurement = measurement
        if measured_value_on_close is not None:
            self.measured_value_on_close = measured_value_on_close
        if measured_value is not None:
            self.measured_value = measured_value
        if incident_key is not None:
            self.incident_key = incident_key
        if impact is not None:
            self.impact = impact
        if id is not None:
            self.id = id
        if error_description is not None:
            self.error_description = error_description
        if description is not None:
            self.description = description
        if breakdowns is not None:
            self.breakdowns = breakdowns
        if affected_views_per_hour_on_open is not None:
            self.affected_views_per_hour_on_open = affected_views_per_hour_on_open
        if affected_views_per_hour is not None:
            self.affected_views_per_hour = affected_views_per_hour
        if affected_views is not None:
            self.affected_views = affected_views

    @property
    def threshold(self):
        """Gets the threshold of this Incident.  # noqa: E501


        :return: The threshold of this Incident.  # noqa: E501
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this Incident.


        :param threshold: The threshold of this Incident.  # noqa: E501
        :type: float
        """

        self._threshold = threshold

    @property
    def status(self):
        """Gets the status of this Incident.  # noqa: E501


        :return: The status of this Incident.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Incident.


        :param status: The status of this Incident.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def started_at(self):
        """Gets the started_at of this Incident.  # noqa: E501


        :return: The started_at of this Incident.  # noqa: E501
        :rtype: str
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this Incident.


        :param started_at: The started_at of this Incident.  # noqa: E501
        :type: str
        """

        self._started_at = started_at

    @property
    def severity(self):
        """Gets the severity of this Incident.  # noqa: E501


        :return: The severity of this Incident.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this Incident.


        :param severity: The severity of this Incident.  # noqa: E501
        :type: str
        """

        self._severity = severity

    @property
    def sample_size_unit(self):
        """Gets the sample_size_unit of this Incident.  # noqa: E501


        :return: The sample_size_unit of this Incident.  # noqa: E501
        :rtype: str
        """
        return self._sample_size_unit

    @sample_size_unit.setter
    def sample_size_unit(self, sample_size_unit):
        """Sets the sample_size_unit of this Incident.


        :param sample_size_unit: The sample_size_unit of this Incident.  # noqa: E501
        :type: str
        """

        self._sample_size_unit = sample_size_unit

    @property
    def sample_size(self):
        """Gets the sample_size of this Incident.  # noqa: E501


        :return: The sample_size of this Incident.  # noqa: E501
        :rtype: float
        """
        return self._sample_size

    @sample_size.setter
    def sample_size(self, sample_size):
        """Sets the sample_size of this Incident.


        :param sample_size: The sample_size of this Incident.  # noqa: E501
        :type: float
        """

        self._sample_size = sample_size

    @property
    def resolved_at(self):
        """Gets the resolved_at of this Incident.  # noqa: E501


        :return: The resolved_at of this Incident.  # noqa: E501
        :rtype: str
        """
        return self._resolved_at

    @resolved_at.setter
    def resolved_at(self, resolved_at):
        """Sets the resolved_at of this Incident.


        :param resolved_at: The resolved_at of this Incident.  # noqa: E501
        :type: str
        """

        self._resolved_at = resolved_at

    @property
    def notifications(self):
        """Gets the notifications of this Incident.  # noqa: E501


        :return: The notifications of this Incident.  # noqa: E501
        :rtype: list[IncidentNotification]
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """Sets the notifications of this Incident.


        :param notifications: The notifications of this Incident.  # noqa: E501
        :type: list[IncidentNotification]
        """

        self._notifications = notifications

    @property
    def notification_rules(self):
        """Gets the notification_rules of this Incident.  # noqa: E501


        :return: The notification_rules of this Incident.  # noqa: E501
        :rtype: list[IncidentNotificationRule]
        """
        return self._notification_rules

    @notification_rules.setter
    def notification_rules(self, notification_rules):
        """Sets the notification_rules of this Incident.


        :param notification_rules: The notification_rules of this Incident.  # noqa: E501
        :type: list[IncidentNotificationRule]
        """

        self._notification_rules = notification_rules

    @property
    def measurement(self):
        """Gets the measurement of this Incident.  # noqa: E501


        :return: The measurement of this Incident.  # noqa: E501
        :rtype: str
        """
        return self._measurement

    @measurement.setter
    def measurement(self, measurement):
        """Sets the measurement of this Incident.


        :param measurement: The measurement of this Incident.  # noqa: E501
        :type: str
        """

        self._measurement = measurement

    @property
    def measured_value_on_close(self):
        """Gets the measured_value_on_close of this Incident.  # noqa: E501


        :return: The measured_value_on_close of this Incident.  # noqa: E501
        :rtype: float
        """
        return self._measured_value_on_close

    @measured_value_on_close.setter
    def measured_value_on_close(self, measured_value_on_close):
        """Sets the measured_value_on_close of this Incident.


        :param measured_value_on_close: The measured_value_on_close of this Incident.  # noqa: E501
        :type: float
        """

        self._measured_value_on_close = measured_value_on_close

    @property
    def measured_value(self):
        """Gets the measured_value of this Incident.  # noqa: E501


        :return: The measured_value of this Incident.  # noqa: E501
        :rtype: float
        """
        return self._measured_value

    @measured_value.setter
    def measured_value(self, measured_value):
        """Sets the measured_value of this Incident.


        :param measured_value: The measured_value of this Incident.  # noqa: E501
        :type: float
        """

        self._measured_value = measured_value

    @property
    def incident_key(self):
        """Gets the incident_key of this Incident.  # noqa: E501


        :return: The incident_key of this Incident.  # noqa: E501
        :rtype: str
        """
        return self._incident_key

    @incident_key.setter
    def incident_key(self, incident_key):
        """Sets the incident_key of this Incident.


        :param incident_key: The incident_key of this Incident.  # noqa: E501
        :type: str
        """

        self._incident_key = incident_key

    @property
    def impact(self):
        """Gets the impact of this Incident.  # noqa: E501


        :return: The impact of this Incident.  # noqa: E501
        :rtype: str
        """
        return self._impact

    @impact.setter
    def impact(self, impact):
        """Sets the impact of this Incident.


        :param impact: The impact of this Incident.  # noqa: E501
        :type: str
        """

        self._impact = impact

    @property
    def id(self):
        """Gets the id of this Incident.  # noqa: E501


        :return: The id of this Incident.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Incident.


        :param id: The id of this Incident.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def error_description(self):
        """Gets the error_description of this Incident.  # noqa: E501


        :return: The error_description of this Incident.  # noqa: E501
        :rtype: str
        """
        return self._error_description

    @error_description.setter
    def error_description(self, error_description):
        """Sets the error_description of this Incident.


        :param error_description: The error_description of this Incident.  # noqa: E501
        :type: str
        """

        self._error_description = error_description

    @property
    def description(self):
        """Gets the description of this Incident.  # noqa: E501


        :return: The description of this Incident.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Incident.


        :param description: The description of this Incident.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def breakdowns(self):
        """Gets the breakdowns of this Incident.  # noqa: E501


        :return: The breakdowns of this Incident.  # noqa: E501
        :rtype: list[IncidentBreakdown]
        """
        return self._breakdowns

    @breakdowns.setter
    def breakdowns(self, breakdowns):
        """Sets the breakdowns of this Incident.


        :param breakdowns: The breakdowns of this Incident.  # noqa: E501
        :type: list[IncidentBreakdown]
        """

        self._breakdowns = breakdowns

    @property
    def affected_views_per_hour_on_open(self):
        """Gets the affected_views_per_hour_on_open of this Incident.  # noqa: E501


        :return: The affected_views_per_hour_on_open of this Incident.  # noqa: E501
        :rtype: float
        """
        return self._affected_views_per_hour_on_open

    @affected_views_per_hour_on_open.setter
    def affected_views_per_hour_on_open(self, affected_views_per_hour_on_open):
        """Sets the affected_views_per_hour_on_open of this Incident.


        :param affected_views_per_hour_on_open: The affected_views_per_hour_on_open of this Incident.  # noqa: E501
        :type: float
        """

        self._affected_views_per_hour_on_open = affected_views_per_hour_on_open

    @property
    def affected_views_per_hour(self):
        """Gets the affected_views_per_hour of this Incident.  # noqa: E501


        :return: The affected_views_per_hour of this Incident.  # noqa: E501
        :rtype: float
        """
        return self._affected_views_per_hour

    @affected_views_per_hour.setter
    def affected_views_per_hour(self, affected_views_per_hour):
        """Sets the affected_views_per_hour of this Incident.


        :param affected_views_per_hour: The affected_views_per_hour of this Incident.  # noqa: E501
        :type: float
        """

        self._affected_views_per_hour = affected_views_per_hour

    @property
    def affected_views(self):
        """Gets the affected_views of this Incident.  # noqa: E501


        :return: The affected_views of this Incident.  # noqa: E501
        :rtype: float
        """
        return self._affected_views

    @affected_views.setter
    def affected_views(self, affected_views):
        """Sets the affected_views of this Incident.


        :param affected_views: The affected_views of this Incident.  # noqa: E501
        :type: float
        """

        self._affected_views = affected_views

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
        if not isinstance(other, Incident):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
