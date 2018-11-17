import zmq
import google.protobuf.text_format

from protos.debug_pb2 import Global_Debug
from domain.debug import Debug
from helpers.debug_mapper import DebugMapper

class DebugSender():
    context = None
    socket = None

    def create_socket(self, port=5558):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PAIR)
        self.socket.connect("tcp://localhost:{:d}".format(port))

    def send_debug(self, debug=Debug()):
        global_debug = DebugMapper.debug_to_global_debug(debug)
        
        serialized = global_debug.SerializeToString()
        self.socket.send(serialized)

        return 0      