from domain.point import Point

class Pose(Point):
    angle = 0.0

    def __init__(self, x=0.0, y=0.0, angle=0.0):
        self.x = x
        self.y = y
        self.angle = angle
