import zmq
import google.protobuf.text_format

from src.protos.command_pb2 import Global_Commands
from src.domain.command import Command
from src.helpers.command_mapper import CommandMapper

class CommandSender():
    context = None
    socket = None

    def create_socket(self, port=5556):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PAIR)
        self.socket.connect("tcp://localhost:{:d}".format(port))

    def send_command(self, command=Command()):
        global_commands = CommandMapper.command_to_global_commands(command)
        
        serialized = global_commands.SerializeToString()
        self.socket.send(serialized)

        return 0    