import zmq
import google.protobuf.text_format

from protos.state_pb2 import Global_State
from domain.state import State
from helpers.state_mapper import StateMapper

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

        state = StateMapper.global_state_to_state(global_state)

        return state