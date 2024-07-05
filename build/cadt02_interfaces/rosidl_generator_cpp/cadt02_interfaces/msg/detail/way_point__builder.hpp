// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from cadt02_interfaces:msg/WayPoint.idl
// generated code does not contain a copyright notice

#ifndef CADT02_INTERFACES__MSG__DETAIL__WAY_POINT__BUILDER_HPP_
#define CADT02_INTERFACES__MSG__DETAIL__WAY_POINT__BUILDER_HPP_

#include "cadt02_interfaces/msg/detail/way_point__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace cadt02_interfaces
{

namespace msg
{

namespace builder
{

class Init_WayPoint_error
{
public:
  explicit Init_WayPoint_error(::cadt02_interfaces::msg::WayPoint & msg)
  : msg_(msg)
  {}
  ::cadt02_interfaces::msg::WayPoint error(::cadt02_interfaces::msg::WayPoint::_error_type arg)
  {
    msg_.error = std::move(arg);
    return std::move(msg_);
  }

private:
  ::cadt02_interfaces::msg::WayPoint msg_;
};

class Init_WayPoint_trajectory
{
public:
  explicit Init_WayPoint_trajectory(::cadt02_interfaces::msg::WayPoint & msg)
  : msg_(msg)
  {}
  Init_WayPoint_error trajectory(::cadt02_interfaces::msg::WayPoint::_trajectory_type arg)
  {
    msg_.trajectory = std::move(arg);
    return Init_WayPoint_error(msg_);
  }

private:
  ::cadt02_interfaces::msg::WayPoint msg_;
};

class Init_WayPoint_done
{
public:
  Init_WayPoint_done()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_WayPoint_trajectory done(::cadt02_interfaces::msg::WayPoint::_done_type arg)
  {
    msg_.done = std::move(arg);
    return Init_WayPoint_trajectory(msg_);
  }

private:
  ::cadt02_interfaces::msg::WayPoint msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::cadt02_interfaces::msg::WayPoint>()
{
  return cadt02_interfaces::msg::builder::Init_WayPoint_done();
}

}  // namespace cadt02_interfaces

#endif  // CADT02_INTERFACES__MSG__DETAIL__WAY_POINT__BUILDER_HPP_
