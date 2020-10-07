# coding: utf-8

"""
    Strava API v3

    The [Swagger Playground](https://developers.strava.com/playground) is the easiest way to familiarize yourself with the Strava API by submitting HTTP requests and observing the responses before you write any client code. It will show what a response will look like with different endpoints depending on the authorization scope you receive from your athletes. To use the Playground, go to https://www.strava.com/settings/api and change your “Authorization Callback Domain” to developers.strava.com. Please note, we only support Swagger 2.0. There is a known issue where you can only select one scope at a time. For more information, please check the section “client code” at https://developers.strava.com/docs.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SummaryActivity(object):
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
        'external_id': 'str',
        'upload_id': 'int',
        'athlete': 'MetaAthlete',
        'name': 'str',
        'distance': 'float',
        'moving_time': 'int',
        'elapsed_time': 'int',
        'total_elevation_gain': 'float',
        'elev_high': 'float',
        'elev_low': 'float',
        'type': 'ActivityType',
        'start_date': 'datetime',
        'start_date_local': 'datetime',
        'timezone': 'str',
        'start_latlng': 'LatLng',
        'end_latlng': 'LatLng',
        'achievement_count': 'int',
        'kudos_count': 'int',
        'comment_count': 'int',
        'athlete_count': 'int',
        'photo_count': 'int',
        'total_photo_count': 'int',
        'map': 'PolylineMap',
        'trainer': 'bool',
        'commute': 'bool',
        'manual': 'bool',
        'private': 'bool',
        'flagged': 'bool',
        'workout_type': 'int',
        'upload_id_str': 'str',
        'average_speed': 'float',
        'max_speed': 'float',
        'has_kudoed': 'bool',
        'gear_id': 'str',
        'kilojoules': 'float',
        'average_watts': 'float',
        'device_watts': 'bool',
        'max_watts': 'int',
        'weighted_average_watts': 'int'
    }

    attribute_map = {
        'external_id': 'external_id',
        'upload_id': 'upload_id',
        'athlete': 'athlete',
        'name': 'name',
        'distance': 'distance',
        'moving_time': 'moving_time',
        'elapsed_time': 'elapsed_time',
        'total_elevation_gain': 'total_elevation_gain',
        'elev_high': 'elev_high',
        'elev_low': 'elev_low',
        'type': 'type',
        'start_date': 'start_date',
        'start_date_local': 'start_date_local',
        'timezone': 'timezone',
        'start_latlng': 'start_latlng',
        'end_latlng': 'end_latlng',
        'achievement_count': 'achievement_count',
        'kudos_count': 'kudos_count',
        'comment_count': 'comment_count',
        'athlete_count': 'athlete_count',
        'photo_count': 'photo_count',
        'total_photo_count': 'total_photo_count',
        'map': 'map',
        'trainer': 'trainer',
        'commute': 'commute',
        'manual': 'manual',
        'private': 'private',
        'flagged': 'flagged',
        'workout_type': 'workout_type',
        'upload_id_str': 'upload_id_str',
        'average_speed': 'average_speed',
        'max_speed': 'max_speed',
        'has_kudoed': 'has_kudoed',
        'gear_id': 'gear_id',
        'kilojoules': 'kilojoules',
        'average_watts': 'average_watts',
        'device_watts': 'device_watts',
        'max_watts': 'max_watts',
        'weighted_average_watts': 'weighted_average_watts'
    }

    def __init__(self, external_id=None, upload_id=None, athlete=None, name=None, distance=None, moving_time=None, elapsed_time=None, total_elevation_gain=None, elev_high=None, elev_low=None, type=None, start_date=None, start_date_local=None, timezone=None, start_latlng=None, end_latlng=None, achievement_count=None, kudos_count=None, comment_count=None, athlete_count=None, photo_count=None, total_photo_count=None, map=None, trainer=None, commute=None, manual=None, private=None, flagged=None, workout_type=None, upload_id_str=None, average_speed=None, max_speed=None, has_kudoed=None, gear_id=None, kilojoules=None, average_watts=None, device_watts=None, max_watts=None, weighted_average_watts=None):  # noqa: E501
        """SummaryActivity - a model defined in Swagger"""  # noqa: E501

        self._external_id = None
        self._upload_id = None
        self._athlete = None
        self._name = None
        self._distance = None
        self._moving_time = None
        self._elapsed_time = None
        self._total_elevation_gain = None
        self._elev_high = None
        self._elev_low = None
        self._type = None
        self._start_date = None
        self._start_date_local = None
        self._timezone = None
        self._start_latlng = None
        self._end_latlng = None
        self._achievement_count = None
        self._kudos_count = None
        self._comment_count = None
        self._athlete_count = None
        self._photo_count = None
        self._total_photo_count = None
        self._map = None
        self._trainer = None
        self._commute = None
        self._manual = None
        self._private = None
        self._flagged = None
        self._workout_type = None
        self._upload_id_str = None
        self._average_speed = None
        self._max_speed = None
        self._has_kudoed = None
        self._gear_id = None
        self._kilojoules = None
        self._average_watts = None
        self._device_watts = None
        self._max_watts = None
        self._weighted_average_watts = None
        self.discriminator = None

        if external_id is not None:
            self.external_id = external_id
        if upload_id is not None:
            self.upload_id = upload_id
        if athlete is not None:
            self.athlete = athlete
        if name is not None:
            self.name = name
        if distance is not None:
            self.distance = distance
        if moving_time is not None:
            self.moving_time = moving_time
        if elapsed_time is not None:
            self.elapsed_time = elapsed_time
        if total_elevation_gain is not None:
            self.total_elevation_gain = total_elevation_gain
        if elev_high is not None:
            self.elev_high = elev_high
        if elev_low is not None:
            self.elev_low = elev_low
        if type is not None:
            self.type = type
        if start_date is not None:
            self.start_date = start_date
        if start_date_local is not None:
            self.start_date_local = start_date_local
        if timezone is not None:
            self.timezone = timezone
        if start_latlng is not None:
            self.start_latlng = start_latlng
        if end_latlng is not None:
            self.end_latlng = end_latlng
        if achievement_count is not None:
            self.achievement_count = achievement_count
        if kudos_count is not None:
            self.kudos_count = kudos_count
        if comment_count is not None:
            self.comment_count = comment_count
        if athlete_count is not None:
            self.athlete_count = athlete_count
        if photo_count is not None:
            self.photo_count = photo_count
        if total_photo_count is not None:
            self.total_photo_count = total_photo_count
        if map is not None:
            self.map = map
        if trainer is not None:
            self.trainer = trainer
        if commute is not None:
            self.commute = commute
        if manual is not None:
            self.manual = manual
        if private is not None:
            self.private = private
        if flagged is not None:
            self.flagged = flagged
        if workout_type is not None:
            self.workout_type = workout_type
        if upload_id_str is not None:
            self.upload_id_str = upload_id_str
        if average_speed is not None:
            self.average_speed = average_speed
        if max_speed is not None:
            self.max_speed = max_speed
        if has_kudoed is not None:
            self.has_kudoed = has_kudoed
        if gear_id is not None:
            self.gear_id = gear_id
        if kilojoules is not None:
            self.kilojoules = kilojoules
        if average_watts is not None:
            self.average_watts = average_watts
        if device_watts is not None:
            self.device_watts = device_watts
        if max_watts is not None:
            self.max_watts = max_watts
        if weighted_average_watts is not None:
            self.weighted_average_watts = weighted_average_watts

    @property
    def external_id(self):
        """Gets the external_id of this SummaryActivity.  # noqa: E501

        The identifier provided at upload time  # noqa: E501

        :return: The external_id of this SummaryActivity.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this SummaryActivity.

        The identifier provided at upload time  # noqa: E501

        :param external_id: The external_id of this SummaryActivity.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def upload_id(self):
        """Gets the upload_id of this SummaryActivity.  # noqa: E501

        The identifier of the upload that resulted in this activity  # noqa: E501

        :return: The upload_id of this SummaryActivity.  # noqa: E501
        :rtype: int
        """
        return self._upload_id

    @upload_id.setter
    def upload_id(self, upload_id):
        """Sets the upload_id of this SummaryActivity.

        The identifier of the upload that resulted in this activity  # noqa: E501

        :param upload_id: The upload_id of this SummaryActivity.  # noqa: E501
        :type: int
        """

        self._upload_id = upload_id

    @property
    def athlete(self):
        """Gets the athlete of this SummaryActivity.  # noqa: E501


        :return: The athlete of this SummaryActivity.  # noqa: E501
        :rtype: MetaAthlete
        """
        return self._athlete

    @athlete.setter
    def athlete(self, athlete):
        """Sets the athlete of this SummaryActivity.


        :param athlete: The athlete of this SummaryActivity.  # noqa: E501
        :type: MetaAthlete
        """

        self._athlete = athlete

    @property
    def name(self):
        """Gets the name of this SummaryActivity.  # noqa: E501

        The name of the activity  # noqa: E501

        :return: The name of this SummaryActivity.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SummaryActivity.

        The name of the activity  # noqa: E501

        :param name: The name of this SummaryActivity.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def distance(self):
        """Gets the distance of this SummaryActivity.  # noqa: E501

        The activity's distance, in meters  # noqa: E501

        :return: The distance of this SummaryActivity.  # noqa: E501
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this SummaryActivity.

        The activity's distance, in meters  # noqa: E501

        :param distance: The distance of this SummaryActivity.  # noqa: E501
        :type: float
        """

        self._distance = distance

    @property
    def moving_time(self):
        """Gets the moving_time of this SummaryActivity.  # noqa: E501

        The activity's moving time, in seconds  # noqa: E501

        :return: The moving_time of this SummaryActivity.  # noqa: E501
        :rtype: int
        """
        return self._moving_time

    @moving_time.setter
    def moving_time(self, moving_time):
        """Sets the moving_time of this SummaryActivity.

        The activity's moving time, in seconds  # noqa: E501

        :param moving_time: The moving_time of this SummaryActivity.  # noqa: E501
        :type: int
        """

        self._moving_time = moving_time

    @property
    def elapsed_time(self):
        """Gets the elapsed_time of this SummaryActivity.  # noqa: E501

        The activity's elapsed time, in seconds  # noqa: E501

        :return: The elapsed_time of this SummaryActivity.  # noqa: E501
        :rtype: int
        """
        return self._elapsed_time

    @elapsed_time.setter
    def elapsed_time(self, elapsed_time):
        """Sets the elapsed_time of this SummaryActivity.

        The activity's elapsed time, in seconds  # noqa: E501

        :param elapsed_time: The elapsed_time of this SummaryActivity.  # noqa: E501
        :type: int
        """

        self._elapsed_time = elapsed_time

    @property
    def total_elevation_gain(self):
        """Gets the total_elevation_gain of this SummaryActivity.  # noqa: E501

        The activity's total elevation gain.  # noqa: E501

        :return: The total_elevation_gain of this SummaryActivity.  # noqa: E501
        :rtype: float
        """
        return self._total_elevation_gain

    @total_elevation_gain.setter
    def total_elevation_gain(self, total_elevation_gain):
        """Sets the total_elevation_gain of this SummaryActivity.

        The activity's total elevation gain.  # noqa: E501

        :param total_elevation_gain: The total_elevation_gain of this SummaryActivity.  # noqa: E501
        :type: float
        """

        self._total_elevation_gain = total_elevation_gain

    @property
    def elev_high(self):
        """Gets the elev_high of this SummaryActivity.  # noqa: E501

        The activity's highest elevation, in meters  # noqa: E501

        :return: The elev_high of this SummaryActivity.  # noqa: E501
        :rtype: float
        """
        return self._elev_high

    @elev_high.setter
    def elev_high(self, elev_high):
        """Sets the elev_high of this SummaryActivity.

        The activity's highest elevation, in meters  # noqa: E501

        :param elev_high: The elev_high of this SummaryActivity.  # noqa: E501
        :type: float
        """

        self._elev_high = elev_high

    @property
    def elev_low(self):
        """Gets the elev_low of this SummaryActivity.  # noqa: E501

        The activity's lowest elevation, in meters  # noqa: E501

        :return: The elev_low of this SummaryActivity.  # noqa: E501
        :rtype: float
        """
        return self._elev_low

    @elev_low.setter
    def elev_low(self, elev_low):
        """Sets the elev_low of this SummaryActivity.

        The activity's lowest elevation, in meters  # noqa: E501

        :param elev_low: The elev_low of this SummaryActivity.  # noqa: E501
        :type: float
        """

        self._elev_low = elev_low

    @property
    def type(self):
        """Gets the type of this SummaryActivity.  # noqa: E501


        :return: The type of this SummaryActivity.  # noqa: E501
        :rtype: ActivityType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SummaryActivity.


        :param type: The type of this SummaryActivity.  # noqa: E501
        :type: ActivityType
        """

        self._type = type

    @property
    def start_date(self):
        """Gets the start_date of this SummaryActivity.  # noqa: E501

        The time at which the activity was started.  # noqa: E501

        :return: The start_date of this SummaryActivity.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this SummaryActivity.

        The time at which the activity was started.  # noqa: E501

        :param start_date: The start_date of this SummaryActivity.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def start_date_local(self):
        """Gets the start_date_local of this SummaryActivity.  # noqa: E501

        The time at which the activity was started in the local timezone.  # noqa: E501

        :return: The start_date_local of this SummaryActivity.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date_local

    @start_date_local.setter
    def start_date_local(self, start_date_local):
        """Sets the start_date_local of this SummaryActivity.

        The time at which the activity was started in the local timezone.  # noqa: E501

        :param start_date_local: The start_date_local of this SummaryActivity.  # noqa: E501
        :type: datetime
        """

        self._start_date_local = start_date_local

    @property
    def timezone(self):
        """Gets the timezone of this SummaryActivity.  # noqa: E501

        The timezone of the activity  # noqa: E501

        :return: The timezone of this SummaryActivity.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this SummaryActivity.

        The timezone of the activity  # noqa: E501

        :param timezone: The timezone of this SummaryActivity.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def start_latlng(self):
        """Gets the start_latlng of this SummaryActivity.  # noqa: E501


        :return: The start_latlng of this SummaryActivity.  # noqa: E501
        :rtype: LatLng
        """
        return self._start_latlng

    @start_latlng.setter
    def start_latlng(self, start_latlng):
        """Sets the start_latlng of this SummaryActivity.


        :param start_latlng: The start_latlng of this SummaryActivity.  # noqa: E501
        :type: LatLng
        """

        self._start_latlng = start_latlng

    @property
    def end_latlng(self):
        """Gets the end_latlng of this SummaryActivity.  # noqa: E501


        :return: The end_latlng of this SummaryActivity.  # noqa: E501
        :rtype: LatLng
        """
        return self._end_latlng

    @end_latlng.setter
    def end_latlng(self, end_latlng):
        """Sets the end_latlng of this SummaryActivity.


        :param end_latlng: The end_latlng of this SummaryActivity.  # noqa: E501
        :type: LatLng
        """

        self._end_latlng = end_latlng

    @property
    def achievement_count(self):
        """Gets the achievement_count of this SummaryActivity.  # noqa: E501

        The number of achievements gained during this activity  # noqa: E501

        :return: The achievement_count of this SummaryActivity.  # noqa: E501
        :rtype: int
        """
        return self._achievement_count

    @achievement_count.setter
    def achievement_count(self, achievement_count):
        """Sets the achievement_count of this SummaryActivity.

        The number of achievements gained during this activity  # noqa: E501

        :param achievement_count: The achievement_count of this SummaryActivity.  # noqa: E501
        :type: int
        """

        self._achievement_count = achievement_count

    @property
    def kudos_count(self):
        """Gets the kudos_count of this SummaryActivity.  # noqa: E501

        The number of kudos given for this activity  # noqa: E501

        :return: The kudos_count of this SummaryActivity.  # noqa: E501
        :rtype: int
        """
        return self._kudos_count

    @kudos_count.setter
    def kudos_count(self, kudos_count):
        """Sets the kudos_count of this SummaryActivity.

        The number of kudos given for this activity  # noqa: E501

        :param kudos_count: The kudos_count of this SummaryActivity.  # noqa: E501
        :type: int
        """

        self._kudos_count = kudos_count

    @property
    def comment_count(self):
        """Gets the comment_count of this SummaryActivity.  # noqa: E501

        The number of comments for this activity  # noqa: E501

        :return: The comment_count of this SummaryActivity.  # noqa: E501
        :rtype: int
        """
        return self._comment_count

    @comment_count.setter
    def comment_count(self, comment_count):
        """Sets the comment_count of this SummaryActivity.

        The number of comments for this activity  # noqa: E501

        :param comment_count: The comment_count of this SummaryActivity.  # noqa: E501
        :type: int
        """

        self._comment_count = comment_count

    @property
    def athlete_count(self):
        """Gets the athlete_count of this SummaryActivity.  # noqa: E501

        The number of athletes for taking part in a group activity  # noqa: E501

        :return: The athlete_count of this SummaryActivity.  # noqa: E501
        :rtype: int
        """
        return self._athlete_count

    @athlete_count.setter
    def athlete_count(self, athlete_count):
        """Sets the athlete_count of this SummaryActivity.

        The number of athletes for taking part in a group activity  # noqa: E501

        :param athlete_count: The athlete_count of this SummaryActivity.  # noqa: E501
        :type: int
        """
        if athlete_count is not None and athlete_count < 1:  # noqa: E501
            raise ValueError("Invalid value for `athlete_count`, must be a value greater than or equal to `1`")  # noqa: E501

        self._athlete_count = athlete_count

    @property
    def photo_count(self):
        """Gets the photo_count of this SummaryActivity.  # noqa: E501

        The number of Instagram photos for this activity  # noqa: E501

        :return: The photo_count of this SummaryActivity.  # noqa: E501
        :rtype: int
        """
        return self._photo_count

    @photo_count.setter
    def photo_count(self, photo_count):
        """Sets the photo_count of this SummaryActivity.

        The number of Instagram photos for this activity  # noqa: E501

        :param photo_count: The photo_count of this SummaryActivity.  # noqa: E501
        :type: int
        """

        self._photo_count = photo_count

    @property
    def total_photo_count(self):
        """Gets the total_photo_count of this SummaryActivity.  # noqa: E501

        The number of Instagram and Strava photos for this activity  # noqa: E501

        :return: The total_photo_count of this SummaryActivity.  # noqa: E501
        :rtype: int
        """
        return self._total_photo_count

    @total_photo_count.setter
    def total_photo_count(self, total_photo_count):
        """Sets the total_photo_count of this SummaryActivity.

        The number of Instagram and Strava photos for this activity  # noqa: E501

        :param total_photo_count: The total_photo_count of this SummaryActivity.  # noqa: E501
        :type: int
        """

        self._total_photo_count = total_photo_count

    @property
    def map(self):
        """Gets the map of this SummaryActivity.  # noqa: E501


        :return: The map of this SummaryActivity.  # noqa: E501
        :rtype: PolylineMap
        """
        return self._map

    @map.setter
    def map(self, map):
        """Sets the map of this SummaryActivity.


        :param map: The map of this SummaryActivity.  # noqa: E501
        :type: PolylineMap
        """

        self._map = map

    @property
    def trainer(self):
        """Gets the trainer of this SummaryActivity.  # noqa: E501

        Whether this activity was recorded on a training machine  # noqa: E501

        :return: The trainer of this SummaryActivity.  # noqa: E501
        :rtype: bool
        """
        return self._trainer

    @trainer.setter
    def trainer(self, trainer):
        """Sets the trainer of this SummaryActivity.

        Whether this activity was recorded on a training machine  # noqa: E501

        :param trainer: The trainer of this SummaryActivity.  # noqa: E501
        :type: bool
        """

        self._trainer = trainer

    @property
    def commute(self):
        """Gets the commute of this SummaryActivity.  # noqa: E501

        Whether this activity is a commute  # noqa: E501

        :return: The commute of this SummaryActivity.  # noqa: E501
        :rtype: bool
        """
        return self._commute

    @commute.setter
    def commute(self, commute):
        """Sets the commute of this SummaryActivity.

        Whether this activity is a commute  # noqa: E501

        :param commute: The commute of this SummaryActivity.  # noqa: E501
        :type: bool
        """

        self._commute = commute

    @property
    def manual(self):
        """Gets the manual of this SummaryActivity.  # noqa: E501

        Whether this activity was created manually  # noqa: E501

        :return: The manual of this SummaryActivity.  # noqa: E501
        :rtype: bool
        """
        return self._manual

    @manual.setter
    def manual(self, manual):
        """Sets the manual of this SummaryActivity.

        Whether this activity was created manually  # noqa: E501

        :param manual: The manual of this SummaryActivity.  # noqa: E501
        :type: bool
        """

        self._manual = manual

    @property
    def private(self):
        """Gets the private of this SummaryActivity.  # noqa: E501

        Whether this activity is private  # noqa: E501

        :return: The private of this SummaryActivity.  # noqa: E501
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this SummaryActivity.

        Whether this activity is private  # noqa: E501

        :param private: The private of this SummaryActivity.  # noqa: E501
        :type: bool
        """

        self._private = private

    @property
    def flagged(self):
        """Gets the flagged of this SummaryActivity.  # noqa: E501

        Whether this activity is flagged  # noqa: E501

        :return: The flagged of this SummaryActivity.  # noqa: E501
        :rtype: bool
        """
        return self._flagged

    @flagged.setter
    def flagged(self, flagged):
        """Sets the flagged of this SummaryActivity.

        Whether this activity is flagged  # noqa: E501

        :param flagged: The flagged of this SummaryActivity.  # noqa: E501
        :type: bool
        """

        self._flagged = flagged

    @property
    def workout_type(self):
        """Gets the workout_type of this SummaryActivity.  # noqa: E501

        The activity's workout type  # noqa: E501

        :return: The workout_type of this SummaryActivity.  # noqa: E501
        :rtype: int
        """
        return self._workout_type

    @workout_type.setter
    def workout_type(self, workout_type):
        """Sets the workout_type of this SummaryActivity.

        The activity's workout type  # noqa: E501

        :param workout_type: The workout_type of this SummaryActivity.  # noqa: E501
        :type: int
        """

        self._workout_type = workout_type

    @property
    def upload_id_str(self):
        """Gets the upload_id_str of this SummaryActivity.  # noqa: E501

        The unique identifier of the upload in string format  # noqa: E501

        :return: The upload_id_str of this SummaryActivity.  # noqa: E501
        :rtype: str
        """
        return self._upload_id_str

    @upload_id_str.setter
    def upload_id_str(self, upload_id_str):
        """Sets the upload_id_str of this SummaryActivity.

        The unique identifier of the upload in string format  # noqa: E501

        :param upload_id_str: The upload_id_str of this SummaryActivity.  # noqa: E501
        :type: str
        """

        self._upload_id_str = upload_id_str

    @property
    def average_speed(self):
        """Gets the average_speed of this SummaryActivity.  # noqa: E501

        The activity's average speed, in meters per second  # noqa: E501

        :return: The average_speed of this SummaryActivity.  # noqa: E501
        :rtype: float
        """
        return self._average_speed

    @average_speed.setter
    def average_speed(self, average_speed):
        """Sets the average_speed of this SummaryActivity.

        The activity's average speed, in meters per second  # noqa: E501

        :param average_speed: The average_speed of this SummaryActivity.  # noqa: E501
        :type: float
        """

        self._average_speed = average_speed

    @property
    def max_speed(self):
        """Gets the max_speed of this SummaryActivity.  # noqa: E501

        The activity's max speed, in meters per second  # noqa: E501

        :return: The max_speed of this SummaryActivity.  # noqa: E501
        :rtype: float
        """
        return self._max_speed

    @max_speed.setter
    def max_speed(self, max_speed):
        """Sets the max_speed of this SummaryActivity.

        The activity's max speed, in meters per second  # noqa: E501

        :param max_speed: The max_speed of this SummaryActivity.  # noqa: E501
        :type: float
        """

        self._max_speed = max_speed

    @property
    def has_kudoed(self):
        """Gets the has_kudoed of this SummaryActivity.  # noqa: E501

        Whether the logged-in athlete has kudoed this activity  # noqa: E501

        :return: The has_kudoed of this SummaryActivity.  # noqa: E501
        :rtype: bool
        """
        return self._has_kudoed

    @has_kudoed.setter
    def has_kudoed(self, has_kudoed):
        """Sets the has_kudoed of this SummaryActivity.

        Whether the logged-in athlete has kudoed this activity  # noqa: E501

        :param has_kudoed: The has_kudoed of this SummaryActivity.  # noqa: E501
        :type: bool
        """

        self._has_kudoed = has_kudoed

    @property
    def gear_id(self):
        """Gets the gear_id of this SummaryActivity.  # noqa: E501

        The id of the gear for the activity  # noqa: E501

        :return: The gear_id of this SummaryActivity.  # noqa: E501
        :rtype: str
        """
        return self._gear_id

    @gear_id.setter
    def gear_id(self, gear_id):
        """Sets the gear_id of this SummaryActivity.

        The id of the gear for the activity  # noqa: E501

        :param gear_id: The gear_id of this SummaryActivity.  # noqa: E501
        :type: str
        """

        self._gear_id = gear_id

    @property
    def kilojoules(self):
        """Gets the kilojoules of this SummaryActivity.  # noqa: E501

        The total work done in kilojoules during this activity. Rides only  # noqa: E501

        :return: The kilojoules of this SummaryActivity.  # noqa: E501
        :rtype: float
        """
        return self._kilojoules

    @kilojoules.setter
    def kilojoules(self, kilojoules):
        """Sets the kilojoules of this SummaryActivity.

        The total work done in kilojoules during this activity. Rides only  # noqa: E501

        :param kilojoules: The kilojoules of this SummaryActivity.  # noqa: E501
        :type: float
        """

        self._kilojoules = kilojoules

    @property
    def average_watts(self):
        """Gets the average_watts of this SummaryActivity.  # noqa: E501

        Average power output in watts during this activity. Rides only  # noqa: E501

        :return: The average_watts of this SummaryActivity.  # noqa: E501
        :rtype: float
        """
        return self._average_watts

    @average_watts.setter
    def average_watts(self, average_watts):
        """Sets the average_watts of this SummaryActivity.

        Average power output in watts during this activity. Rides only  # noqa: E501

        :param average_watts: The average_watts of this SummaryActivity.  # noqa: E501
        :type: float
        """

        self._average_watts = average_watts

    @property
    def device_watts(self):
        """Gets the device_watts of this SummaryActivity.  # noqa: E501

        Whether the watts are from a power meter, false if estimated  # noqa: E501

        :return: The device_watts of this SummaryActivity.  # noqa: E501
        :rtype: bool
        """
        return self._device_watts

    @device_watts.setter
    def device_watts(self, device_watts):
        """Sets the device_watts of this SummaryActivity.

        Whether the watts are from a power meter, false if estimated  # noqa: E501

        :param device_watts: The device_watts of this SummaryActivity.  # noqa: E501
        :type: bool
        """

        self._device_watts = device_watts

    @property
    def max_watts(self):
        """Gets the max_watts of this SummaryActivity.  # noqa: E501

        Rides with power meter data only  # noqa: E501

        :return: The max_watts of this SummaryActivity.  # noqa: E501
        :rtype: int
        """
        return self._max_watts

    @max_watts.setter
    def max_watts(self, max_watts):
        """Sets the max_watts of this SummaryActivity.

        Rides with power meter data only  # noqa: E501

        :param max_watts: The max_watts of this SummaryActivity.  # noqa: E501
        :type: int
        """

        self._max_watts = max_watts

    @property
    def weighted_average_watts(self):
        """Gets the weighted_average_watts of this SummaryActivity.  # noqa: E501

        Similar to Normalized Power. Rides with power meter data only  # noqa: E501

        :return: The weighted_average_watts of this SummaryActivity.  # noqa: E501
        :rtype: int
        """
        return self._weighted_average_watts

    @weighted_average_watts.setter
    def weighted_average_watts(self, weighted_average_watts):
        """Sets the weighted_average_watts of this SummaryActivity.

        Similar to Normalized Power. Rides with power meter data only  # noqa: E501

        :param weighted_average_watts: The weighted_average_watts of this SummaryActivity.  # noqa: E501
        :type: int
        """

        self._weighted_average_watts = weighted_average_watts

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
        if issubclass(SummaryActivity, dict):
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
        if not isinstance(other, SummaryActivity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
