// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from cadt02_interfaces:msg/ArduinoFeedback.idl
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
#include "cadt02_interfaces/msg/detail/arduino_feedback__struct.h"
#include "cadt02_interfaces/msg/detail/arduino_feedback__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool cadt02_interfaces__msg__arduino_feedback__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[56];
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
    assert(strncmp("cadt02_interfaces.msg._arduino_feedback.ArduinoFeedback", full_classname_dest, 55) == 0);
  }
  cadt02_interfaces__msg__ArduinoFeedback * ros_message = _ros_message;
  {  // rail_btm
    PyObject * field = PyObject_GetAttrString(_pymsg, "rail_btm");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->rail_btm = (Py_True == field);
    Py_DECREF(field);
  }
  {  // front_right
    PyObject * field = PyObject_GetAttrString(_pymsg, "front_right");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->front_right = (Py_True == field);
    Py_DECREF(field);
  }
  {  // front_left
    PyObject * field = PyObject_GetAttrString(_pymsg, "front_left");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->front_left = (Py_True == field);
    Py_DECREF(field);
  }
  {  // grp_ball
    PyObject * field = PyObject_GetAttrString(_pymsg, "grp_ball");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->grp_ball = (Py_True == field);
    Py_DECREF(field);
  }
  {  // rail_top
    PyObject * field = PyObject_GetAttrString(_pymsg, "rail_top");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->rail_top = (Py_True == field);
    Py_DECREF(field);
  }
  {  // start
    PyObject * field = PyObject_GetAttrString(_pymsg, "start");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->start = (Py_True == field);
    Py_DECREF(field);
  }
  {  // retry
    PyObject * field = PyObject_GetAttrString(_pymsg, "retry");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->retry = (Py_True == field);
    Py_DECREF(field);
  }
  {  // mode
    PyObject * field = PyObject_GetAttrString(_pymsg, "mode");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->mode = (Py_True == field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * cadt02_interfaces__msg__arduino_feedback__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of ArduinoFeedback */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("cadt02_interfaces.msg._arduino_feedback");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "ArduinoFeedback");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  cadt02_interfaces__msg__ArduinoFeedback * ros_message = (cadt02_interfaces__msg__ArduinoFeedback *)raw_ros_message;
  {  // rail_btm
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->rail_btm ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "rail_btm", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // front_right
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->front_right ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "front_right", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // front_left
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->front_left ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "front_left", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // grp_ball
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->grp_ball ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "grp_ball", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // rail_top
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->rail_top ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "rail_top", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // start
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->start ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "start", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // retry
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->retry ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "retry", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // mode
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->mode ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "mode", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
