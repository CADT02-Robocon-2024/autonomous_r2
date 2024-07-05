// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from cadt02_interfaces:msg/SmartDriver.idl
// generated code does not contain a copyright notice
#include "cadt02_interfaces/msg/detail/smart_driver__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "cadt02_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "cadt02_interfaces/msg/detail/smart_driver__struct.h"
#include "cadt02_interfaces/msg/detail/smart_driver__functions.h"
#include "fastcdr/Cdr.h"

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

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _SmartDriver__ros_msg_type = cadt02_interfaces__msg__SmartDriver;

static bool _SmartDriver__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _SmartDriver__ros_msg_type * ros_message = static_cast<const _SmartDriver__ros_msg_type *>(untyped_ros_message);
  // Field name: motor_id
  {
    cdr << ros_message->motor_id;
  }

  // Field name: goal
  {
    cdr << ros_message->goal;
  }

  // Field name: speedmode
  {
    cdr << (ros_message->speedmode ? true : false);
  }

  // Field name: stop
  {
    cdr << (ros_message->stop ? true : false);
  }

  // Field name: reset
  {
    cdr << (ros_message->reset ? true : false);
  }

  // Field name: voltagemode
  {
    cdr << (ros_message->voltagemode ? true : false);
  }

  return true;
}

static bool _SmartDriver__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _SmartDriver__ros_msg_type * ros_message = static_cast<_SmartDriver__ros_msg_type *>(untyped_ros_message);
  // Field name: motor_id
  {
    cdr >> ros_message->motor_id;
  }

  // Field name: goal
  {
    cdr >> ros_message->goal;
  }

  // Field name: speedmode
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->speedmode = tmp ? true : false;
  }

  // Field name: stop
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->stop = tmp ? true : false;
  }

  // Field name: reset
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->reset = tmp ? true : false;
  }

  // Field name: voltagemode
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->voltagemode = tmp ? true : false;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_cadt02_interfaces
size_t get_serialized_size_cadt02_interfaces__msg__SmartDriver(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _SmartDriver__ros_msg_type * ros_message = static_cast<const _SmartDriver__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name motor_id
  {
    size_t item_size = sizeof(ros_message->motor_id);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name goal
  {
    size_t item_size = sizeof(ros_message->goal);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name speedmode
  {
    size_t item_size = sizeof(ros_message->speedmode);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name stop
  {
    size_t item_size = sizeof(ros_message->stop);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name reset
  {
    size_t item_size = sizeof(ros_message->reset);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name voltagemode
  {
    size_t item_size = sizeof(ros_message->voltagemode);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _SmartDriver__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_cadt02_interfaces__msg__SmartDriver(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_cadt02_interfaces
size_t max_serialized_size_cadt02_interfaces__msg__SmartDriver(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: motor_id
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }
  // member: goal
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: speedmode
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: stop
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: reset
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: voltagemode
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static size_t _SmartDriver__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_cadt02_interfaces__msg__SmartDriver(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_SmartDriver = {
  "cadt02_interfaces::msg",
  "SmartDriver",
  _SmartDriver__cdr_serialize,
  _SmartDriver__cdr_deserialize,
  _SmartDriver__get_serialized_size,
  _SmartDriver__max_serialized_size
};

static rosidl_message_type_support_t _SmartDriver__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_SmartDriver,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, cadt02_interfaces, msg, SmartDriver)() {
  return &_SmartDriver__type_support;
}

#if defined(__cplusplus)
}
#endif
