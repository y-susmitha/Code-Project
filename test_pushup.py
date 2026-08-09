import yaml

# Open the YAML configuration file
with open("config/pushup.yaml", "r") as f:
    config = yaml.safe_load(f)

# Display the complete configuration
print(config)

print("\nExercise Information")
print("--------------------")
print("Exercise :", config["name"])
print("Type     :", config["exercise_type"])
print("Joint    :", config["joint"])
print("Side     :", config["side"])

print("\nThresholds")
print("--------------------")
print("Up Angle   :", config["thresholds"]["up_angle"])
print("Down Angle :", config["thresholds"]["down_angle"])

print("\nLandmarks")
print("--------------------")
print("Shoulder :", config["landmarks"]["shoulder"])
print("Elbow    :", config["landmarks"]["elbow"])
print("Wrist    :", config["landmarks"]["wrist"])
