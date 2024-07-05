// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from cadt02_interfaces:msg/SmartDriver.idl
// generated code does not contain a copyright notice

#ifndef CADT02_INTERFACES__MSG__DETAIL__SMART_DRIVER__BUILDER_HPP_
#define CADT02_INTERFACES__MSG__DETAIL__SMART_DRIVER__BUILDER_HPP_

#include "cadt02_interfaces/msg/detail/smart_driver__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace cadt02_interfaces
{

namespace msg
{

namespace builder
{

class Init_SmartDriver_voltagemode
{
public:
  explicit Init_SmartDriver_voltagemode(::cadt02_interfaces::msg::SmartDriver & msg)
  : msg_(msg)
  {}
  ::cadt02_interfaces::msg::SmartDriver voltagemode(::cadt02_interfaces::msg::SmartDriver::_voltagemode_type arg)
  {
    msg_.voltagemode = std::move(arg);
    return std::move(msg_);
  }

private:
  ::cadt02_interfaces::msg::SmartDriver msg_;
};

class Init_SmartDriver_reset
{
public:
  explicit Init_SmartDriver_reset(::cadt02_interfaces::msg::SmartDriver & msg)
  : msg_(msg)
  {}
  Init_SmartDriver_voltagemode reset(::cadt02_interfaces::msg::SmartDriver::_reset_type arg)
  {
    msg_.reset = std::move(arg);
    return Init_SmartDriver_voltagemode(msg_);
  }

private:
  ::cadt02_interfaces::msg::SmartDriver msg_;
};

class Init_SmartDriver_stop
{
public:
  explicit Init_SmartDriver_stop(::cadt02_interfaces::msg::SmartDriver & msg)
  : msg_(msg)
  {}
  Init_SmartDriver_reset stop(::cadt02_interfaces::msg::SmartDriver::_stop_type arg)
  {
    msg_.stop = std::move(arg);
    return Init_SmartDriver_reset(msg_);
  }

private:
  ::cadt02_interfaces::msg::SmartDriver msg_;
};

class Init_SmartDriver_speedmode
{
public:
  explicit Init_SmartDriver_speedmode(::cadt02_interfaces::msg::SmartDriver & msg)
  : msg_(msg)
  {}
  Init_SmartDriver_stop speedmode(::cadt02_interfaces::msg::SmartDriver::_speedmode_type arg)
  {
    msg_.speedmode = std::move(arg);
    return Init_SmartDriver_stop(msg_);
  }

private:
  ::cadt02_interfaces::msg::SmartDriver msg_;
};

class Init_SmartDriver_goal
{
public:
  explicit Init_SmartDriver_goal(::cadt02_interfaces::msg::SmartDriver & msg)
  : msg_(msg)
  {}
  Init_SmartDriver_speedmode goal(::cadt02_interfaces::msg::SmartDriver::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return Init_SmartDriver_speedmode(msg_);
  }

private:
  ::cadt02_interfaces::msg::SmartDriver msg_;
};

class Init_SmartDriver_motor_id
{
public:
  Init_SmartDriver_motor_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SmartDriver_goal motor_id(::cadt02_interfaces::msg::SmartDriver::_motor_id_type arg)
  {
    msg_.motor_id = std::move(arg);
    return Init_SmartDriver_goal(msg_);
  }

private:
  ::cadt02_interfaces::msg::SmartDriver msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::cadt02_interfaces::msg::SmartDriver>()
{
  return cadt02_interfaces::msg::builder::Init_SmartDriver_motor_id();
}

}  // namespace cadt02_interfaces

#endif  // CADT02_INTERFACES__MSG__DETAIL__SMART_DRIVER__BUILDER_HPP_
