__author__ = 'pavlo'
from time import time
from sys import version_info
from hashlib import sha512

if version_info < (3, 4):
    import sha3


def current_milli_time():
    return int(round(time() * 1000))


def hash_password(password, salt):
    hash_function = sha512
    hash_function.update(password + salt)
    return hash_function.hexdigest()