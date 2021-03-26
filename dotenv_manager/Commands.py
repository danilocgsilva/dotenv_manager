from dotenv_manager.CommandsException import CommandsException

class Commands:

    def __init__(self, command: str):
        if command == None:
            raise CommandsException("No order send.")
        self.command = command
