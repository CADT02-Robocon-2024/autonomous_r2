// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from cadt02_interfaces:msg/WayPoint.idl
// generated code does not contain a copyright notice

#ifndef CADT02_INTERFACES__MSG__DETAIL__WAY_POINT__STRUCT_H_
#define CADT02_INTERFACES__MSG__DETAIL__WAY_POINT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/WayPoint in the package cadt02_interfaces.
typedef struct cadt02_interfaces__msg__WayPoint
{
  bool done;
  bool trajectory;
  double error;
} cadt02_interfaces__msg__WayPoint;

// Struct for a sequence of cadt02_interfaces__msg__WayPoint.
typedef struct cadt02_interfaces__msg__WayPoint__Sequence
{
  cadt02_interfaces__msg__WayPoint * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} cadt02_interfaces__msg__WayPoint__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CADT02_INTERFACES__MSG__DETAIL__WAY_POINT__STRUCT_H_
