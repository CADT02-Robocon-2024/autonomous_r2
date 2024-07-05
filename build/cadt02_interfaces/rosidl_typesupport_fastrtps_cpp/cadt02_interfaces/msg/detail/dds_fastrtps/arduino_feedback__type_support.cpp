// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from cadt02_interfaces:msg/ArduinoFeedback.idl
// generated code does not contain a copyright notice
#include "cadt02_interfaces/msg/detail/arduino_feedback__rosidl_typesupport_fastrtps_cpp.hpp"
#include "cadt02_interfaces/msg/detail/arduino_feedback__struct.hpp"

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
  const cadt02_interfaces::msg::ArduinoFeedback & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: rail_btm
  cdr << (ros_message.rail_btm ? true : false);
  // Member: front_right
  cdr << (ros_message.front_right ? true : false);
  // Member: front_left
  cdr << (ros_message.front_left ? true : false);
  // Member: grp_ball
  cdr << (ros_message.grp_ball ? true : false);
  // Member: rail_top
  cdr << (ros_message.rail_top ? true : false);
  // Member: start
  cdr << (ros_message.start ? true : false);
  // Member: retry
  cdr << (ros_message.retry ? true : false);
  // Member: mode
  cdr << (ros_message.mode ? true : false);
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_cadt02_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  cadt02_interfaces::msg::ArduinoFeedback & ros_message)
{
  // Member: rail_btm
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.rail_btm = tmp ? true : false;
  }

  // Member: front_right
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.front_right = tmp ? true : false;
  }

  // Member: front_left
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.front_left = tmp ? true : false;
  }

  // Member: grp_ball
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.grp_ball = tmp ? true : false;
  }

  // Member: rail_top
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.rail_top = tmp ? true : false;
  }

  // Member: start
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.start = tmp ? true : false;
  }

  // Member: retry
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.retry = tmp ? true : false;
  }

  // Member: mode
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.mode = tmp ? true : false;
  }

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_cadt02_interfaces
get_serialized_size(
  const cadt02_interfaces::msg::ArduinoFeedback & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: rail_btm
  {
    size_t item_size = sizeof(ros_message.rail_btm);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: front_right
  {
    size_t item_size = sizeof(ros_message.front_right);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: front_left
  {
    size_t item_size = sizeof(ros_message.front_left);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: grp_ball
  {
    size_t item_size = sizeof(ros_message.grp_ball);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: rail_top
  {
    size_t item_size = sizeof(ros_message.rail_top);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: start
  {
    size_t item_size = sizeof(ros_message.start);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: retry
  {
    size_t item_size = sizeof(ros_message.retry);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: mode
  {
    size_t item_size = sizeof(ros_message.mode);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_cadt02_interfaces
max_serialized_size_ArduinoFeedback(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: rail_btm
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: front_right
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: front_left
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: grp_ball
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: rail_top
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: start
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: retry
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: mode
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static bool _ArduinoFeedback__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const cadt02_interfaces::msg::ArduinoFeedback *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _ArduinoFeedback__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<cadt02_interfaces::msg::ArduinoFeedback *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _ArduinoFeedback__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const cadt02_interfaces::msg::ArduinoFeedback *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _ArduinoFeedback__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_ArduinoFeedback(full_bounded, 0);
}

static message_type_support_callbacks_t _ArduinoFeedback__callbacks = {
  "cadt02_interfaces::msg",
  "ArduinoFeedback",
  _ArduinoFeedback__cdr_serialize,
  _ArduinoFeedback__cdr_deserialize,
  _ArduinoFeedback__get_serialized_size,
  _ArduinoFeedback__max_serialized_size
};

static rosidl_message_type_support_t _ArduinoFeedback__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_ArduinoFeedback__callbacks,
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
get_message_type_support_handle<cadt02_interfaces::msg::ArduinoFeedback>()
{
  return &cadt02_interfaces::msg::typesupport_fastrtps_cpp::_ArduinoFeedback__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, cadt02_interfaces, msg, ArduinoFeedback)() {
  return &cadt02_interfaces::msg::typesupport_fastrtps_cpp::_ArduinoFeedback__handle;
}

#ifdef __cplusplus
}
#endif
