import sys

sys.path.insert(1, 'protos')
sys.path.insert(1, 'debug')

from state_pb2 import Global_State
from state import State

class StateReceiver():
    def create_socket(self):
        return 0

    def receive_state(self):
        return State() 