from exercise_loader import ExerciseLoader
from feedback_engine import FeedbackEngine


# Load YAML configuration
loader = ExerciseLoader("config/bicep_curl.yaml")
config = loader.load()


# Create feedback engine
feedback = FeedbackEngine(config)


# Test feedback messages
print("DOWN :", feedback.get_feedback("DOWN"))
print("UP :", feedback.get_feedback("UP"))
print("TOO_FAST :", feedback.get_feedback("TOO_FAST"))
print("TOO_SLOW :", feedback.get_feedback("TOO_SLOW"))