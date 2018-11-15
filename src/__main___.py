import time
import sys

sys.path.insert(0, 'communications/')

from command_sender import CommandSender
from debug_sender import DebugSender
from state_receiver import StateReceiver

def main():
    while True:
        time.sleep(5)
        print("teste")


if __name__ == "__main__":
    # execute only if run as a script
    main()

