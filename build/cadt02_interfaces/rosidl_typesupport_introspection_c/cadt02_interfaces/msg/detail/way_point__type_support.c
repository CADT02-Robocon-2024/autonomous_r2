// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from cadt02_interfaces:msg/WayPoint.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "cadt02_interfaces/msg/detail/way_point__rosidl_typesupport_introspection_c.h"
#include "cadt02_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "cadt02_interfaces/msg/detail/way_point__functions.h"
#include "cadt02_interfaces/msg/detail/way_point__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void WayPoint__rosidl_typesupport_introspection_c__WayPoint_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  cadt02_interfaces__msg__WayPoint__init(message_memory);
}

void WayPoint__rosidl_typesupport_introspection_c__WayPoint_fini_function(void * message_memory)
{
  cadt02_interfaces__msg__WayPoint__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember WayPoint__rosidl_typesupport_introspection_c__WayPoint_message_member_array[3] = {
  {
    "done",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(cadt02_interfaces__msg__WayPoint, done),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "trajectory",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(cadt02_interfaces__msg__WayPoint, trajectory),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "error",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(cadt02_interfaces__msg__WayPoint, error),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers WayPoint__rosidl_typesupport_introspection_c__WayPoint_message_members = {
  "cadt02_interfaces__msg",  // message namespace
  "WayPoint",  // message name
  3,  // number of fields
  sizeof(cadt02_interfaces__msg__WayPoint),
  WayPoint__rosidl_typesupport_introspection_c__WayPoint_message_member_array,  // message members
  WayPoint__rosidl_typesupport_introspection_c__WayPoint_init_function,  // function to initialize message memory (memory has to be allocated)
  WayPoint__rosidl_typesupport_introspection_c__WayPoint_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t WayPoint__rosidl_typesupport_introspection_c__WayPoint_message_type_support_handle = {
  0,
  &WayPoint__rosidl_typesupport_introspection_c__WayPoint_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_cadt02_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, cadt02_interfaces, msg, WayPoint)() {
  if (!WayPoint__rosidl_typesupport_introspection_c__WayPoint_message_type_support_handle.typesupport_identifier) {
    WayPoint__rosidl_typesupport_introspection_c__WayPoint_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &WayPoint__rosidl_typesupport_introspection_c__WayPoint_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
