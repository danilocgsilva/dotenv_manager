import unittest 
from dotenv_manager.Data import Data

class test_Data(unittest.TestCase):

    def test_exception_empty_environment_group(self):

        data = Data()
        environmentGroupName = "my_environment"
        data.environmentGroup(environmentGroupName)
