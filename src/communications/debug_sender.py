import zmq
import google.protobuf.text_format

from src.protos.debug_pb2 import Global_Debug
from src.domain.debug import Debug

class DebugSender():
    context = None
    socket = None

    def create_socket(self, port=5558):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PAIR)
        self.socket.connect("tcp://localhost:{:d}".format(port))

    def send_debug(self, debug=Debug()):
        return 0    