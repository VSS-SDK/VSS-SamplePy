import sys

sys.path.insert(1, 'protos')

from state_pb2 import Global_State


class StateReceiver():
    def create_socket(self):
        return 0

    def send_debug(self):
        return 0    