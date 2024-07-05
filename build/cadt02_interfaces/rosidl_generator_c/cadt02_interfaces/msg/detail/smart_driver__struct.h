// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from cadt02_interfaces:msg/SmartDriver.idl
// generated code does not contain a copyright notice

#ifndef CADT02_INTERFACES__MSG__DETAIL__SMART_DRIVER__STRUCT_H_
#define CADT02_INTERFACES__MSG__DETAIL__SMART_DRIVER__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/SmartDriver in the package cadt02_interfaces.
typedef struct cadt02_interfaces__msg__SmartDriver
{
  uint16_t motor_id;
  float goal;
  bool speedmode;
  bool stop;
  bool reset;
  bool voltagemode;
} cadt02_interfaces__msg__SmartDriver;

// Struct for a sequence of cadt02_interfaces__msg__SmartDriver.
typedef struct cadt02_interfaces__msg__SmartDriver__Sequence
{
  cadt02_interfaces__msg__SmartDriver * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} cadt02_interfaces__msg__SmartDriver__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CADT02_INTERFACES__MSG__DETAIL__SMART_DRIVER__STRUCT_H_
