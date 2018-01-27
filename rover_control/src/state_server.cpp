#include "ros/ros.h"
#include "rover_control/state_srv.h"
#include "rover_control/act_srv.h"


// void drive(int, int);

bool custom_set(rover_control::state_srv::Request &req, rover_control::state_srv::Response &res)
{
    ros::NodeHandle n;
    // ROS_INFO("triggerd");
    // char* modes [5] = ["Init","Break","Manual", "Autonomous","Emergency"];
    switch (req.mode)
    {
    case 0:
        n.setParam("rover/mode", "Init");
        // res.state = "Init";
        break;
    case 1:
        n.setParam("rover/mode", "Break");
        // res.state = "Break";
        break;
    case 2:
        n.setParam("rover/mode", "Manual");
        // res.state = "Manual";
        break;
    case 3:
        n.setParam("rover/mode", "Autonomous");
        // res.state = "Autonomous";
        break;
    default:
        n.setParam("rover/mode", "Emergency");
        // res.state = "Emergency";
    }
    return true;
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "stateNode");
    ros::NodeHandle n;

    // Construct a map of strings
    std::map<std::string, std::string> rover;
    rover["mode"] = "init";
    rover["version"] = "4.0.1";
    rover["os"] = "ROS";
    rover["Power"] = "100\%";

    // Set and get a map of strings
    n.setParam("rover", rover);
    n.setParam("rover/motorPower", false);
    n.setParam("rover/armPower", false);
    // n.setParam("rover/usage", "explore");
    // n.getParam("my_string_map", map_s2);
    ros::ServiceServer stateSrv = n.advertiseService("state_srv", custom_set);
    // ROS_INFO("Ready to receive from client.");
    ros::spin();

    return 0;
}

void drive(int x, int y)
{
    ROS_INFO("drive triggerd");
    ros::NodeHandle n;
    ros::ServiceClient act_client = n.serviceClient<rover_control::act_srv>("act_srv");
    rover_control::act_srv srv_act;
    srv_act.request.vel[0] = 1;
    srv_act.request.vel[1] = 2;

    act_client.call(srv_act);
}
