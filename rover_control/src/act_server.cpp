#include "ros/ros.h"
#include "rover_control/act_srv.h"
bool drive(rover_control::act_srv::Request &req, rover_control::act_srv::Response &res)
{
    ROS_INFO("act triggered");

    return true;
}
int main(int argc, char **argv)
{
    ros::init(argc, argv, "actNode");
    ros::NodeHandle n;

    ros::ServiceServer actSrv = n.advertiseService("act_srv", drive);
    ROS_INFO("Ready to receive from client.");
    ros::spin();
    return 0;
}
