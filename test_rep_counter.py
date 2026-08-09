from exercise_loader import ExerciseLoader
from rep_counter import RepCounter

loader = ExerciseLoader("config/bicep_curl.yaml")
config = loader.load()

counter = RepCounter(config)

angles = [170,165,150,120,90,45,90,120,160,170]

for angle in angles:

    reps, stage = counter.update(angle)

    print("Angle:", angle,
          " Stage:", stage,
          " Reps:", reps)