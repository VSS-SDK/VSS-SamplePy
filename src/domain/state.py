from domain.ball import Ball

class State():
    ball = Ball()
    team_blue = list()
    team_yellow = list()

    def __init__(self, ball=Ball(), team_blue=list(), team_yellow=list()):
        self.ball = ball
        self.team_blue = team_blue
        self.team_yellow = team_yellow

    def clean(self):
        self.ball = Ball()
        self.team_blue = list()
        self.team_yellow = list()