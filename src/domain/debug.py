class Debug():
    step_points = None
    final_poses = None
    paths = None

    def __init__(self, step_points=list(), final_poses=list(), paths=list()):
        self.step_points = step_points
        self.final_poses = final_poses
        self.paths = paths