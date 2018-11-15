import sys

sys.path.insert(1, 'protos')
sys.path.insert(1, 'domain')

from command_pb2 import Global_Commands
from command import Command

class CommandSender():
    def create_socket(self):
        return 0

    def send_command(self, command=Command()):
        return 0    