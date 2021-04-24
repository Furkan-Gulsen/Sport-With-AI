import cv2
import mediapipe as mp
import numpy as np
import pandas as pd
from utils import *
from body_part_angle import BodyPartAngle

# drawing your body
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(0)
## Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5,
                  min_tracking_confidence=0.5) as pose:
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

        landmarks = results.pose_landmarks.landmark

        # Get coordinates
        shoulder = detection_body_part(landmarks, "LEFT_SHOULDER")
        elbow = detection_body_part(landmarks, "LEFT_ELBOW")
        wrist = detection_body_part(landmarks, "LEFT_WRIST")

        # Calculate angle
        angle = calculate_angle(shoulder, elbow, wrist)
        # left_arm = BodyPartAngle(landmarks).angle_of_the_left_arm()

        cv2.putText(image, str(left_arm),
                    tuple(np.multiply(elbow, [640, 480]).astype(int)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2,
                    cv2.LINE_AA)

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
