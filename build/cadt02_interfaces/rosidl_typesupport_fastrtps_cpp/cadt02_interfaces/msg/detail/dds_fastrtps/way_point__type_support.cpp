// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from cadt02_interfaces:msg/WayPoint.idl
// generated code does not contain a copyright notice
#include "cadt02_interfaces/msg/detail/way_point__rosidl_typesupport_fastrtps_cpp.hpp"
#include "cadt02_interfaces/msg/detail/way_point__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace cadt02_interfaces
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_cadt02_interfaces
cdr_serialize(
  const cadt02_interfaces::msg::WayPoint & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: done
  cdr << (ros_message.done ? true : false);
  // Member: trajectory
  cdr << (ros_message.trajectory ? true : false);
  // Member: error
  cdr << ros_message.error;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_cadt02_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  cadt02_interfaces::msg::WayPoint & ros_message)
{
  // Member: done
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.done = tmp ? true : false;
  }

  // Member: trajectory
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.trajectory = tmp ? true : false;
  }

  // Member: error
  cdr >> ros_message.error;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_cadt02_interfaces
get_serialized_size(
  const cadt02_interfaces::msg::WayPoint & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: done
  {
    size_t item_size = sizeof(ros_message.done);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: trajectory
  {
    size_t item_size = sizeof(ros_message.trajectory);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: error
  {
    size_t item_size = sizeof(ros_message.error);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_cadt02_interfaces
max_serialized_size_WayPoint(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: done
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: trajectory
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: error
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  return current_alignment - initial_alignment;
}

static bool _WayPoint__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const cadt02_interfaces::msg::WayPoint *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _WayPoint__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<cadt02_interfaces::msg::WayPoint *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _WayPoint__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const cadt02_interfaces::msg::WayPoint *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _WayPoint__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_WayPoint(full_bounded, 0);
}

static message_type_support_callbacks_t _WayPoint__callbacks = {
  "cadt02_interfaces::msg",
  "WayPoint",
  _WayPoint__cdr_serialize,
  _WayPoint__cdr_deserialize,
  _WayPoint__get_serialized_size,
  _WayPoint__max_serialized_size
};

static rosidl_message_type_support_t _WayPoint__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_WayPoint__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace cadt02_interfaces

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_cadt02_interfaces
const rosidl_message_type_support_t *
get_message_type_support_handle<cadt02_interfaces::msg::WayPoint>()
{
  return &cadt02_interfaces::msg::typesupport_fastrtps_cpp::_WayPoint__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, cadt02_interfaces, msg, WayPoint)() {
  return &cadt02_interfaces::msg::typesupport_fastrtps_cpp::_WayPoint__handle;
}

#ifdef __cplusplus
}
#endif
