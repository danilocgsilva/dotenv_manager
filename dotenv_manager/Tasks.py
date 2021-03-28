class Tasks:

    def zeroOrder(self):
        message = """
The demanager script needs some parameters to work...

Here are some ways to user the script:

(to be implemented)
demanager -m :
List all environment variables groups

(to be implemented)
demanager -m <groupenvironment>
List all variables from <groupenvironment>

(to be implementd)
demanager -m <groupenvironment>:<SOMEVARIABLE>
Prints the variable value from <SOMEVARIABLE> that belongs to the variable group <groupenvironment>

(to be implemented)
demanager -m <groupenvironment>:<SOMEVARIABLE> <VALUE>
Sets the <VALUE> to the <SOMEVARIABLE> belonging to <groupenvironment>

(to be implemented)
demanager -m <groupenvironment> -f <file_path>
Creates an <groupenvironment> using the <file_path> values

(to be implemented)
demanager -m <groupenvironment> -t <file_path>
Creates a variable template, may some variables needed for some kind of project that will require run in different environments with the same variables changed
"""
        print(message)
