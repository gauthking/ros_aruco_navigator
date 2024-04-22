#!/usr/bin/env python

import cv2 as cv
from cv2 import aruco
import numpy as np
import rospy
from aruco_controlled_bot.msg import MarkerPosition
import threading

def display_camera_feed():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Unable to open camera")
        return

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to capture frame")
            break

        cv.imshow('Camera Feed', frame)

        key = cv.waitKey(1)
        if key == ord('q'):
            break

        # Pass the frame to the talker function
        talker(frame)

    cap.release()
    cv.destroyAllWindows()

def talker(frame):
    pub = rospy.Publisher('marker_position', MarkerPosition, queue_size=10)
    rate = rospy.Rate(10)  # 10hz

    calib_data_path = "./src/aruco_controlled_bot/src/scripts/calib_data/MultiMatrix.npz"
    calib_data = np.load(calib_data_path)
    cam_mat = calib_data["camMatrix"]
    dist_coef = calib_data["distCoef"]
    
    r_vectors = calib_data["rVector"]
    t_vectors = calib_data["tVector"]

    MARKER_SIZE = 16  # centimeters
    marker_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
    param_markers = aruco.DetectorParameters_create()

    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    marker_corners, marker_IDs, _ = aruco.detectMarkers(
        gray_frame, marker_dict, parameters=param_markers
    )
    
    if marker_corners:
        rVec, tVec, _ = aruco.estimatePoseSingleMarkers(
            marker_corners, MARKER_SIZE, cam_mat, dist_coef
        )
        total_markers = range(0, marker_IDs.size)
        for ids, rvec, tvec, i in zip(marker_IDs, rVec, tVec, total_markers):
            distance = np.sqrt(
                tVec[i][0][2] ** 2 + tVec[i][0][0] ** 2 + tVec[i][0][1] ** 2
            )
            # Convert rotation vector to rotation matrix
            rot_mat, _ = cv.Rodrigues(rvec)
            # Extract Euler angles from rotation matrix
            roll, pitch, yaw = cv.RQDecomp3x3(rot_mat)[0]
            marker_position = MarkerPosition()
            for corners in marker_corners:
                centroid = np.mean(corners.squeeze(), axis=0)
                marker_position.x = centroid[0]
                marker_position.y = centroid[1]
                marker_position.z = distance 
                marker_position.roll= np.degrees(roll)
                marker_position.pitch = np.degrees(pitch)
                marker_position.yaw = np.degrees(yaw)
                pub.publish(marker_position)
                rospy.loginfo("Published marker position: {}".format(marker_position))

    rate.sleep()

if __name__ == '__main__':
    rospy.init_node('controller', anonymous=True)  # Initialize ROS node
    try:
        display_thread = threading.Thread(target=display_camera_feed)
        display_thread.daemon = True
        display_thread.start()
        rospy.spin()  # Keep the main thread alive
    except rospy.ROSInterruptException:
        pass
