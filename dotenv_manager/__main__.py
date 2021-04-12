import sys
from dotenv_manager.Interactor import Interactor
from dotenv_manager.Tasks import Tasks
from danilocgsilvame_python_helpers.DcgsPythonHelpers import DcgsPythonHelpers

def main():

    tasks = Tasks()

    interactor = Interactor()
    if not interactor.argument:
        tasks.zeroOrder()
        exit()
    
    pHelpers = DcgsPythonHelpers()
    argumentsparsed = pHelpers.command_line_argument_names('command', 'c', 'template', 't', 'manage', 'm')
    tasks.process(argumentsparsed)

