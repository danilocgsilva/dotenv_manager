import sys
from dotenv_manager.Interactor import Interactor
from dotenv_manager.Tasks import Tasks
from danilocgsilvame_python_helpers.DcgsPythonHelpers import DcgsPythonHelpers

def main():

    interactor = Interactor()
    if not interactor.argument:
        Tasks().zeroOrder()
        exit()
    
    pHelpers = DcgsPythonHelpers()
    argumentsparsed = pHelpers.command_line_argument_names('command', 'c', 'template', 't')
    print("The command was " + argumentsparsed.command + " and the template was " + argumentsparsed.template)

