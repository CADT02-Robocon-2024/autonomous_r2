// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from cadt02_interfaces:msg/ArduinoFeedback.idl
// generated code does not contain a copyright notice
#include "cadt02_interfaces/msg/detail/arduino_feedback__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
cadt02_interfaces__msg__ArduinoFeedback__init(cadt02_interfaces__msg__ArduinoFeedback * msg)
{
  if (!msg) {
    return false;
  }
  // rail_btm
  // front_right
  // front_left
  // grp_ball
  // rail_top
  // start
  // retry
  // mode
  return true;
}

void
cadt02_interfaces__msg__ArduinoFeedback__fini(cadt02_interfaces__msg__ArduinoFeedback * msg)
{
  if (!msg) {
    return;
  }
  // rail_btm
  // front_right
  // front_left
  // grp_ball
  // rail_top
  // start
  // retry
  // mode
}

bool
cadt02_interfaces__msg__ArduinoFeedback__are_equal(const cadt02_interfaces__msg__ArduinoFeedback * lhs, const cadt02_interfaces__msg__ArduinoFeedback * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // rail_btm
  if (lhs->rail_btm != rhs->rail_btm) {
    return false;
  }
  // front_right
  if (lhs->front_right != rhs->front_right) {
    return false;
  }
  // front_left
  if (lhs->front_left != rhs->front_left) {
    return false;
  }
  // grp_ball
  if (lhs->grp_ball != rhs->grp_ball) {
    return false;
  }
  // rail_top
  if (lhs->rail_top != rhs->rail_top) {
    return false;
  }
  // start
  if (lhs->start != rhs->start) {
    return false;
  }
  // retry
  if (lhs->retry != rhs->retry) {
    return false;
  }
  // mode
  if (lhs->mode != rhs->mode) {
    return false;
  }
  return true;
}

bool
cadt02_interfaces__msg__ArduinoFeedback__copy(
  const cadt02_interfaces__msg__ArduinoFeedback * input,
  cadt02_interfaces__msg__ArduinoFeedback * output)
{
  if (!input || !output) {
    return false;
  }
  // rail_btm
  output->rail_btm = input->rail_btm;
  // front_right
  output->front_right = input->front_right;
  // front_left
  output->front_left = input->front_left;
  // grp_ball
  output->grp_ball = input->grp_ball;
  // rail_top
  output->rail_top = input->rail_top;
  // start
  output->start = input->start;
  // retry
  output->retry = input->retry;
  // mode
  output->mode = input->mode;
  return true;
}

cadt02_interfaces__msg__ArduinoFeedback *
cadt02_interfaces__msg__ArduinoFeedback__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  cadt02_interfaces__msg__ArduinoFeedback * msg = (cadt02_interfaces__msg__ArduinoFeedback *)allocator.allocate(sizeof(cadt02_interfaces__msg__ArduinoFeedback), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(cadt02_interfaces__msg__ArduinoFeedback));
  bool success = cadt02_interfaces__msg__ArduinoFeedback__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
cadt02_interfaces__msg__ArduinoFeedback__destroy(cadt02_interfaces__msg__ArduinoFeedback * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    cadt02_interfaces__msg__ArduinoFeedback__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
cadt02_interfaces__msg__ArduinoFeedback__Sequence__init(cadt02_interfaces__msg__ArduinoFeedback__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  cadt02_interfaces__msg__ArduinoFeedback * data = NULL;

  if (size) {
    data = (cadt02_interfaces__msg__ArduinoFeedback *)allocator.zero_allocate(size, sizeof(cadt02_interfaces__msg__ArduinoFeedback), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = cadt02_interfaces__msg__ArduinoFeedback__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        cadt02_interfaces__msg__ArduinoFeedback__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
cadt02_interfaces__msg__ArduinoFeedback__Sequence__fini(cadt02_interfaces__msg__ArduinoFeedback__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      cadt02_interfaces__msg__ArduinoFeedback__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

cadt02_interfaces__msg__ArduinoFeedback__Sequence *
cadt02_interfaces__msg__ArduinoFeedback__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  cadt02_interfaces__msg__ArduinoFeedback__Sequence * array = (cadt02_interfaces__msg__ArduinoFeedback__Sequence *)allocator.allocate(sizeof(cadt02_interfaces__msg__ArduinoFeedback__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = cadt02_interfaces__msg__ArduinoFeedback__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
cadt02_interfaces__msg__ArduinoFeedback__Sequence__destroy(cadt02_interfaces__msg__ArduinoFeedback__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    cadt02_interfaces__msg__ArduinoFeedback__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
cadt02_interfaces__msg__ArduinoFeedback__Sequence__are_equal(const cadt02_interfaces__msg__ArduinoFeedback__Sequence * lhs, const cadt02_interfaces__msg__ArduinoFeedback__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!cadt02_interfaces__msg__ArduinoFeedback__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
cadt02_interfaces__msg__ArduinoFeedback__Sequence__copy(
  const cadt02_interfaces__msg__ArduinoFeedback__Sequence * input,
  cadt02_interfaces__msg__ArduinoFeedback__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(cadt02_interfaces__msg__ArduinoFeedback);
    cadt02_interfaces__msg__ArduinoFeedback * data =
      (cadt02_interfaces__msg__ArduinoFeedback *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!cadt02_interfaces__msg__ArduinoFeedback__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          cadt02_interfaces__msg__ArduinoFeedback__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!cadt02_interfaces__msg__ArduinoFeedback__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
