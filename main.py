import cv2
import mediapipe as mp
import numpy as np
import pandas as pd
from utils import *
from body_part_angle import BodyPartAngle
from types_of_exercise import TypeOfExercise

# drawing your body
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture("push-up.mp4")
## Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5,
                  min_tracking_confidence=0.5) as pose:

    counter = 0
    status = True
    while cap.isOpened():
        ret, frame = cap.read()

        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Make detection
        results = pose.process(image)

        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        try:
            landmarks = results.pose_landmarks.landmark
            # push up
            counter, status = TypeOfExercise(landmarks).push_up(
                counter, status)

            cv2.putText(
                image, "Status: " + str(status) + "/ counter: " + str(counter),
                (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2,
                cv2.LINE_AA)
        except:
            pass

        # Render detections
        mp_drawing.draw_landmarks(
            image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(245, 117, 66),
                                   thickness=2,
                                   circle_radius=2),
            mp_drawing.DrawingSpec(color=(245, 66, 230),
                                   thickness=2,
                                   circle_radius=2))

        cv2.imshow('Mediapipe Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
