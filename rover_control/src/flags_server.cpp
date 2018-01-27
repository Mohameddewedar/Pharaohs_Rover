#include "ros/ros.h"
#include "rover_control/flags_srv.h"

bool change_flag(rover_control::flags_srv::Request &req, rover_control::flags_srv::Response &res)
{
    ros::NodeHandle n;
    // ROS_INFO("triggerd");
    switch (req.flag[0])
    {
    case 0:
        n.setParam("rover/motorPower", req.flag[1]==1?true:false);
    ROS_INFO(req.flag[1]==1?"true":"false");

        // res.state = "Init";
        break;
    case 1:
        n.setParam("rover/armPower", req.flag[1]==1?true:false);
        // res.state = "Break";
        break;
    //case 2:
    //     n.setParam("rover/mode", "Manual");
    //     // res.state = "Manual";
    //     break;
    // case 3:
    //     n.setParam("rover/mode", "Autonomous");
    //     // res.state = "Autonomous";
    //     break;
    default:
        // n.setParam("rover/mode", "Emergency");
        // res.state = "Emergency";
    	break;
    }
    return true;
}
int main(int argc, char **argv)
{
    ros::init(argc, argv, "flagsNode");
    ros::NodeHandle n;

    ros::ServiceServer flagsSrv = n.advertiseService("flags_srv", change_flag);
    ROS_INFO("Ready to receive from client.");
    ros::spin();
    return 0;
}
