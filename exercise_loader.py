import yaml


class ExerciseLoader:

    def __init__(self, file):

        self.file = file

    def load(self):

        with open(self.file, "r") as f:

            return yaml.safe_load(f)
