class Command:
    commands = list()

    def __init__(self, commands=list()):
        self.commands = commands

    def clean(self):
        self.commands = list()