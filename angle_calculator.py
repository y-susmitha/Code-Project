import math


class AngleCalculator:

    def __init__(self):
        pass

    def calculate_angle(self, point1, point2, point3):
        """
        Calculate the angle at point2.

        point1 = first landmark
        point2 = middle/joint landmark
        point3 = third landmark

        Example for bicep curl:
        point1 = shoulder
        point2 = elbow
        point3 = wrist

        Returns:
            angle in degrees
        """

        # Vector from point2 to point1
        vector1 = (
            point1[0] - point2[0],
            point1[1] - point2[1]
        )

        # Vector from point2 to point3
        vector2 = (
            point3[0] - point2[0],
            point3[1] - point2[1]
        )

        # Dot product
        dot_product = (
            vector1[0] * vector2[0] +
            vector1[1] * vector2[1]
        )

        # Magnitudes
        magnitude1 = math.sqrt(
            vector1[0] ** 2 +
            vector1[1] ** 2
        )

        magnitude2 = math.sqrt(
            vector2[0] ** 2 +
            vector2[1] ** 2
        )

        # Avoid division by zero
        if magnitude1 == 0 or magnitude2 == 0:
            return 0.0

        # Calculate cosine of angle
        cosine_angle = dot_product / (
            magnitude1 * magnitude2
        )

        # Prevent numerical errors
        cosine_angle = max(
            -1.0,
            min(1.0, cosine_angle)
        )

        # Calculate angle
        angle = math.degrees(
            math.acos(cosine_angle)
        )

        return angle


# -------------------------------------------------
# Test the angle calculator
# -------------------------------------------------

if __name__ == "__main__":

    calculator = AngleCalculator()

    # Example:
    # Shoulder = (100, 100)
    # Elbow    = (100, 200)
    # Wrist    = (200, 200)

    shoulder = (100, 100)
    elbow = (100, 200)
    wrist = (200, 200)

    angle = calculator.calculate_angle(
        shoulder,
        elbow,
        wrist
    )

    print("Calculated angle:", round(angle, 2), "degrees")
```
