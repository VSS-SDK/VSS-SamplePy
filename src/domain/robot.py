from domain.pose import Pose

class Robot(Pose):
    speed_x = 0.0
    speed_y = 0.0
    speed_angle = 0.0

    def __init__(self, x=0.0, y=0.0, angle=0.0, speed_x=0.0, speed_y=0.0, speed_angle=0.0):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.speed_angle = speed_angle
