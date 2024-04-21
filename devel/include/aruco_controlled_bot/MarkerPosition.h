// Generated by gencpp from file aruco_controlled_bot/MarkerPosition.msg
// DO NOT EDIT!


#ifndef ARUCO_CONTROLLED_BOT_MESSAGE_MARKERPOSITION_H
#define ARUCO_CONTROLLED_BOT_MESSAGE_MARKERPOSITION_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace aruco_controlled_bot
{
template <class ContainerAllocator>
struct MarkerPosition_
{
  typedef MarkerPosition_<ContainerAllocator> Type;

  MarkerPosition_()
    : x(0.0)
    , y(0.0)
    , z(0.0)  {
    }
  MarkerPosition_(const ContainerAllocator& _alloc)
    : x(0.0)
    , y(0.0)
    , z(0.0)  {
  (void)_alloc;
    }



   typedef double _x_type;
  _x_type x;

   typedef double _y_type;
  _y_type y;

   typedef double _z_type;
  _z_type z;





  typedef boost::shared_ptr< ::aruco_controlled_bot::MarkerPosition_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::aruco_controlled_bot::MarkerPosition_<ContainerAllocator> const> ConstPtr;

}; // struct MarkerPosition_

typedef ::aruco_controlled_bot::MarkerPosition_<std::allocator<void> > MarkerPosition;

typedef boost::shared_ptr< ::aruco_controlled_bot::MarkerPosition > MarkerPositionPtr;
typedef boost::shared_ptr< ::aruco_controlled_bot::MarkerPosition const> MarkerPositionConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::aruco_controlled_bot::MarkerPosition_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::aruco_controlled_bot::MarkerPosition_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::aruco_controlled_bot::MarkerPosition_<ContainerAllocator1> & lhs, const ::aruco_controlled_bot::MarkerPosition_<ContainerAllocator2> & rhs)
{
  return lhs.x == rhs.x &&
    lhs.y == rhs.y &&
    lhs.z == rhs.z;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::aruco_controlled_bot::MarkerPosition_<ContainerAllocator1> & lhs, const ::aruco_controlled_bot::MarkerPosition_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace aruco_controlled_bot

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::aruco_controlled_bot::MarkerPosition_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::aruco_controlled_bot::MarkerPosition_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::aruco_controlled_bot::MarkerPosition_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::aruco_controlled_bot::MarkerPosition_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::aruco_controlled_bot::MarkerPosition_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::aruco_controlled_bot::MarkerPosition_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::aruco_controlled_bot::MarkerPosition_<ContainerAllocator> >
{
  static const char* value()
  {
    return "4a842b65f413084dc2b10fb484ea7f17";
  }

  static const char* value(const ::aruco_controlled_bot::MarkerPosition_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x4a842b65f413084dULL;
  static const uint64_t static_value2 = 0xc2b10fb484ea7f17ULL;
};

template<class ContainerAllocator>
struct DataType< ::aruco_controlled_bot::MarkerPosition_<ContainerAllocator> >
{
  static const char* value()
  {
    return "aruco_controlled_bot/MarkerPosition";
  }

  static const char* value(const ::aruco_controlled_bot::MarkerPosition_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::aruco_controlled_bot::MarkerPosition_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 x\n"
"float64 y\n"
"float64 z\n"
;
  }

  static const char* value(const ::aruco_controlled_bot::MarkerPosition_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::aruco_controlled_bot::MarkerPosition_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.x);
      stream.next(m.y);
      stream.next(m.z);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct MarkerPosition_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::aruco_controlled_bot::MarkerPosition_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::aruco_controlled_bot::MarkerPosition_<ContainerAllocator>& v)
  {
    s << indent << "x: ";
    Printer<double>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<double>::stream(s, indent + "  ", v.y);
    s << indent << "z: ";
    Printer<double>::stream(s, indent + "  ", v.z);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ARUCO_CONTROLLED_BOT_MESSAGE_MARKERPOSITION_H
