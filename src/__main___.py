import time
import sys

sys.path.insert(1, 'communications')

from command_sender import CommandSender
from debug_sender import DebugSender
from state_receiver import StateReceiver

def main():
	state_receiver = StateReceiver()
	state_receiver.create_socket()

	while True:
		state = state_receiver.receive_state()
		# build and send command
		# build and send debug


if __name__ == "__main__":
    # execute only if run as a script
    main()

