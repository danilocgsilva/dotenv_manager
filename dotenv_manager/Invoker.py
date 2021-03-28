class Invoker:

    def __init__(self, userCommand: str):
        self.userCommand = userCommand

    def execute(self):
        print(self.userCommand)
