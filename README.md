# Sport With AI

> The human body is detected with the help of the [Pose Estimation](https://github.com/google/mediapipe) library. Then, using the mathematical methods applied, it is determined how much the exercise movement is done.

## Sit-Up Exercise
![Sit-Up](https://github.com/Furkan-Gulsen/Sport-With-AI/blob/main/output/output%20sit-up.gif)

The sit-up is an abdominal endurance training exercise to strengthen, tighten and tone the abdominal muscles. It is similar to a crunch, but sit-ups have a fuller range of motion and condition additional muscles.
```
python main.py -t sit-up -vs videos/sit-up.mp4
```


## Pull-Up Exercise
![Pull-Up](https://github.com/Furkan-Gulsen/Sport-With-AI/blob/main/output/output%20pull-up.gif?raw=true)

A pull-up is an upper-body strength exercise. The pull-up is a closed-chain movement where the body is suspended by the hands and pulls up. As this happens, the elbows flex and the shoulders adduct and extend to bring the elbows to the torso.
```
python main.py -t pull-up -vs videos/pull-up.mp4
```


## Push-Up Exercise
![Push-Up](https://github.com/Furkan-Gulsen/Sport-With-AI/blob/main/output/output%20push-up.gif?raw=true)

A push-up is a common calisthenics exercise beginning from the prone position. By raising and lowering the body using the arms, push-ups exercise the pectoral muscles, triceps, and anterior deltoids, with ancillary benefits to the rest of the deltoids, serratus anterior, coracobrachialis and the midsection as a whole. 
```
python main.py -t push-up -vs videos/push-up.mp4
```


## Squat Exercise
![Squat](https://github.com/Furkan-Gulsen/Sport-With-AI/blob/main/output/output%20squat.gif)

A squat is a strength exercise in which the trainee lowers their hips from a standing position and then stands back up. During the descent of a squat, the hip and knee joints flex while the ankle joint dorsiflexes; conversely the hip and knee joints extend and the ankle joint plantarflexes when standing up.
```
python main.py -t squat -vs videos/squat.mp4
```


## Walking Exercise
![Walking](https://github.com/Furkan-Gulsen/Sport-With-AI/blob/main/output/output%20walking%20exercise.gif)
```
python main.py -t walk -vs videos/walk.mp4
```

---

If you want to detect your movements live with your webcam, you can run the code line below.
```
python main.py -t sit-up
# or python main.py -t pull-up
# or python main.py -t push-up
# or python main.py -t squat
# or python main.py -t walk
```
