#!/usr/bin/env python3  
import roslib
#roslib.load_manifest('learning_tf')
import rospy
from geometry_msgs.msg import PoseStamped
import tf
from tf2_msgs.msg import TFMessage                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             



def handle_turtle_pose(msg):
    global count
    global x_trans 
    global y_trans 
    global z_trans 
    global x_rot 
    global y_rot 
    global z_rot
    global w_rot
    global br

    

    # if msg.transforms[0].header.frame_id == "map" and msg.transforms[0].child_frame_id == "robot_base_link" and count == 0:
        # print("got frame, transforming")

    #     #br = tf.TransformBroadcaster()
    #     x_trans = msg.transforms[0].transform.translation.x + 0.73
    #     y_trans = msg.transforms[0].transform.translation.y + 0.24
    #     z_trans = 0
    #     x_rot = msg.transforms[0].transform.rotation.x  
    #     y_rot = msg.transforms[0].transform.rotation.y
    #     z_rot = msg.transforms[0].transform.rotation.z
    #     w_rot = msg.transforms[0].transform.rotation.w
    #     br.sendTransform((x_trans, y_trans, z_trans),
    #                     [x_rot, y_rot, z_rot, w_rot],
    #                     rospy.Time.now(),
    #                     "t265_odom_frame",
    #                     "map")

    #     count = 1
    # else:
    #     #br = tf.TransformBroadcaster()  
    #     br.sendTransform((x_trans, y_trans, z_trans),
    #                      [x_rot, y_rot, z_rot, w_rot],
    #                      rospy.Time.now(),
    #                      "t265_odom_frame",
    #                      "map")

    br.sendTransform((-.375, 0, 0),
    [0, 0, 0, 1],
    rospy.Time.now(),
    "base_footprint",
    "t265_pose_frame")
    



global count 
count = 0 

global x_trans 
global y_trans 
global z_trans 
global x_rot 
global y_rot 
global z_rot
global w_rot 

x_trans = 0
y_trans = 0
z_trans = 0
x_rot = 0
y_rot = 0
z_rot = 0
w_rot = 0


if __name__ == '__main__':
    global br
    rospy.init_node('robot_to_camera_tf_broadcaster')
    br = tf.TransformBroadcaster()  

    rospy.Timer(rospy.Duration(.001), handle_turtle_pose)             
    rospy.spin()