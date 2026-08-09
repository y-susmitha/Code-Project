from exercise_loader import ExerciseLoader
from exercise_engine import ExerciseEngine
from calibration import Calibration

# -----------------------------
# Load Exercise
# -----------------------------
loader = ExerciseLoader("config/squat.yaml")

config = loader.load()

print(config)

# -----------------------------
# Calibration
# -----------------------------
cal = Calibration()

for i in range(100):

    cal.add(170)

baseline = cal.compute()

print("Calibration")

print(baseline)

# -----------------------------
# Exercise Engine
# -----------------------------
engine = ExerciseEngine(config)

angles = [

170,
165,
150,
120,
90,
70,
60,
70,
90,
120,
150,
170,

170,
150,
80,
70,
90,
170

]

for angle in angles:

    reps = engine.update(angle)

    print("Angle =", angle, " Reps =", reps)
