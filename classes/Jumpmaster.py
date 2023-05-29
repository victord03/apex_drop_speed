
class JumpMaster:
    direction: float  # 1 represents entirely horizontally; 0 entirely vertically
    speed: int

    def __init__(self):
        self.direction = 0.0
        self.speed = 0

    def set_direction(self, direction: float):
        self.direction = direction

    def set_speed(self):
        """min speed 9, max speed 12 (30% increase from min to max)"""

        speed = int()

        if 0.0 <= self.direction <= 0.33:
            speed = 12
        elif 0.33 < self.direction <= 0.66:
            speed = 10
        elif 0.66 < self.direction <= 1.0:
            speed = 9

        self.speed = speed

