import cv2
import mediapipe as mp
import time

# -----------------------------
# Initialize MediaPipe Pose
# -----------------------------
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

pose = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=1,
    smooth_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# -----------------------------
# Open Webcam
# -----------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

previous_time = 0

while True:

    success, frame = cap.read()

    if not success:
        break

    # Flip image horizontally
    frame = cv2.flip(frame, 1)

    # Convert BGR to RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Pose estimation
    results = pose.process(rgb)

    # Draw landmarks
    if results.pose_landmarks:

        mp_drawing.draw_landmarks(
            frame,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(
                color=(0,255,0),
                thickness=2,
                circle_radius=3
            ),
            mp_drawing.DrawingSpec(
                color=(255,0,0),
                thickness=2
            )
        )

        # Print landmark coordinates
        h, w, _ = frame.shape

        for idx, lm in enumerate(results.pose_landmarks.landmark):

            x = int(lm.x * w)
            y = int(lm.y * h)

            cv2.putText(
                frame,
                str(idx),
                (x, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.4,
                (0,255,255),
                1
            )

    # FPS Calculation
    current_time = time.time()
    fps = 1 / (current_time - previous_time) if previous_time else 0
    previous_time = current_time

    cv2.putText(
        frame,
        f"FPS: {int(fps)}",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,0,255),
        2
    )

    cv2.imshow("Live Pose Detection", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
