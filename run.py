#!/usr/bin/env python3.6
from credentials import Credentials
from user import User
import random

#user 
####crate account####
def create_useraccount(username, password):
    '''
    method creates a user account
    '''
    new_user = User(username, password)
    return new_user

     ######save user#####
def save_user(user):
    '''
    method save user  account
    '''
    user.save_user()

def save_credentials(credentials):

    '''
    method save credentials  account
    '''

    credentials.save_credentials


 ######search user########

def find_user(username):
    '''
    method for find user using username
    '''
    return User.find_user(username)

    # create credentials####
def create_credentials(account, email, passlock):
    '''
    method credentials details
    '''
    new_cred = Credentials(account, email, passlock)
    return new_cred

       ###save credential#######

def save_cred(cred):
    '''
    save credentials
    '''
    cred.save_cred()


    ######dispaly credential#######

def display_cred():
    '''
    method to display all the saved credentials
    '''
    return Credentials.display_cred()


######search credentials#######

def find_account(account):
    '''
    method to search for an account
    '''
    return Credentials.find_account(account)