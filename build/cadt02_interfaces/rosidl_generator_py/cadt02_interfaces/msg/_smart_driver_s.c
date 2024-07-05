// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from cadt02_interfaces:msg/SmartDriver.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "cadt02_interfaces/msg/detail/smart_driver__struct.h"
#include "cadt02_interfaces/msg/detail/smart_driver__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool cadt02_interfaces__msg__smart_driver__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[48];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("cadt02_interfaces.msg._smart_driver.SmartDriver", full_classname_dest, 47) == 0);
  }
  cadt02_interfaces__msg__SmartDriver * ros_message = _ros_message;
  {  // motor_id
    PyObject * field = PyObject_GetAttrString(_pymsg, "motor_id");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->motor_id = (uint16_t)PyLong_AsUnsignedLong(field);
    Py_DECREF(field);
  }
  {  // goal
    PyObject * field = PyObject_GetAttrString(_pymsg, "goal");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->goal = (float)PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // speedmode
    PyObject * field = PyObject_GetAttrString(_pymsg, "speedmode");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->speedmode = (Py_True == field);
    Py_DECREF(field);
  }
  {  // stop
    PyObject * field = PyObject_GetAttrString(_pymsg, "stop");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->stop = (Py_True == field);
    Py_DECREF(field);
  }
  {  // reset
    PyObject * field = PyObject_GetAttrString(_pymsg, "reset");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->reset = (Py_True == field);
    Py_DECREF(field);
  }
  {  // voltagemode
    PyObject * field = PyObject_GetAttrString(_pymsg, "voltagemode");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->voltagemode = (Py_True == field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * cadt02_interfaces__msg__smart_driver__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of SmartDriver */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("cadt02_interfaces.msg._smart_driver");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "SmartDriver");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  cadt02_interfaces__msg__SmartDriver * ros_message = (cadt02_interfaces__msg__SmartDriver *)raw_ros_message;
  {  // motor_id
    PyObject * field = NULL;
    field = PyLong_FromUnsignedLong(ros_message->motor_id);
    {
      int rc = PyObject_SetAttrString(_pymessage, "motor_id", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // goal
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->goal);
    {
      int rc = PyObject_SetAttrString(_pymessage, "goal", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // speedmode
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->speedmode ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "speedmode", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // stop
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->stop ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "stop", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // reset
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->reset ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "reset", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // voltagemode
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->voltagemode ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "voltagemode", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
