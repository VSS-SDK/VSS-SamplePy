from .ball import Ball

class State():
    ball = None
    team_blue = None
    team_yellow = None

    def __init__(self, ball=Ball(), team_blue=list(), team_yellow=list()):
        self.ball = ball
        self.team_blue = team_blue
        self.team_yellow = team_yellow
