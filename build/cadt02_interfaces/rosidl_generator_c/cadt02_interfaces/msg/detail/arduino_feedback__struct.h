// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from cadt02_interfaces:msg/ArduinoFeedback.idl
// generated code does not contain a copyright notice

#ifndef CADT02_INTERFACES__MSG__DETAIL__ARDUINO_FEEDBACK__STRUCT_H_
#define CADT02_INTERFACES__MSG__DETAIL__ARDUINO_FEEDBACK__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/ArduinoFeedback in the package cadt02_interfaces.
typedef struct cadt02_interfaces__msg__ArduinoFeedback
{
  bool rail_btm;
  bool front_right;
  bool front_left;
  bool grp_ball;
  bool rail_top;
  bool start;
  bool retry;
  bool mode;
} cadt02_interfaces__msg__ArduinoFeedback;

// Struct for a sequence of cadt02_interfaces__msg__ArduinoFeedback.
typedef struct cadt02_interfaces__msg__ArduinoFeedback__Sequence
{
  cadt02_interfaces__msg__ArduinoFeedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} cadt02_interfaces__msg__ArduinoFeedback__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CADT02_INTERFACES__MSG__DETAIL__ARDUINO_FEEDBACK__STRUCT_H_
