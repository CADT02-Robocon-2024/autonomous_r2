// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from cadt02_interfaces:msg/SmartDriver.idl
// generated code does not contain a copyright notice
#include "cadt02_interfaces/msg/detail/smart_driver__rosidl_typesupport_fastrtps_cpp.hpp"
#include "cadt02_interfaces/msg/detail/smart_driver__struct.hpp"

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
  const cadt02_interfaces::msg::SmartDriver & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: motor_id
  cdr << ros_message.motor_id;
  // Member: goal
  cdr << ros_message.goal;
  // Member: speedmode
  cdr << (ros_message.speedmode ? true : false);
  // Member: stop
  cdr << (ros_message.stop ? true : false);
  // Member: reset
  cdr << (ros_message.reset ? true : false);
  // Member: voltagemode
  cdr << (ros_message.voltagemode ? true : false);
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_cadt02_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  cadt02_interfaces::msg::SmartDriver & ros_message)
{
  // Member: motor_id
  cdr >> ros_message.motor_id;

  // Member: goal
  cdr >> ros_message.goal;

  // Member: speedmode
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.speedmode = tmp ? true : false;
  }

  // Member: stop
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.stop = tmp ? true : false;
  }

  // Member: reset
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.reset = tmp ? true : false;
  }

  // Member: voltagemode
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.voltagemode = tmp ? true : false;
  }

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_cadt02_interfaces
get_serialized_size(
  const cadt02_interfaces::msg::SmartDriver & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: motor_id
  {
    size_t item_size = sizeof(ros_message.motor_id);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: goal
  {
    size_t item_size = sizeof(ros_message.goal);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: speedmode
  {
    size_t item_size = sizeof(ros_message.speedmode);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: stop
  {
    size_t item_size = sizeof(ros_message.stop);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: reset
  {
    size_t item_size = sizeof(ros_message.reset);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: voltagemode
  {
    size_t item_size = sizeof(ros_message.voltagemode);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_cadt02_interfaces
max_serialized_size_SmartDriver(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: motor_id
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }

  // Member: goal
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: speedmode
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: stop
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: reset
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: voltagemode
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static bool _SmartDriver__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const cadt02_interfaces::msg::SmartDriver *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _SmartDriver__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<cadt02_interfaces::msg::SmartDriver *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _SmartDriver__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const cadt02_interfaces::msg::SmartDriver *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _SmartDriver__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_SmartDriver(full_bounded, 0);
}

static message_type_support_callbacks_t _SmartDriver__callbacks = {
  "cadt02_interfaces::msg",
  "SmartDriver",
  _SmartDriver__cdr_serialize,
  _SmartDriver__cdr_deserialize,
  _SmartDriver__get_serialized_size,
  _SmartDriver__max_serialized_size
};

static rosidl_message_type_support_t _SmartDriver__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_SmartDriver__callbacks,
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
get_message_type_support_handle<cadt02_interfaces::msg::SmartDriver>()
{
  return &cadt02_interfaces::msg::typesupport_fastrtps_cpp::_SmartDriver__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, cadt02_interfaces, msg, SmartDriver)() {
  return &cadt02_interfaces::msg::typesupport_fastrtps_cpp::_SmartDriver__handle;
}

#ifdef __cplusplus
}
#endif
