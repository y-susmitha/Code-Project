import numpy as np


class Calibration:

    def __init__(self):

        self.samples = []

    def add(self, angle):

        self.samples.append(angle)

    def complete(self):

        return len(self.samples) >= 100

    def compute(self):

        return {

            "mean": np.mean(self.samples),

            "std": np.std(self.samples)

        }
