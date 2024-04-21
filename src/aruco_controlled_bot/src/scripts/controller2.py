#!/usr/bin/env python

import cv2 as cv
from cv2 import aruco
import numpy as np
import rospy
from aruco_controlled_bot.msg import MarkerPosition

def talker():
    pub = rospy.Publisher('marker_position', MarkerPosition, queue_size=10)
    rospy.init_node('controller', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    cap = cv.VideoCapture(0)



    calib_data_path = "/home/vanderwaal/ros_proj/src/aruco_controlled_bot/src/scripts/calib_data/MultiMatrix.npz"
    calib_data = np.load(calib_data_path)
    cam_mat = calib_data["camMatrix"]
    dist_coef = calib_data["distCoef"]
    
    r_vectors = calib_data["rVector"]
    t_vectors = calib_data["tVector"]

    MARKER_SIZE = 16  # centimeters
    marker_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
    param_markers = aruco.DetectorParameters_create()

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if not ret:
            break
        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        marker_corners, marker_IDs, reject = aruco.detectMarkers(
        gray_frame, marker_dict, parameters=param_markers
        )
        if marker_corners:
            rVec, tVec, _ = aruco.estimatePoseSingleMarkers(
                marker_corners, MARKER_SIZE, cam_mat, dist_coef
            )
            total_markers = range(0, marker_IDs.size)
            for ids, rvec, tvec, i in zip(marker_IDs, rVec, tVec, total_markers):
                cv.polylines(
                    frame, [marker_corners[i].astype(np.int32)], True, (0, 255, 255), 4, cv.LINE_AA
                )
                corners = corners.reshape(4, 2)
                corners = corners.astype(int)
                top_right = tuple(corners[0].ravel())
                top_left = corners[1].ravel()
                bottom_right = tuple(corners[2].ravel())
                bottom_left = corners[3].ravel()
                
                # Convert rotation vector to rotation matrix
                rot_mat, _ = cv.Rodrigues(rvec)

                # Extract Euler angles from rotation matrix
                roll, pitch, yaw = cv.RQDecomp3x3(rot_mat)[0]

                # Print orientation in each axis
                print(f"Marker ID: {ids[0]}, Roll: {np.degrees(roll):.2f}, Pitch: {np.degrees(pitch):.2f}, Yaw: {np.degrees(yaw):.2f}")

                # Draw the detected marker and its pose
                

                distance = np.sqrt(
                tVec[i][0][2] ** 2 + tVec[i][0][0] ** 2 + tVec[i][0][1] ** 2
                )

                point = cv.drawFrameAxes(frame, cam_mat, dist_coef, rvec, tvec, 4)

        cv.imshow("frame", frame)
        

        if marker_corners:
            marker_position = MarkerPosition()
            for corners in marker_corners:
                centroid = np.mean(corners.squeeze(), axis=0)
                marker_position.x = centroid[0]
                marker_position.y = centroid[1]
                marker_position.z = distance 
                pub.publish(marker_position)
                rospy.loginfo("Published marker position: {}".format(marker_position))

        rate.sleep()
    cap.release()
    cv.destroyAllWindows()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
