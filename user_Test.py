import unittest # Importing the unittest module
from user import User # Importing the contact class
class TestUser(unittest.TestCase):



       def setUp(self):
        '''
        method to run before each test
        '''
        self.new_user=User("dukelemayian", "lemayian1005") #new User created
