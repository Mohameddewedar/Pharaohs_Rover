#!/usr/bin/env python
import time
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from sensor_msgs.msg import Joy
# from arm_control.arm_5DOF import arm
from arm_5DOF import arm

myArm = arm()


def read_joy(cmd_joy):
    if cmd_joy.buttons[0]:  # moving the point in space
        myArm.x += -1 * cmd_joy.axes[0]
        myArm.y += -1 * cmd_joy.axes[1]
        myArm.update_inverse()

    # n += cmd_joy.axes[2]/10
    # myArm.n = cmd_joy.axes[3]

    myArm.gripper = (cmd_joy.axes[3] + 1) * 45

    if cmd_joy.buttons[2] ^ cmd_joy.buttons[3]:
        if cmd_joy.buttons[2]:
            myArm.twist += -1
            if myArm.twist<=0:
                myArm.twist=1
        else:
            myArm.twist += 1
            if myArm.twist>=180:
                myArm.twist=179

    myArm.new_link += cmd_joy.axes[4]

    if cmd_joy.axes[5] != 0:
        myArm.z += 1 * cmd_joy.axes[5]
        myArm.update_inverse()

    if cmd_joy.buttons[6] ^ cmd_joy.buttons[7]:
        if cmd_joy.buttons[7]:
            myArm.d1 += 0.5
        else:
            myArm.d1 -= 0.5
        myArm.calculate_forward()

    if cmd_joy.buttons[8] ^ cmd_joy.buttons[9]:
        if cmd_joy.buttons[9]:
            myArm.d2 += 0.2
        else:
            myArm.d2 -= 0.2
        myArm.calculate_forward()

    if cmd_joy.buttons[10] ^ cmd_joy.buttons[11]:
        if cmd_joy.buttons[11]:
            myArm.d3 += 0.5
        else:
            myArm.d3 -= 0.5
        if myArm.d3 > 300:
            myArm.d3 = 300
        if myArm.d3 < 260:
            myArm.d3 = 260
        myArm.calculate_forward()

    if cmd_joy.buttons[1]:  # intialization
        myArm.initialize()
        myArm.calculate_forward()

    time.sleep(0.01)


def talker():
    rospy.init_node('joy_to_I2C', anonymous=False)
    rospy.Subscriber('/joy', Joy, read_joy, queue_size=5)
    pub = rospy.Publisher('actuator_lengths', String, queue_size=5)
    rate = rospy.Rate(25)  # 10hz
    while not rospy.is_shutdown():

        rospy.loginfo([myArm.x, myArm.y, myArm.z, myArm.n])
        # rospy.loginfo([myArm.d1, myArm.d2, myArm.d3, myArm.beta])
        pub.publish("$%i,%i,%i,%i,%i,%i,%i*" %
                    (myArm.d1, myArm.d2, myArm.d3, myArm.beta, myArm.new_link, myArm.twist, myArm.gripper))
        rospy.loginfo("$%i,%i,%i,%i,%i,%i,%i*" %
                      (myArm.d1, myArm.d2, myArm.d3, myArm.beta, myArm.new_link, myArm.twist, myArm.gripper))

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
