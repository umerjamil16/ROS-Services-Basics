#! /usr/bin/env python

import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse # you import the service message python classes generated from Empty.srv.
#from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def my_callback(request):

    sides = request.side
    rep = request.repetitions

    loop_func(4, sides)


    response = BB8CustomServiceMessageResponse()
    response.success = True
    return response

def loop_func(count, sides):

    i = 0
    while(i < count):
        go_str(sides)
        rotate()
        i = i + 1

def go_str(sides):
    wait_time = float(sides/10)
    pub.publish(move(0.2,0,0,0,0,0))
    rospy.sleep(wait_time) # Sleeps for 1 sec
    pub.publish(move(0,0,0,0,0,0))

def rotate():
    #Starts a new node
    vel_msg = Twist()
    # Receiveing the user's input
    print("Rotating robot")
    speed = 45 #input("Input your speed (degrees/sec):")
    angle = 45 #input("Type your distance (degrees):")
    clockwise = True #input("Clockwise?: ") #True or false

     #Converting from angles to radians
    angular_speed = speed*2*PI/360
    relative_angle = angle*2*PI/360

     #We wont use linear components
    vel_msg.linear.x=0
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0

     # Checking if our movement is CW or CCW
    if clockwise:
        vel_msg.angular.z = -abs(angular_speed)
    else:
        vel_msg.angular.z = abs(angular_speed)
    # Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while(current_angle < relative_angle):
        pub.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)

     #Forcing our robot to stop
    vel_msg.angular.z = 0
    pub.publish(vel_msg)
#    rospy.spin()

def move(x1, y1, z1, x2, y2, z2):
    move = Twist()
    move.linear.x = x1
    move.linear.y = y1
    move.linear.z = z1

    move.angular.x = x2
    move.angular.y = y2
    move.angular.z = z2
    return move

rospy.init_node('move_bb8_in_square_custom')
my_service = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage , my_callback )# create the Service called my_service with the defined callback

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rospy.loginfo("Service /move_bb8_in_square_custom Ready")
rate = rospy.Rate(1)

rospy.spin() # maintain the service open.