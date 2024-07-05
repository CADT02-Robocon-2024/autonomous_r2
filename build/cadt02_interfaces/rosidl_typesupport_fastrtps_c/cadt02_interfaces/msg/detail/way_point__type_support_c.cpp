// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from cadt02_interfaces:msg/WayPoint.idl
// generated code does not contain a copyright notice
#include "cadt02_interfaces/msg/detail/way_point__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "cadt02_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "cadt02_interfaces/msg/detail/way_point__struct.h"
#include "cadt02_interfaces/msg/detail/way_point__functions.h"
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


using _WayPoint__ros_msg_type = cadt02_interfaces__msg__WayPoint;

static bool _WayPoint__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _WayPoint__ros_msg_type * ros_message = static_cast<const _WayPoint__ros_msg_type *>(untyped_ros_message);
  // Field name: done
  {
    cdr << (ros_message->done ? true : false);
  }

  // Field name: trajectory
  {
    cdr << (ros_message->trajectory ? true : false);
  }

  // Field name: error
  {
    cdr << ros_message->error;
  }

  return true;
}

static bool _WayPoint__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _WayPoint__ros_msg_type * ros_message = static_cast<_WayPoint__ros_msg_type *>(untyped_ros_message);
  // Field name: done
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->done = tmp ? true : false;
  }

  // Field name: trajectory
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->trajectory = tmp ? true : false;
  }

  // Field name: error
  {
    cdr >> ros_message->error;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_cadt02_interfaces
size_t get_serialized_size_cadt02_interfaces__msg__WayPoint(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _WayPoint__ros_msg_type * ros_message = static_cast<const _WayPoint__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name done
  {
    size_t item_size = sizeof(ros_message->done);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name trajectory
  {
    size_t item_size = sizeof(ros_message->trajectory);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name error
  {
    size_t item_size = sizeof(ros_message->error);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _WayPoint__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_cadt02_interfaces__msg__WayPoint(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_cadt02_interfaces
size_t max_serialized_size_cadt02_interfaces__msg__WayPoint(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: done
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: trajectory
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: error
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  return current_alignment - initial_alignment;
}

static size_t _WayPoint__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_cadt02_interfaces__msg__WayPoint(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_WayPoint = {
  "cadt02_interfaces::msg",
  "WayPoint",
  _WayPoint__cdr_serialize,
  _WayPoint__cdr_deserialize,
  _WayPoint__get_serialized_size,
  _WayPoint__max_serialized_size
};

static rosidl_message_type_support_t _WayPoint__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_WayPoint,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, cadt02_interfaces, msg, WayPoint)() {
  return &_WayPoint__type_support;
}

#if defined(__cplusplus)
}
#endif
