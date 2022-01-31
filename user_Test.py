import unittest # Importing the unittest module
from user import User # Importing the contact class
class TestUser(unittest.TestCase):



       def setUp(self):
        '''
        method to run before each test
        '''
        self.new_user=User("dukelemayian", "lemayian1005") #new User created

       def tearDown(self):
        '''
        clean up after each test to prevent errors
        '''
        User.user_list = []

