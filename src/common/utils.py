import os

ROOT_DIRECTORY = "/wa"

if not os.path.exists(ROOT_DIRECTORY):
    os.mkdir(ROOT_DIRECTORY)


def touch(fname, times=None):
    """ Touch file in given path """
    with open(fname, 'a'):
        os.utime(fname, times)


def get_pwd():
    """ Returns present working directory """
    return os.getcwd()