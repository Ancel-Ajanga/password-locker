###########CLASS USER#########
class User:
    '''
    Class that generates new instances of user
    '''
    user_list = []  # list of users to be stored here

    def __init__(self, username, password):
        '''
        saving user credentials into user_list for login
        '''
        self.username = username
        self.password = password

#########save multiple users#########