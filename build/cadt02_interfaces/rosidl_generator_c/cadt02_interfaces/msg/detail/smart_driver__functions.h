// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from cadt02_interfaces:msg/SmartDriver.idl
// generated code does not contain a copyright notice

#ifndef CADT02_INTERFACES__MSG__DETAIL__SMART_DRIVER__FUNCTIONS_H_
#define CADT02_INTERFACES__MSG__DETAIL__SMART_DRIVER__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "cadt02_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "cadt02_interfaces/msg/detail/smart_driver__struct.h"

/// Initialize msg/SmartDriver message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * cadt02_interfaces__msg__SmartDriver
 * )) before or use
 * cadt02_interfaces__msg__SmartDriver__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_cadt02_interfaces
bool
cadt02_interfaces__msg__SmartDriver__init(cadt02_interfaces__msg__SmartDriver * msg);

/// Finalize msg/SmartDriver message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_cadt02_interfaces
void
cadt02_interfaces__msg__SmartDriver__fini(cadt02_interfaces__msg__SmartDriver * msg);

/// Create msg/SmartDriver message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * cadt02_interfaces__msg__SmartDriver__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_cadt02_interfaces
cadt02_interfaces__msg__SmartDriver *
cadt02_interfaces__msg__SmartDriver__create();

/// Destroy msg/SmartDriver message.
/**
 * It calls
 * cadt02_interfaces__msg__SmartDriver__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_cadt02_interfaces
void
cadt02_interfaces__msg__SmartDriver__destroy(cadt02_interfaces__msg__SmartDriver * msg);

/// Check for msg/SmartDriver message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_cadt02_interfaces
bool
cadt02_interfaces__msg__SmartDriver__are_equal(const cadt02_interfaces__msg__SmartDriver * lhs, const cadt02_interfaces__msg__SmartDriver * rhs);

/// Copy a msg/SmartDriver message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_cadt02_interfaces
bool
cadt02_interfaces__msg__SmartDriver__copy(
  const cadt02_interfaces__msg__SmartDriver * input,
  cadt02_interfaces__msg__SmartDriver * output);

/// Initialize array of msg/SmartDriver messages.
/**
 * It allocates the memory for the number of elements and calls
 * cadt02_interfaces__msg__SmartDriver__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_cadt02_interfaces
bool
cadt02_interfaces__msg__SmartDriver__Sequence__init(cadt02_interfaces__msg__SmartDriver__Sequence * array, size_t size);

/// Finalize array of msg/SmartDriver messages.
/**
 * It calls
 * cadt02_interfaces__msg__SmartDriver__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_cadt02_interfaces
void
cadt02_interfaces__msg__SmartDriver__Sequence__fini(cadt02_interfaces__msg__SmartDriver__Sequence * array);

/// Create array of msg/SmartDriver messages.
/**
 * It allocates the memory for the array and calls
 * cadt02_interfaces__msg__SmartDriver__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_cadt02_interfaces
cadt02_interfaces__msg__SmartDriver__Sequence *
cadt02_interfaces__msg__SmartDriver__Sequence__create(size_t size);

/// Destroy array of msg/SmartDriver messages.
/**
 * It calls
 * cadt02_interfaces__msg__SmartDriver__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_cadt02_interfaces
void
cadt02_interfaces__msg__SmartDriver__Sequence__destroy(cadt02_interfaces__msg__SmartDriver__Sequence * array);

/// Check for msg/SmartDriver message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_cadt02_interfaces
bool
cadt02_interfaces__msg__SmartDriver__Sequence__are_equal(const cadt02_interfaces__msg__SmartDriver__Sequence * lhs, const cadt02_interfaces__msg__SmartDriver__Sequence * rhs);

/// Copy an array of msg/SmartDriver messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_cadt02_interfaces
bool
cadt02_interfaces__msg__SmartDriver__Sequence__copy(
  const cadt02_interfaces__msg__SmartDriver__Sequence * input,
  cadt02_interfaces__msg__SmartDriver__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // CADT02_INTERFACES__MSG__DETAIL__SMART_DRIVER__FUNCTIONS_H_
