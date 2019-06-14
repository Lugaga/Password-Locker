#!usr/bin/env python 3.6

from user import User
from credentials import Credentials
import random


def register_user(f_name, l_name, u_name, password):
    """
    Function that creates a new Password Locker user account.
    """
    new_user = User(f_name, l_name, u_name, password)
    new_user.save_user()

def save_credentials(cred):
    """
        Method that stores existing credentials
    """
    Credentials.cred_list.append(cred)

    

