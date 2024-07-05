// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from cadt02_interfaces:msg/SmartDriver.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "cadt02_interfaces/msg/detail/smart_driver__rosidl_typesupport_introspection_c.h"
#include "cadt02_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "cadt02_interfaces/msg/detail/smart_driver__functions.h"
#include "cadt02_interfaces/msg/detail/smart_driver__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void SmartDriver__rosidl_typesupport_introspection_c__SmartDriver_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  cadt02_interfaces__msg__SmartDriver__init(message_memory);
}

void SmartDriver__rosidl_typesupport_introspection_c__SmartDriver_fini_function(void * message_memory)
{
  cadt02_interfaces__msg__SmartDriver__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember SmartDriver__rosidl_typesupport_introspection_c__SmartDriver_message_member_array[6] = {
  {
    "motor_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(cadt02_interfaces__msg__SmartDriver, motor_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "goal",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(cadt02_interfaces__msg__SmartDriver, goal),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "speedmode",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(cadt02_interfaces__msg__SmartDriver, speedmode),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "stop",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(cadt02_interfaces__msg__SmartDriver, stop),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "reset",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(cadt02_interfaces__msg__SmartDriver, reset),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "voltagemode",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(cadt02_interfaces__msg__SmartDriver, voltagemode),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers SmartDriver__rosidl_typesupport_introspection_c__SmartDriver_message_members = {
  "cadt02_interfaces__msg",  // message namespace
  "SmartDriver",  // message name
  6,  // number of fields
  sizeof(cadt02_interfaces__msg__SmartDriver),
  SmartDriver__rosidl_typesupport_introspection_c__SmartDriver_message_member_array,  // message members
  SmartDriver__rosidl_typesupport_introspection_c__SmartDriver_init_function,  // function to initialize message memory (memory has to be allocated)
  SmartDriver__rosidl_typesupport_introspection_c__SmartDriver_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t SmartDriver__rosidl_typesupport_introspection_c__SmartDriver_message_type_support_handle = {
  0,
  &SmartDriver__rosidl_typesupport_introspection_c__SmartDriver_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_cadt02_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, cadt02_interfaces, msg, SmartDriver)() {
  if (!SmartDriver__rosidl_typesupport_introspection_c__SmartDriver_message_type_support_handle.typesupport_identifier) {
    SmartDriver__rosidl_typesupport_introspection_c__SmartDriver_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &SmartDriver__rosidl_typesupport_introspection_c__SmartDriver_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
