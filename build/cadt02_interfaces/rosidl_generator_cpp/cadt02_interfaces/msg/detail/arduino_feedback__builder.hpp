// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from cadt02_interfaces:msg/ArduinoFeedback.idl
// generated code does not contain a copyright notice

#ifndef CADT02_INTERFACES__MSG__DETAIL__ARDUINO_FEEDBACK__BUILDER_HPP_
#define CADT02_INTERFACES__MSG__DETAIL__ARDUINO_FEEDBACK__BUILDER_HPP_

#include "cadt02_interfaces/msg/detail/arduino_feedback__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace cadt02_interfaces
{

namespace msg
{

namespace builder
{

class Init_ArduinoFeedback_mode
{
public:
  explicit Init_ArduinoFeedback_mode(::cadt02_interfaces::msg::ArduinoFeedback & msg)
  : msg_(msg)
  {}
  ::cadt02_interfaces::msg::ArduinoFeedback mode(::cadt02_interfaces::msg::ArduinoFeedback::_mode_type arg)
  {
    msg_.mode = std::move(arg);
    return std::move(msg_);
  }

private:
  ::cadt02_interfaces::msg::ArduinoFeedback msg_;
};

class Init_ArduinoFeedback_retry
{
public:
  explicit Init_ArduinoFeedback_retry(::cadt02_interfaces::msg::ArduinoFeedback & msg)
  : msg_(msg)
  {}
  Init_ArduinoFeedback_mode retry(::cadt02_interfaces::msg::ArduinoFeedback::_retry_type arg)
  {
    msg_.retry = std::move(arg);
    return Init_ArduinoFeedback_mode(msg_);
  }

private:
  ::cadt02_interfaces::msg::ArduinoFeedback msg_;
};

class Init_ArduinoFeedback_start
{
public:
  explicit Init_ArduinoFeedback_start(::cadt02_interfaces::msg::ArduinoFeedback & msg)
  : msg_(msg)
  {}
  Init_ArduinoFeedback_retry start(::cadt02_interfaces::msg::ArduinoFeedback::_start_type arg)
  {
    msg_.start = std::move(arg);
    return Init_ArduinoFeedback_retry(msg_);
  }

private:
  ::cadt02_interfaces::msg::ArduinoFeedback msg_;
};

class Init_ArduinoFeedback_rail_top
{
public:
  explicit Init_ArduinoFeedback_rail_top(::cadt02_interfaces::msg::ArduinoFeedback & msg)
  : msg_(msg)
  {}
  Init_ArduinoFeedback_start rail_top(::cadt02_interfaces::msg::ArduinoFeedback::_rail_top_type arg)
  {
    msg_.rail_top = std::move(arg);
    return Init_ArduinoFeedback_start(msg_);
  }

private:
  ::cadt02_interfaces::msg::ArduinoFeedback msg_;
};

class Init_ArduinoFeedback_grp_ball
{
public:
  explicit Init_ArduinoFeedback_grp_ball(::cadt02_interfaces::msg::ArduinoFeedback & msg)
  : msg_(msg)
  {}
  Init_ArduinoFeedback_rail_top grp_ball(::cadt02_interfaces::msg::ArduinoFeedback::_grp_ball_type arg)
  {
    msg_.grp_ball = std::move(arg);
    return Init_ArduinoFeedback_rail_top(msg_);
  }

private:
  ::cadt02_interfaces::msg::ArduinoFeedback msg_;
};

class Init_ArduinoFeedback_front_left
{
public:
  explicit Init_ArduinoFeedback_front_left(::cadt02_interfaces::msg::ArduinoFeedback & msg)
  : msg_(msg)
  {}
  Init_ArduinoFeedback_grp_ball front_left(::cadt02_interfaces::msg::ArduinoFeedback::_front_left_type arg)
  {
    msg_.front_left = std::move(arg);
    return Init_ArduinoFeedback_grp_ball(msg_);
  }

private:
  ::cadt02_interfaces::msg::ArduinoFeedback msg_;
};

class Init_ArduinoFeedback_front_right
{
public:
  explicit Init_ArduinoFeedback_front_right(::cadt02_interfaces::msg::ArduinoFeedback & msg)
  : msg_(msg)
  {}
  Init_ArduinoFeedback_front_left front_right(::cadt02_interfaces::msg::ArduinoFeedback::_front_right_type arg)
  {
    msg_.front_right = std::move(arg);
    return Init_ArduinoFeedback_front_left(msg_);
  }

private:
  ::cadt02_interfaces::msg::ArduinoFeedback msg_;
};

class Init_ArduinoFeedback_rail_btm
{
public:
  Init_ArduinoFeedback_rail_btm()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ArduinoFeedback_front_right rail_btm(::cadt02_interfaces::msg::ArduinoFeedback::_rail_btm_type arg)
  {
    msg_.rail_btm = std::move(arg);
    return Init_ArduinoFeedback_front_right(msg_);
  }

private:
  ::cadt02_interfaces::msg::ArduinoFeedback msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::cadt02_interfaces::msg::ArduinoFeedback>()
{
  return cadt02_interfaces::msg::builder::Init_ArduinoFeedback_rail_btm();
}

}  // namespace cadt02_interfaces

#endif  // CADT02_INTERFACES__MSG__DETAIL__ARDUINO_FEEDBACK__BUILDER_HPP_
