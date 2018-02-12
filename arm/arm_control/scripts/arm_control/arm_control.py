#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from sensor_msgs.msg import Joy
# from arm_control.arm_5DOF import arm
from arm_5DOF import arm


myArm = arm()


def read_joy(cmd_joy):
    if cmd_joy.buttons[0]:  # moving the point in space
        myArm.x += -10 * cmd_joy.axes[0]
        myArm.y += -10 * cmd_joy.axes[1]

    myArm.z += -5 * cmd_joy.axes[5]
    # n += cmd_joy.axes[2]/10
    # myArm.n = cmd_joy.axes[3]


    if cmd_joy.buttons[0] or cmd_joy.axes[5] != 0 :
        # rospy.loginfo("updated..")
        myArm.update_inverse()

    if cmd_joy.buttons[1]:  # intialization
        myArm.d1 = 436
        myArm.d2 = 334
        myArm.d3 = 243
        myArm.beta = 0
        myArm.calculate_forward()
    


def talker():
    rospy.init_node('joy_to_I2C', anonymous=False)
    rospy.Subscriber('/joy', Joy, read_joy,queue_size=5)
    pub = rospy.Publisher('actuator_lengths', String, queue_size=5)
    rate = rospy.Rate(2)  # 10hz
    while not rospy.is_shutdown():

        rospy.loginfo([myArm.x, myArm.y, myArm.z, myArm.n])
        # rospy.loginfo([myArm.d1, myArm.d2, myArm.d3, myArm.beta])
        pub.publish("$%.2f,%.2f,%.2f,%.2f*" %
                    (myArm.d1, myArm.d2, myArm.d3, myArm.beta))
        rospy.loginfo("$%.2f,%.2f,%.2f,%.2f*" %
                      (myArm.d1, myArm.d2, myArm.d3, myArm.beta))

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
