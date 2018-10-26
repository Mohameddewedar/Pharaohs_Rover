#include "pi2c.h"
#include "ros/ros.h"
#include "std_msgs/String.h"
#include <iostream>
#include <sstream>

#define NO_REC_VALS 4 // d1 d2 d3 beta

using namespace std;
std::ostringstream message;
std::string tosend;
std::string feedback;
std_msgs::String feedback_msg;
int feedback_msg_length = 20;

char rec;
std::string out;
int count;
std::string recArray[NO_REC_VALS - 1];
bool valid = false;

std::string read_feedback()
{
  Pi2c arduino(43);
  arduino.i2cRead(&feedback[0], feedback_msg_length + 10);

  for (size_t i = 0; i < feedback.length(); i++)
  {
    rec = feedback[i];
    if (rec == '*')
    {
      valid = false;
    }
    if (valid && rec != ',')
    {
      out += rec;
    }
    else if (valid && rec == ',')
    {
      recArray[i] = out;
      out = "";
      i++;
    }
    if (!valid && rec == '$')
    {
      valid = true;
      i = 0;
    }

    feedback_msg_length = stoi(recArray[0]);

    return feedback;
  }
}

void i2c_operation(const std_msgs::String &lengths)
{
  Pi2c arduino(43);
  tosend = "";
  message.str("");
  message << lengths;
  tosend = message.str();
  std::cout << tosend << "\n";
  arduino.i2cWrite(&tosend[0], sizeof(tosend));
  feedback_msg.data = read_feedback();
}

int main(int argc, char **argv)
{

  ros::init(argc, argv, "to_rover_i2c");
  ros::NodeHandle nh;
  ros::Subscriber sub = nh.subscribe("/actuator_lengths", 100, i2c_operation);
  ros::Publisher feedback_publisher =
      nh.advertise<std_msgs::String>("/arm_feedback", 10);
  feedback_publisher.publish(feedback_msg); // not sure
  ros::spin(); // Not sure ros::spin() or ros::spinOnce() and where to put this

  return 0;
}
