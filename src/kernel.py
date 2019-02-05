import vsscorepy

from vsscorepy.communications.command_sender import CommandSender
from vsscorepy.communications.debug_sender import DebugSender
from vsscorepy.communications.state_receiver import StateReceiver
from vsscorepy.domain.command import Command
from vsscorepy.domain.wheels_command import WheelsCommand
from vsscorepy.domain.point import Point
from vsscorepy.domain.pose import Pose
from vsscorepy.domain.debug import Debug


class Kernel(object):
    state_receiver = None
    command_sender = None
    debug_sender = None

    def loop(self):
        self.state_receiver = StateReceiver()
        self.state_receiver.create_socket()

        self.command_sender = CommandSender()
        self.command_sender.create_socket()

        self.debug_sender = DebugSender()
        self.debug_sender.create_socket()

        while True:
            state = self.state_receiver.receive_state()
            self.command_sender.send_command(self.__build_command())
            self.debug_sender.send_debug(self.__build_debug(state))

    def __build_command(self):
        command = Command()

        command.wheels_commands.append(WheelsCommand(10, -10))
        command.wheels_commands.append(WheelsCommand(10, -10))
        command.wheels_commands.append(WheelsCommand(10, -10))

        return command

    def __build_debug(self, state):
        debug = Debug()
        debug.clean()

        for robot in state.team_yellow:
            debug.step_points.append(Point(robot.x + 10, robot.y + 10))
            debug.final_poses.append(Pose(state.ball.x + 10, state.ball.y + 10, 10))

        return debug
