// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from cadt02_interfaces:msg/WayPoint.idl
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
#include "cadt02_interfaces/msg/detail/way_point__struct.h"
#include "cadt02_interfaces/msg/detail/way_point__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool cadt02_interfaces__msg__way_point__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[42];
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
    assert(strncmp("cadt02_interfaces.msg._way_point.WayPoint", full_classname_dest, 41) == 0);
  }
  cadt02_interfaces__msg__WayPoint * ros_message = _ros_message;
  {  // done
    PyObject * field = PyObject_GetAttrString(_pymsg, "done");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->done = (Py_True == field);
    Py_DECREF(field);
  }
  {  // trajectory
    PyObject * field = PyObject_GetAttrString(_pymsg, "trajectory");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->trajectory = (Py_True == field);
    Py_DECREF(field);
  }
  {  // error
    PyObject * field = PyObject_GetAttrString(_pymsg, "error");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->error = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * cadt02_interfaces__msg__way_point__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of WayPoint */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("cadt02_interfaces.msg._way_point");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "WayPoint");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  cadt02_interfaces__msg__WayPoint * ros_message = (cadt02_interfaces__msg__WayPoint *)raw_ros_message;
  {  // done
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->done ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "done", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // trajectory
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->trajectory ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "trajectory", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // error
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->error);
    {
      int rc = PyObject_SetAttrString(_pymessage, "error", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
