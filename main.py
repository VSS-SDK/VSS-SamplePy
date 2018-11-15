from src.communications.command_sender import CommandSender
#from src.communications.debug_sender import DebugSender
from src.communications.state_receiver import StateReceiver
from src.domain.command import Command
from src.domain.wheels_command import WheelsCommand

def main():
	state_receiver = StateReceiver()
	state_receiver.create_socket()

	command_sender = CommandSender()
	command_sender.create_socket()

	#debug_sender = DebugSender()
	#debug_sender.create_socket()

	while True:
		state = state_receiver.receive_state()
		command_sender.send_command(build_command())
		#debug_sender.send_debug(build_debug())


def build_command():
	command = Command()

	command.commands.append(WheelsCommand(10, -10))
	command.commands.append(WheelsCommand(10, -10))
	command.commands.append(WheelsCommand(10, -10))

	return command


def build_debug():
	return Debug()


if __name__ == "__main__":
    # execute only if run as a script
    main()