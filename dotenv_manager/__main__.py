import sys
from dotenv_manager.Interactor import Interactor
from dotenv_manager.Invoker import Invoker
from dotenv_manager.Tasks import Tasks

def main():

    interactor = Interactor()
    if not interactor.argument:
        Tasks().zeroOrder()
        exit()
    
    invoker = Invoker(interactor.argument)
    invoker.execute()

