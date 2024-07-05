// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from cadt02_interfaces:msg/WayPoint.idl
// generated code does not contain a copyright notice

#ifndef CADT02_INTERFACES__MSG__DETAIL__WAY_POINT__STRUCT_HPP_
#define CADT02_INTERFACES__MSG__DETAIL__WAY_POINT__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__cadt02_interfaces__msg__WayPoint __attribute__((deprecated))
#else
# define DEPRECATED__cadt02_interfaces__msg__WayPoint __declspec(deprecated)
#endif

namespace cadt02_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct WayPoint_
{
  using Type = WayPoint_<ContainerAllocator>;

  explicit WayPoint_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->done = false;
      this->trajectory = false;
      this->error = 0.0;
    }
  }

  explicit WayPoint_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->done = false;
      this->trajectory = false;
      this->error = 0.0;
    }
  }

  // field types and members
  using _done_type =
    bool;
  _done_type done;
  using _trajectory_type =
    bool;
  _trajectory_type trajectory;
  using _error_type =
    double;
  _error_type error;

  // setters for named parameter idiom
  Type & set__done(
    const bool & _arg)
  {
    this->done = _arg;
    return *this;
  }
  Type & set__trajectory(
    const bool & _arg)
  {
    this->trajectory = _arg;
    return *this;
  }
  Type & set__error(
    const double & _arg)
  {
    this->error = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    cadt02_interfaces::msg::WayPoint_<ContainerAllocator> *;
  using ConstRawPtr =
    const cadt02_interfaces::msg::WayPoint_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<cadt02_interfaces::msg::WayPoint_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<cadt02_interfaces::msg::WayPoint_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      cadt02_interfaces::msg::WayPoint_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<cadt02_interfaces::msg::WayPoint_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      cadt02_interfaces::msg::WayPoint_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<cadt02_interfaces::msg::WayPoint_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<cadt02_interfaces::msg::WayPoint_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<cadt02_interfaces::msg::WayPoint_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__cadt02_interfaces__msg__WayPoint
    std::shared_ptr<cadt02_interfaces::msg::WayPoint_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__cadt02_interfaces__msg__WayPoint
    std::shared_ptr<cadt02_interfaces::msg::WayPoint_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const WayPoint_ & other) const
  {
    if (this->done != other.done) {
      return false;
    }
    if (this->trajectory != other.trajectory) {
      return false;
    }
    if (this->error != other.error) {
      return false;
    }
    return true;
  }
  bool operator!=(const WayPoint_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct WayPoint_

// alias to use template instance with default allocator
using WayPoint =
  cadt02_interfaces::msg::WayPoint_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace cadt02_interfaces

#endif  // CADT02_INTERFACES__MSG__DETAIL__WAY_POINT__STRUCT_HPP_
