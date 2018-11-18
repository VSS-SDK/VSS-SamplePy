import vsscorepy

from vsscorepy.communications.command_sender import CommandSender
from vsscorepy.communications.debug_sender import DebugSender
from vsscorepy.communications.state_receiver import StateReceiver
from vsscorepy.domain.command import Command
from vsscorepy.domain.wheels_command import WheelsCommand
from vsscorepy.domain.point import Point
from vsscorepy.domain.pose import Pose
from vsscorepy.domain.debug import Debug

def main():
	state_receiver = StateReceiver()
	state_receiver.create_socket()

	command_sender = CommandSender()
	command_sender.create_socket()

	debug_sender = DebugSender()
	debug_sender.create_socket()

	while True:
		state = state_receiver.receive_state()
		command_sender.send_command(build_command())
		debug_sender.send_debug(build_debug(state))


def build_command():
	command = Command()

	command.commands.append(WheelsCommand(10, -10))
	command.commands.append(WheelsCommand(10, -10))
	command.commands.append(WheelsCommand(10, -10))

	return command


def build_debug(state):
	debug = Debug()
	debug.clean()

	for robot in state.team_yellow:
		debug.step_points.append(Point(robot.x + 10, robot.y + 10))
		debug.final_poses.append(Pose(state.ball.x + 10, state.ball.y + 10, 10))

	return debug


if __name__ == "__main__":
    # execute only if run as a script
    main()