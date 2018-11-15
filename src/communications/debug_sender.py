import zmq
import sys
import google.protobuf.text_format

sys.path.insert(1, 'protos')
sys.path.insert(1, 'domain')

from debug_pb2 import Global_Debug
from debug import Debug

class DebugSender():
    context = None
    socket = None

    def create_socket(self, port=5558):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PAIR)
        self.socket.connect(f"tcp://localhost:{port}")

    def send_debug(self, debug=Debug()):
        return 0    