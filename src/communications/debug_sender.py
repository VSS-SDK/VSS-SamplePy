import sys

sys.path.insert(1, 'protos')
sys.path.insert(1, 'domain')

from debug_pb2 import Global_Debug
from debug import Debug

class DebugSender():
    def create_socket(self):
        return 0

    def send_debug(self, debug=Debug()):
        return 0    