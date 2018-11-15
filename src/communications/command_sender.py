import zmq
import sys
import google.protobuf.text_format

sys.path.insert(1, 'protos')
sys.path.insert(1, 'domain')

from command_pb2 import Global_Commands
from command import Command

class CommandSender():
    context = None
    socket = None

    def create_socket(self, port=5556):
        context = zmq.Context()
        socket = context.socket(zmq.PAIR)
        self.socket.connect(f"tcp://localhost:{port}")

        return 0

    def send_command(self, command=Command()):
        return 0    