// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from cadt02_interfaces:msg/ArduinoFeedback.idl
// generated code does not contain a copyright notice

#ifndef CADT02_INTERFACES__MSG__DETAIL__ARDUINO_FEEDBACK__STRUCT_HPP_
#define CADT02_INTERFACES__MSG__DETAIL__ARDUINO_FEEDBACK__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__cadt02_interfaces__msg__ArduinoFeedback __attribute__((deprecated))
#else
# define DEPRECATED__cadt02_interfaces__msg__ArduinoFeedback __declspec(deprecated)
#endif

namespace cadt02_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ArduinoFeedback_
{
  using Type = ArduinoFeedback_<ContainerAllocator>;

  explicit ArduinoFeedback_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->rail_btm = false;
      this->front_right = false;
      this->front_left = false;
      this->grp_ball = false;
      this->rail_top = false;
      this->start = false;
      this->retry = false;
      this->mode = false;
    }
  }

  explicit ArduinoFeedback_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->rail_btm = false;
      this->front_right = false;
      this->front_left = false;
      this->grp_ball = false;
      this->rail_top = false;
      this->start = false;
      this->retry = false;
      this->mode = false;
    }
  }

  // field types and members
  using _rail_btm_type =
    bool;
  _rail_btm_type rail_btm;
  using _front_right_type =
    bool;
  _front_right_type front_right;
  using _front_left_type =
    bool;
  _front_left_type front_left;
  using _grp_ball_type =
    bool;
  _grp_ball_type grp_ball;
  using _rail_top_type =
    bool;
  _rail_top_type rail_top;
  using _start_type =
    bool;
  _start_type start;
  using _retry_type =
    bool;
  _retry_type retry;
  using _mode_type =
    bool;
  _mode_type mode;

  // setters for named parameter idiom
  Type & set__rail_btm(
    const bool & _arg)
  {
    this->rail_btm = _arg;
    return *this;
  }
  Type & set__front_right(
    const bool & _arg)
  {
    this->front_right = _arg;
    return *this;
  }
  Type & set__front_left(
    const bool & _arg)
  {
    this->front_left = _arg;
    return *this;
  }
  Type & set__grp_ball(
    const bool & _arg)
  {
    this->grp_ball = _arg;
    return *this;
  }
  Type & set__rail_top(
    const bool & _arg)
  {
    this->rail_top = _arg;
    return *this;
  }
  Type & set__start(
    const bool & _arg)
  {
    this->start = _arg;
    return *this;
  }
  Type & set__retry(
    const bool & _arg)
  {
    this->retry = _arg;
    return *this;
  }
  Type & set__mode(
    const bool & _arg)
  {
    this->mode = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    cadt02_interfaces::msg::ArduinoFeedback_<ContainerAllocator> *;
  using ConstRawPtr =
    const cadt02_interfaces::msg::ArduinoFeedback_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<cadt02_interfaces::msg::ArduinoFeedback_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<cadt02_interfaces::msg::ArduinoFeedback_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      cadt02_interfaces::msg::ArduinoFeedback_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<cadt02_interfaces::msg::ArduinoFeedback_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      cadt02_interfaces::msg::ArduinoFeedback_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<cadt02_interfaces::msg::ArduinoFeedback_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<cadt02_interfaces::msg::ArduinoFeedback_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<cadt02_interfaces::msg::ArduinoFeedback_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__cadt02_interfaces__msg__ArduinoFeedback
    std::shared_ptr<cadt02_interfaces::msg::ArduinoFeedback_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__cadt02_interfaces__msg__ArduinoFeedback
    std::shared_ptr<cadt02_interfaces::msg::ArduinoFeedback_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ArduinoFeedback_ & other) const
  {
    if (this->rail_btm != other.rail_btm) {
      return false;
    }
    if (this->front_right != other.front_right) {
      return false;
    }
    if (this->front_left != other.front_left) {
      return false;
    }
    if (this->grp_ball != other.grp_ball) {
      return false;
    }
    if (this->rail_top != other.rail_top) {
      return false;
    }
    if (this->start != other.start) {
      return false;
    }
    if (this->retry != other.retry) {
      return false;
    }
    if (this->mode != other.mode) {
      return false;
    }
    return true;
  }
  bool operator!=(const ArduinoFeedback_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ArduinoFeedback_

// alias to use template instance with default allocator
using ArduinoFeedback =
  cadt02_interfaces::msg::ArduinoFeedback_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace cadt02_interfaces

#endif  // CADT02_INTERFACES__MSG__DETAIL__ARDUINO_FEEDBACK__STRUCT_HPP_
