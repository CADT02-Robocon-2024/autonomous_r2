// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from cadt02_interfaces:msg/WayPoint.idl
// generated code does not contain a copyright notice

#ifndef CADT02_INTERFACES__MSG__DETAIL__WAY_POINT__TRAITS_HPP_
#define CADT02_INTERFACES__MSG__DETAIL__WAY_POINT__TRAITS_HPP_

#include "cadt02_interfaces/msg/detail/way_point__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<cadt02_interfaces::msg::WayPoint>()
{
  return "cadt02_interfaces::msg::WayPoint";
}

template<>
inline const char * name<cadt02_interfaces::msg::WayPoint>()
{
  return "cadt02_interfaces/msg/WayPoint";
}

template<>
struct has_fixed_size<cadt02_interfaces::msg::WayPoint>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<cadt02_interfaces::msg::WayPoint>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<cadt02_interfaces::msg::WayPoint>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // CADT02_INTERFACES__MSG__DETAIL__WAY_POINT__TRAITS_HPP_
