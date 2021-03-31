import unittest 
from dotenv_manager.Data import Data

class test_Data(unittest.TestCase):

    def test_not_exists_environment_group(self):

        data = Data()

        environmentGroupName = "my_environment"
        existsGroup = data.environmentGroup(environmentGroupName).exists()
        self.assertFalse(existsGroup)

    def test_save_environment_group(self):

        data = Data()
        
        environmentGroupName = "my_environment"
        data.environmentGroup(environmentGroupName).save()
        existsGroup = data.environmentGroup(environmentGroupName).exists()
        self.assertTrue(existsGroup)
