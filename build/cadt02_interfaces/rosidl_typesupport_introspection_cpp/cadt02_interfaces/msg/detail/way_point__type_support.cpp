// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from cadt02_interfaces:msg/WayPoint.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "cadt02_interfaces/msg/detail/way_point__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace cadt02_interfaces
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void WayPoint_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) cadt02_interfaces::msg::WayPoint(_init);
}

void WayPoint_fini_function(void * message_memory)
{
  auto typed_message = static_cast<cadt02_interfaces::msg::WayPoint *>(message_memory);
  typed_message->~WayPoint();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember WayPoint_message_member_array[3] = {
  {
    "done",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(cadt02_interfaces::msg::WayPoint, done),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "trajectory",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(cadt02_interfaces::msg::WayPoint, trajectory),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "error",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(cadt02_interfaces::msg::WayPoint, error),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers WayPoint_message_members = {
  "cadt02_interfaces::msg",  // message namespace
  "WayPoint",  // message name
  3,  // number of fields
  sizeof(cadt02_interfaces::msg::WayPoint),
  WayPoint_message_member_array,  // message members
  WayPoint_init_function,  // function to initialize message memory (memory has to be allocated)
  WayPoint_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t WayPoint_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &WayPoint_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace cadt02_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<cadt02_interfaces::msg::WayPoint>()
{
  return &::cadt02_interfaces::msg::rosidl_typesupport_introspection_cpp::WayPoint_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, cadt02_interfaces, msg, WayPoint)() {
  return &::cadt02_interfaces::msg::rosidl_typesupport_introspection_cpp::WayPoint_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
