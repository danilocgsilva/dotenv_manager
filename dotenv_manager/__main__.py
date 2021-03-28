import sys
from dotenv_manager.Interactor import Interactor
from dotenv_manager.Commands import Commands
from dotenv_manager.CommandsException import CommandsException
from dotenv_manager.Tasks import Tasks

def main():

    interactor = Interactor()
    try:
        commands = Commands(interactor.argument)
    except CommandsException:
        Tasks().zeroOrder()
