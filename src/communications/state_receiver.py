import zmq
import sys
import google.protobuf.text_format
import base64

sys.path.insert(1, 'protos')
sys.path.insert(1, 'debug')

from state_pb2 import Global_State
from state import State

class StateReceiver():
    context = None
    socket = None

    def create_socket(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.SUB)
        self.socket.connect("tcp://localhost:5555")
        self.socket.setsockopt(zmq.SUBSCRIBE, b"")

    def receive_state(self):
        byte_array = self.socket.recv()
        global_state = Global_State()
        global_state.ParseFromString(byte_array)
        return 0