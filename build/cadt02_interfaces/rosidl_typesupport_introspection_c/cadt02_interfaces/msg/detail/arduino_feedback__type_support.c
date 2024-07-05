// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from cadt02_interfaces:msg/ArduinoFeedback.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "cadt02_interfaces/msg/detail/arduino_feedback__rosidl_typesupport_introspection_c.h"
#include "cadt02_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "cadt02_interfaces/msg/detail/arduino_feedback__functions.h"
#include "cadt02_interfaces/msg/detail/arduino_feedback__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void ArduinoFeedback__rosidl_typesupport_introspection_c__ArduinoFeedback_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  cadt02_interfaces__msg__ArduinoFeedback__init(message_memory);
}

void ArduinoFeedback__rosidl_typesupport_introspection_c__ArduinoFeedback_fini_function(void * message_memory)
{
  cadt02_interfaces__msg__ArduinoFeedback__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember ArduinoFeedback__rosidl_typesupport_introspection_c__ArduinoFeedback_message_member_array[8] = {
  {
    "rail_btm",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(cadt02_interfaces__msg__ArduinoFeedback, rail_btm),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "front_right",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(cadt02_interfaces__msg__ArduinoFeedback, front_right),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "front_left",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(cadt02_interfaces__msg__ArduinoFeedback, front_left),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "grp_ball",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(cadt02_interfaces__msg__ArduinoFeedback, grp_ball),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "rail_top",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(cadt02_interfaces__msg__ArduinoFeedback, rail_top),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "start",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(cadt02_interfaces__msg__ArduinoFeedback, start),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "retry",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(cadt02_interfaces__msg__ArduinoFeedback, retry),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "mode",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(cadt02_interfaces__msg__ArduinoFeedback, mode),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers ArduinoFeedback__rosidl_typesupport_introspection_c__ArduinoFeedback_message_members = {
  "cadt02_interfaces__msg",  // message namespace
  "ArduinoFeedback",  // message name
  8,  // number of fields
  sizeof(cadt02_interfaces__msg__ArduinoFeedback),
  ArduinoFeedback__rosidl_typesupport_introspection_c__ArduinoFeedback_message_member_array,  // message members
  ArduinoFeedback__rosidl_typesupport_introspection_c__ArduinoFeedback_init_function,  // function to initialize message memory (memory has to be allocated)
  ArduinoFeedback__rosidl_typesupport_introspection_c__ArduinoFeedback_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t ArduinoFeedback__rosidl_typesupport_introspection_c__ArduinoFeedback_message_type_support_handle = {
  0,
  &ArduinoFeedback__rosidl_typesupport_introspection_c__ArduinoFeedback_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_cadt02_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, cadt02_interfaces, msg, ArduinoFeedback)() {
  if (!ArduinoFeedback__rosidl_typesupport_introspection_c__ArduinoFeedback_message_type_support_handle.typesupport_identifier) {
    ArduinoFeedback__rosidl_typesupport_introspection_c__ArduinoFeedback_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &ArduinoFeedback__rosidl_typesupport_introspection_c__ArduinoFeedback_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
