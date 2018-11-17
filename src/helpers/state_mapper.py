from domain.state import State
from domain.ball import Ball
from domain.robot import Robot
from protos.state_pb2 import Global_State

class StateMapper():
    @classmethod
    def global_state_to_state(self, global_state=Global_State()):
        state = State()

        state.ball = self.__get_ball(global_state)
        state.team_blue = self.__get_team_blue(global_state)
        state.team_yellow = self.__get_team_yellow(global_state)

        return state

    @classmethod
    def __get_ball(self, global_state):
        ball_state = global_state.balls[0]
        ball_pose = ball_state.pose
        ball_v_pose = ball_state.v_pose

        ball = Ball(ball_pose.x, ball_pose.y, ball_v_pose.x, ball_v_pose.y)
        return ball

    @classmethod
    def __get_team_blue(self, global_state):
        team_blue = list()

        robots = global_state.robots_blue

        for robot_state in robots:
            team_blue.append(self.__get_robot(robot_state))

        return team_blue

    @classmethod
    def __get_team_yellow(self, global_state):
        team_yellow = list()

        robots = global_state.robots_yellow

        for robot_state in robots:
            team_yellow.append(self.__get_robot(robot_state))

        return team_yellow

    @classmethod
    def __get_robot(self, robot_state):
        robot_pose = robot_state.pose
        robot_v_pose = robot_state.v_pose

        return Robot(robot_pose.x, robot_pose.y, robot_pose.yaw, robot_v_pose.x, robot_v_pose.y, robot_v_pose.yaw)