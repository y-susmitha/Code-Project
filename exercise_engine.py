class ExerciseEngine:

    def __init__(self, config):

        self.config = config

        self.state = config["rep"]["start"]

        self.reps = 0

    def update(self, knee):

        if self.state == "UP":

            if knee < 90:

                self.state = "DOWN"

        elif self.state == "DOWN":

            if knee > 160:

                self.state = "UP"

                self.reps += 1

        return self.reps
