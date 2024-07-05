// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from cadt02_interfaces:msg/SmartDriver.idl
// generated code does not contain a copyright notice

#ifndef CADT02_INTERFACES__MSG__DETAIL__SMART_DRIVER__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define CADT02_INTERFACES__MSG__DETAIL__SMART_DRIVER__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "cadt02_interfaces/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "cadt02_interfaces/msg/detail/smart_driver__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace cadt02_interfaces
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_cadt02_interfaces
cdr_serialize(
  const cadt02_interfaces::msg::SmartDriver & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_cadt02_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  cadt02_interfaces::msg::SmartDriver & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_cadt02_interfaces
get_serialized_size(
  const cadt02_interfaces::msg::SmartDriver & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_cadt02_interfaces
max_serialized_size_SmartDriver(
  bool & full_bounded,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace cadt02_interfaces

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_cadt02_interfaces
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, cadt02_interfaces, msg, SmartDriver)();

#ifdef __cplusplus
}
#endif

#endif  // CADT02_INTERFACES__MSG__DETAIL__SMART_DRIVER__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
