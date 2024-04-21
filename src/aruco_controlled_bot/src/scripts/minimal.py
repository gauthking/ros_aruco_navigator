#!/usr/bin/env python

import cv2 as cv

def main():
    cap = cv.VideoCapture(0)  # Open default camera (index 0)

    if not cap.isOpened():
        print("Error: Unable to open camera")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Unable to capture frame")
            break

        cv.imshow('Camera Feed', frame)

        # Check for key press
        key = cv.waitKey(1)
        if key == ord('q'):  # Quit when 'q' is pressed
            break

    cap.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()
