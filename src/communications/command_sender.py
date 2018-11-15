import zmq

import google.protobuf.text_format

from src.protos.command_pb2 import Global_Commands
# from command_pb2 import Global_Commands
from src.domain.command import Command

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