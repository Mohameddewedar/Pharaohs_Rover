#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from sensor_msgs.msg import Joy
from arm_control.arm_5DOF import arm


myArm = arm()


def read_joy(cmd_joy):
    if cmd_joy.buttons[0]:  # moving the point in space
        myArm.x += cmd_joy.axes[0]
        myArm.y += cmd_joy.axes[1]
    myArm.z += cmd_joy.axes[5]
    # n += cmd_joy.axes[2]/10
    myArm.n = 0

    if cmd_joy.buttons[1]:  # intialization
        myArm.d1 = 0
        myArm.d2 = 0
        myArm.d3 = 0
        myArm.beta = 0

    if cmd_joy.buttons[0] or cmd_joy.axes[5] != 0 or cmd_joy.buttons[1]:
        myArm.update_inverse()


def talker():
    rospy.init_node('joy_to_I2C', anonymous=False)
    rospy.Subscriber('/joy', Joy, read_joy)
    pub = rospy.Publisher('actuator_lengths', String, queue_size=10)
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():

        rospy.loginfo([myArm.x, myArm.y, myArm.z, myArm.n])
        # rospy.loginfo([myArm.d1, myArm.d2, myArm.d3, myArm.beta])
        pub.publish("$%.2f,%.2f,%.2f,%.2f*" %
                    (myArm.d1, myArm.d2, myArm.d3, myArm.beta))
        # rospy.loginfo("$%.2f,%.2f,%.2f,%.2f*" %
        #               (myArm.d1, myArm.d2, myArm.d3, myArm.beta))

        # rospy.loginfo([myArm.d1[0:5], myArm.d2, myArm.d3, myArm.beta])

        # output.data=[int(myArm.d1*100), int(myArm.d2*100), int(myArm.d3*100), int(myArm.beta*100)]
        # pub.publish(output)
        # rospy.loginfo(output)
        
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
