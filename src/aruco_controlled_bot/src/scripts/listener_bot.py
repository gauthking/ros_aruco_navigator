#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from aruco_controlled_bot.msg import MarkerPosition

class TeleopBot:
    def __init__(self):
        rospy.init_node('teleop_bot', anonymous=True)
        rospy.Subscriber('marker_position', MarkerPosition, self.position_callback)
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.twist = Twist()

    def position_callback(self, position_msg):
        # Control the TurtleBot based on marker position
        if position_msg.y < 200:
            # Move forward
            self.twist.linear.x = 0.5  # Adjust velocity as needed
        elif position_msg.y > 500:
            # Move backward
            self.twist.linear.x = -0.5  # Adjust velocity as needed
        else:
            # Stop
            self.twist.linear.x = 0.0

        if position_msg.x < 350:
            # Turn right
            self.twist.angular.z = -0.5  # Adjust angular velocity as needed
        elif position_msg.x > 850:
            # Turn left
            self.twist.angular.z = 0.5  # Adjust angular velocity as needed
        else:
            # Stop turning
            self.twist.angular.z = 0.0

    def run(self):
        rate = rospy.Rate(10)  # 10 Hz
        while not rospy.is_shutdown():
            # Publish control commands
            self.cmd_vel_pub.publish(self.twist)
            rate.sleep()

if __name__ == '__main__':
    teleop_bot = TeleopBot()
    teleop_bot.run()
