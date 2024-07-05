// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from cadt02_interfaces:msg/SmartDriver.idl
// generated code does not contain a copyright notice
#include "cadt02_interfaces/msg/detail/smart_driver__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
cadt02_interfaces__msg__SmartDriver__init(cadt02_interfaces__msg__SmartDriver * msg)
{
  if (!msg) {
    return false;
  }
  // motor_id
  // goal
  // speedmode
  // stop
  // reset
  // voltagemode
  return true;
}

void
cadt02_interfaces__msg__SmartDriver__fini(cadt02_interfaces__msg__SmartDriver * msg)
{
  if (!msg) {
    return;
  }
  // motor_id
  // goal
  // speedmode
  // stop
  // reset
  // voltagemode
}

bool
cadt02_interfaces__msg__SmartDriver__are_equal(const cadt02_interfaces__msg__SmartDriver * lhs, const cadt02_interfaces__msg__SmartDriver * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // motor_id
  if (lhs->motor_id != rhs->motor_id) {
    return false;
  }
  // goal
  if (lhs->goal != rhs->goal) {
    return false;
  }
  // speedmode
  if (lhs->speedmode != rhs->speedmode) {
    return false;
  }
  // stop
  if (lhs->stop != rhs->stop) {
    return false;
  }
  // reset
  if (lhs->reset != rhs->reset) {
    return false;
  }
  // voltagemode
  if (lhs->voltagemode != rhs->voltagemode) {
    return false;
  }
  return true;
}

bool
cadt02_interfaces__msg__SmartDriver__copy(
  const cadt02_interfaces__msg__SmartDriver * input,
  cadt02_interfaces__msg__SmartDriver * output)
{
  if (!input || !output) {
    return false;
  }
  // motor_id
  output->motor_id = input->motor_id;
  // goal
  output->goal = input->goal;
  // speedmode
  output->speedmode = input->speedmode;
  // stop
  output->stop = input->stop;
  // reset
  output->reset = input->reset;
  // voltagemode
  output->voltagemode = input->voltagemode;
  return true;
}

cadt02_interfaces__msg__SmartDriver *
cadt02_interfaces__msg__SmartDriver__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  cadt02_interfaces__msg__SmartDriver * msg = (cadt02_interfaces__msg__SmartDriver *)allocator.allocate(sizeof(cadt02_interfaces__msg__SmartDriver), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(cadt02_interfaces__msg__SmartDriver));
  bool success = cadt02_interfaces__msg__SmartDriver__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
cadt02_interfaces__msg__SmartDriver__destroy(cadt02_interfaces__msg__SmartDriver * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    cadt02_interfaces__msg__SmartDriver__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
cadt02_interfaces__msg__SmartDriver__Sequence__init(cadt02_interfaces__msg__SmartDriver__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  cadt02_interfaces__msg__SmartDriver * data = NULL;

  if (size) {
    data = (cadt02_interfaces__msg__SmartDriver *)allocator.zero_allocate(size, sizeof(cadt02_interfaces__msg__SmartDriver), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = cadt02_interfaces__msg__SmartDriver__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        cadt02_interfaces__msg__SmartDriver__fini(&data[i - 1]);
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
cadt02_interfaces__msg__SmartDriver__Sequence__fini(cadt02_interfaces__msg__SmartDriver__Sequence * array)
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
      cadt02_interfaces__msg__SmartDriver__fini(&array->data[i]);
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

cadt02_interfaces__msg__SmartDriver__Sequence *
cadt02_interfaces__msg__SmartDriver__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  cadt02_interfaces__msg__SmartDriver__Sequence * array = (cadt02_interfaces__msg__SmartDriver__Sequence *)allocator.allocate(sizeof(cadt02_interfaces__msg__SmartDriver__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = cadt02_interfaces__msg__SmartDriver__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
cadt02_interfaces__msg__SmartDriver__Sequence__destroy(cadt02_interfaces__msg__SmartDriver__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    cadt02_interfaces__msg__SmartDriver__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
cadt02_interfaces__msg__SmartDriver__Sequence__are_equal(const cadt02_interfaces__msg__SmartDriver__Sequence * lhs, const cadt02_interfaces__msg__SmartDriver__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!cadt02_interfaces__msg__SmartDriver__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
cadt02_interfaces__msg__SmartDriver__Sequence__copy(
  const cadt02_interfaces__msg__SmartDriver__Sequence * input,
  cadt02_interfaces__msg__SmartDriver__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(cadt02_interfaces__msg__SmartDriver);
    cadt02_interfaces__msg__SmartDriver * data =
      (cadt02_interfaces__msg__SmartDriver *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!cadt02_interfaces__msg__SmartDriver__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          cadt02_interfaces__msg__SmartDriver__fini(&data[i]);
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
    if (!cadt02_interfaces__msg__SmartDriver__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
