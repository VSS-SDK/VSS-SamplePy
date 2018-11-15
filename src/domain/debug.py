class Debug():
    step_points = list()
    final_poses = list()
    paths = list()

    def __init__(self, step_points=list(), final_poses=list(), paths=list()):
        self.step_points = step_points
        self.final_poses = final_poses
        self.paths = paths

    def clean(self):
        self.step_points = list()
        self.final_poses = list()
        self.paths = list()