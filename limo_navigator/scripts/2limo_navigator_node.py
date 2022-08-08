#!/usr/bin/env python

import rospy

# Brings in the SimpleActionClient
import actionlib
# Brings in the .action file and messages used by the move base action
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client():

   # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()

   # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
   # Move 0.5 meters forward along the x axis of the "map" coordinate frame
    goal.target_pose.pose.position.x = 0.0
    goal.target_pose.pose.position.y = -2.0
   # No rotation of the mobile base frame w.r.t. map frame
    goal.target_pose.pose.orientation.w = 1.0
    goal.target_pose.pose.orientation.z = 8.0

   # Sends the goal to the action server.
    client.send_goal(goal)
   # Waits for the server to finish performing the action.
    wait = client.wait_for_result()
   # If the result doesn't arrive, assume the Server is not available
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
    # Result of executing the action
        return client.get_result()
    
    #rospy.sleep(10)   

def movebase_client2():

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal2 = MoveBaseGoal()
    goal2.target_pose.header.frame_id = "map"
    goal2.target_pose.header.stamp = rospy.Time.now()
    goal2.target_pose.pose.position.x = -4.0
    goal2.target_pose.pose.position.y = -2.0
    goal2.target_pose.pose.orientation.w = 1.0
    goal2.target_pose.pose.orientation.z = 2.0

    client.send_goal(goal2)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()

def movebase_client3():

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal3 = MoveBaseGoal()
    goal3.target_pose.header.frame_id = "map"
    goal3.target_pose.header.stamp = rospy.Time.now()
    goal3.target_pose.pose.position.x = -4.0
    goal3.target_pose.pose.position.y = 0.6
    goal3.target_pose.pose.orientation.w = 1.0

    client.send_goal(goal3)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result() 

def movebase_client4():

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal4 = MoveBaseGoal()
    goal4.target_pose.header.frame_id = "map"
    goal4.target_pose.header.stamp = rospy.Time.now()
    goal4.target_pose.pose.position.x = 0.0
    goal4.target_pose.pose.position.y = 0.0
    goal4.target_pose.pose.orientation.w = 1.0

    client.send_goal(goal4)
    wait = client.wait_for_result()
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()               

# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
    try:
       # Initializes a rospy node to let the SimpleActionClient publish and subscribe
        rospy.init_node('movebase_client_py')
        result = movebase_client()
        if result:
            rospy.loginfo("Goal1 execution done!")
        #rospy.sleep(10)
        result2 = movebase_client2()
        if result2:
            rospy.loginfo("Goal2 execution done!")
        result3 = movebase_client3()
        if result3:
            rospy.loginfo("Goal3 execution done!")
        result4 = movebase_client4()
        if result4:
            rospy.loginfo("Goal4 execution done!")                        

    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")


