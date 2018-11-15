# from src.communications.command_sender import CommandSender
# from src.communications.debug_sender import DebugSender
from src.communications.state_receiver import StateReceiver


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