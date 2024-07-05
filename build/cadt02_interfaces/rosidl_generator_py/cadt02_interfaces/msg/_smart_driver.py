# generated from rosidl_generator_py/resource/_idl.py.em
# with input from cadt02_interfaces:msg/SmartDriver.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_SmartDriver(type):
    """Metaclass of message 'SmartDriver'."""

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
                'cadt02_interfaces.msg.SmartDriver')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__smart_driver
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__smart_driver
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__smart_driver
            cls._TYPE_SUPPORT = module.type_support_msg__msg__smart_driver
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__smart_driver

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class SmartDriver(metaclass=Metaclass_SmartDriver):
    """Message class 'SmartDriver'."""

    __slots__ = [
        '_motor_id',
        '_goal',
        '_speedmode',
        '_stop',
        '_reset',
        '_voltagemode',
    ]

    _fields_and_field_types = {
        'motor_id': 'uint16',
        'goal': 'float',
        'speedmode': 'boolean',
        'stop': 'boolean',
        'reset': 'boolean',
        'voltagemode': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.motor_id = kwargs.get('motor_id', int())
        self.goal = kwargs.get('goal', float())
        self.speedmode = kwargs.get('speedmode', bool())
        self.stop = kwargs.get('stop', bool())
        self.reset = kwargs.get('reset', bool())
        self.voltagemode = kwargs.get('voltagemode', bool())

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
        if self.motor_id != other.motor_id:
            return False
        if self.goal != other.goal:
            return False
        if self.speedmode != other.speedmode:
            return False
        if self.stop != other.stop:
            return False
        if self.reset != other.reset:
            return False
        if self.voltagemode != other.voltagemode:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def motor_id(self):
        """Message field 'motor_id'."""
        return self._motor_id

    @motor_id.setter
    def motor_id(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'motor_id' field must be of type 'int'"
            assert value >= 0 and value < 65536, \
                "The 'motor_id' field must be an unsigned integer in [0, 65535]"
        self._motor_id = value

    @property
    def goal(self):
        """Message field 'goal'."""
        return self._goal

    @goal.setter
    def goal(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'goal' field must be of type 'float'"
        self._goal = value

    @property
    def speedmode(self):
        """Message field 'speedmode'."""
        return self._speedmode

    @speedmode.setter
    def speedmode(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'speedmode' field must be of type 'bool'"
        self._speedmode = value

    @property
    def stop(self):
        """Message field 'stop'."""
        return self._stop

    @stop.setter
    def stop(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'stop' field must be of type 'bool'"
        self._stop = value

    @property
    def reset(self):
        """Message field 'reset'."""
        return self._reset

    @reset.setter
    def reset(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'reset' field must be of type 'bool'"
        self._reset = value

    @property
    def voltagemode(self):
        """Message field 'voltagemode'."""
        return self._voltagemode

    @voltagemode.setter
    def voltagemode(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'voltagemode' field must be of type 'bool'"
        self._voltagemode = value
