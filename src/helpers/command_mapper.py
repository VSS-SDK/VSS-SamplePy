from domain.command import Command
from domain.wheels_command import WheelsCommand
from protos.command_pb2 import Global_Commands
from protos.command_pb2 import Robot_Command

class CommandMapper():
    @classmethod
    def command_to_global_commands(self, command=Command()):
        global_commands = Global_Commands()

        for i in range(0, 3):
            robot_command = self.__get_robot_command(command.commands[i])

            global_commands.robot_commands.add()  
            global_commands.robot_commands[i].left_vel = robot_command.left_vel
            global_commands.robot_commands[i].right_vel = robot_command.right_vel

        return global_commands

    @classmethod
    def __get_robot_command(self, wheels_command):
        robot_command = Robot_Command()

        robot_command.left_vel = wheels_command.left_vel
        robot_command.right_vel = wheels_command.right_vel

        return robot_command