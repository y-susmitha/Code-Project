"""
rep_counter.py
Generic repetition counter
"""

class RepCounter:

    def __init__(self, config):

        self.config = config

        self.up_angle = config["thresholds"]["up_angle"]
        self.down_angle = config["thresholds"]["down_angle"]

        self.stage = "UP"

        self.reps = 0

    def update(self, angle):

        if angle > self.up_angle:

            if self.stage == "DOWN":

                self.stage = "UP"

                self.reps += 1

        elif angle < self.down_angle:

            self.stage = "DOWN"

        return self.reps, self.stage