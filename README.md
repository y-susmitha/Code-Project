1\. Live Pose Estimation



live\_pose.py is responsible for obtaining video frames from the webcam and detecting human body landmarks using MediaPipe Pose.



The system detects body landmarks such as:



Nose

Shoulder

Elbow

Wrist

Hip

Knee

Ankle



For example, MediaPipe landmark numbers used for a right-arm bicep curl are:



Shoulder = 12

Elbow    = 14

Wrist    = 16

2\. Angle Calculator



angle\_calculator.py calculates the angle between three body landmarks.



For a bicep curl:



Shoulder

&#x20;   \\

&#x20;    \\

&#x20;    Elbow

&#x20;      \\

&#x20;       \\

&#x20;       Wrist



The elbow angle is calculated using:



Shoulder → Elbow → Wrist



The angle is returned in degrees.



Example:



angle = calculator.calculate\_angle(

&#x20;   shoulder,

&#x20;   elbow,

&#x20;   wrist

)

3\. Calibration



calibration.py is used to determine a user's normal starting position and movement range.



Calibration can collect multiple angle measurements and calculate:



Mean angle

Standard deviation



Example:



Mean = 170°

Standard deviation = 3°



These values can be used to adapt exercise detection to different users.



4\. Generic Exercise Engine



exercise\_engine.py provides the common logic for different exercises.



Instead of creating a separate program for every exercise, the engine loads exercise-specific parameters from YAML configuration files.



For example:



bicep\_curl.yaml

pushup.yaml

squat.yaml



This makes the system configurable and reusable.



5\. Exercise Configuration



Exercise-specific parameters are stored in the config directory.



Example:



config/

│

├── bicep\_curl.yaml

├── pushup.yaml

└── squat.yaml



A bicep curl configuration contains information such as:



name: Bicep Curl



exercise\_type: upper\_body



joint: elbow



side: right



Landmarks:



landmarks:



&#x20; shoulder: 12



&#x20; elbow: 14



&#x20; wrist: 16



Thresholds:



thresholds:



&#x20; down\_angle: 165



&#x20; up\_angle: 45

6\. Repetition Counter



rep\_counter.py detects exercise repetitions based on the joint angle and exercise state.



For example, a bicep curl can use:



Arm extended

&#x20;    ↓

DOWN

&#x20;    ↓

Arm curled

&#x20;    ↓

UP

&#x20;    ↓

Arm extended

&#x20;    ↓

One repetition



Example output:



Angle: 170°

Stage: DOWN

Reps: 0



Angle: 45°

Stage: UP

Reps: 0



Angle: 170°

Stage: DOWN

Reps: 1

7\. Feedback Engine



feedback\_engine.py generates real-time instructions for the user.



Example feedback:



Excellent Curl

Lower Completely

Slow Down

Lift Smoothly



The feedback is based on the current exercise state and movement characteristics.



8\. Supported Exercises



The system can be configured for different exercises.



Currently planned:



Bicep Curl



Main joint:



Elbow



Landmarks:



Shoulder → Elbow → Wrist

Push-up



Possible measurement:



Shoulder → Elbow → Wrist



and/or



Shoulder → Hip → Knee

Squat



Main measurement:



Hip → Knee → Ankle



The exercise-specific thresholds are stored in YAML files.



9\. Requirements



The project requires Python and the following packages:



numpy

pyyaml

opencv-python

mediapipe



Install the requirements using:



python -m pip install -r requirements.txt



If multiple Python versions are installed, use the intended Python interpreter explicitly.



For example:



C:\\ProgramData\\anaconda3\\python.exe -m pip install -r requirements.txt

10\. Running the Project



Open PowerShell.



Go to the project directory:



cd C:\\Users\\sushm\\Downloads\\exercise



Check the files:



dir



Run the main program:



python main.py



Alternatively, explicitly specify the Python interpreter:



C:\\ProgramData\\anaconda3\\python.exe main.py

11\. Testing Angle Calculator



Run:



python angle\_calculator.py



Expected output:



Calculated angle: 90.0 degrees

12\. Testing MediaPipe



Run:



python live\_pose.py



If the webcam opens, the system should display the detected human pose.



Press:



Q



to close the webcam window.



13\. Testing the Rep Counter



The repetition counter can be tested using predefined angles.



Example:



170

165

150

120

90

75

90

120

160

170



The program should identify changes between exercise states and count repetitions.



14\. Example Bicep Curl



The processing pipeline is:



Webcam

&#x20;  ↓

MediaPipe

&#x20;  ↓

Shoulder = 12

Elbow = 14

Wrist = 16

&#x20;  ↓

Calculate elbow angle

&#x20;  ↓

Compare angle with thresholds

&#x20;  ↓

Determine DOWN / UP

&#x20;  ↓

Count repetition

&#x20;  ↓

Generate feedback



Example:



Elbow Angle: 170°

Stage: DOWN

Reps: 0

Feedback: Lower Completely



After completing one repetition:



Elbow Angle: 170°

Stage: DOWN

Reps: 1

Feedback: Excellent Curl

15\. PowerShell Commands

Navigate to project

cd C:\\Users\\sushm\\Downloads\\exercise

Display files

dir

Display configuration files

dir config

Display YAML configuration

Get-Content .\\config\\bicep\_curl.yaml

Run angle calculator

python angle\_calculator.py

Run live pose estimation

python live\_pose.py

Run complete application

python main.py

16\. Development Sequence



The recommended development order is:



Step 1

Create project structure

&#x20;       ↓

Step 2

Test Angle Calculator

&#x20;       ↓

Step 3

Test MediaPipe Pose

&#x20;       ↓

Step 4

Connect MediaPipe landmarks

&#x20;       ↓

Step 5

Calculate joint angles

&#x20;       ↓

Step 6

Implement calibration

&#x20;       ↓

Step 7

Implement repetition counter

&#x20;       ↓

Step 8

Implement feedback engine

&#x20;       ↓

Step 9

Load YAML exercise configuration

&#x20;       ↓

Step 10

Run complete exercise engine

17\. Future Improvements



The system can be extended with:



Multiple exercise recognition

Left/right-side exercise detection

Automatic exercise selection

Personalized calibration

Movement-speed estimation

Posture correction

Audio feedback

Exercise scoring

Workout history

GUI dashboard

Repetition history

Performance analytics

Mobile application integration

