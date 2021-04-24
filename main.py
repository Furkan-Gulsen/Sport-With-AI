## import packages
import cv2
import argparse
from utils import *
import mediapipe as mp
from body_part_angle import BodyPartAngle
from types_of_exercise import TypeOfExercise

## setup agrparse
ap = argparse.ArgumentParser()
ap.add_argument("-t",
                "--exercise_type",
                type=str,
                help='Type of activity to do',
                required=True)
ap.add_argument("-vs",
                "--video_source",
                type=str,
                help='Type of activity to do',
                required=False)
args = vars(ap.parse_args())

## drawing body
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

## setting the video source
if args["video_source"] is not None:
    cap = cv2.VideoCapture(args["video_source"])
else:
    cap = cv2.VideoCapture(0)  # webcam

cap.set(3, 800)  # width
cap.set(4, 480)  # height

## setup mediapipe
with mp_pose.Pose(min_detection_confidence=0.5,
                  min_tracking_confidence=0.5) as pose:

    counter = 0  # movement of exercise
    status = True  # state of move
    while cap.isOpened():
        ret, frame = cap.read()
        frame = cv2.resize(frame, (800, 480), interpolation=cv2.INTER_AREA)
        ## recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        ## make detection
        results = pose.process(image)
        ## recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        try:
            landmarks = results.pose_landmarks.landmark
            if args["exercise_type"] == "push-up":
                counter, status = TypeOfExercise(landmarks).push_up(
                    counter, status)
            elif args["exercise_type"] == "pull-up":
                counter, status = TypeOfExercise(landmarks).pull_up(
                    counter, status)
            elif args["exercise_type"] == "squat":
                counter, status = TypeOfExercise(landmarks).squat(
                    counter, status)
            elif args["exercise_type"] == "walk":
                counter, status = TypeOfExercise(landmarks).walk(
                    counter, status)
            elif args["exercise_type"] == "sit-up":
                counter, status = TypeOfExercise(landmarks).sit_up(
                    counter, status)

        except:
            pass

        cv2.putText(image,
                    "Status: " + str(status) + " / Counter: " + str(counter),
                    (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (174, 139, 45),
                    2, cv2.LINE_AA)

        ## render detections (for landmarks)
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(255, 255, 255),
                                   thickness=2,
                                   circle_radius=2),
            mp_drawing.DrawingSpec(color=(174, 139, 45),
                                   thickness=2,
                                   circle_radius=2),
        )

        cv2.imshow('Mediapipe Feed', image)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
