# generated from rosidl_generator_py/resource/_idl.py.em
# with input from cadt02_interfaces:msg/ArduinoFeedback.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_ArduinoFeedback(type):
    """Metaclass of message 'ArduinoFeedback'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('cadt02_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'cadt02_interfaces.msg.ArduinoFeedback')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__arduino_feedback
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__arduino_feedback
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__arduino_feedback
            cls._TYPE_SUPPORT = module.type_support_msg__msg__arduino_feedback
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__arduino_feedback

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class ArduinoFeedback(metaclass=Metaclass_ArduinoFeedback):
    """Message class 'ArduinoFeedback'."""

    __slots__ = [
        '_rail_btm',
        '_front_right',
        '_front_left',
        '_grp_ball',
        '_rail_top',
        '_start',
        '_retry',
        '_mode',
    ]

    _fields_and_field_types = {
        'rail_btm': 'boolean',
        'front_right': 'boolean',
        'front_left': 'boolean',
        'grp_ball': 'boolean',
        'rail_top': 'boolean',
        'start': 'boolean',
        'retry': 'boolean',
        'mode': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.rail_btm = kwargs.get('rail_btm', bool())
        self.front_right = kwargs.get('front_right', bool())
        self.front_left = kwargs.get('front_left', bool())
        self.grp_ball = kwargs.get('grp_ball', bool())
        self.rail_top = kwargs.get('rail_top', bool())
        self.start = kwargs.get('start', bool())
        self.retry = kwargs.get('retry', bool())
        self.mode = kwargs.get('mode', bool())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.rail_btm != other.rail_btm:
            return False
        if self.front_right != other.front_right:
            return False
        if self.front_left != other.front_left:
            return False
        if self.grp_ball != other.grp_ball:
            return False
        if self.rail_top != other.rail_top:
            return False
        if self.start != other.start:
            return False
        if self.retry != other.retry:
            return False
        if self.mode != other.mode:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def rail_btm(self):
        """Message field 'rail_btm'."""
        return self._rail_btm

    @rail_btm.setter
    def rail_btm(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'rail_btm' field must be of type 'bool'"
        self._rail_btm = value

    @property
    def front_right(self):
        """Message field 'front_right'."""
        return self._front_right

    @front_right.setter
    def front_right(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'front_right' field must be of type 'bool'"
        self._front_right = value

    @property
    def front_left(self):
        """Message field 'front_left'."""
        return self._front_left

    @front_left.setter
    def front_left(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'front_left' field must be of type 'bool'"
        self._front_left = value

    @property
    def grp_ball(self):
        """Message field 'grp_ball'."""
        return self._grp_ball

    @grp_ball.setter
    def grp_ball(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'grp_ball' field must be of type 'bool'"
        self._grp_ball = value

    @property
    def rail_top(self):
        """Message field 'rail_top'."""
        return self._rail_top

    @rail_top.setter
    def rail_top(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'rail_top' field must be of type 'bool'"
        self._rail_top = value

    @property
    def start(self):
        """Message field 'start'."""
        return self._start

    @start.setter
    def start(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'start' field must be of type 'bool'"
        self._start = value

    @property
    def retry(self):
        """Message field 'retry'."""
        return self._retry

    @retry.setter
    def retry(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'retry' field must be of type 'bool'"
        self._retry = value

    @property
    def mode(self):
        """Message field 'mode'."""
        return self._mode

    @mode.setter
    def mode(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'mode' field must be of type 'bool'"
        self._mode = value
