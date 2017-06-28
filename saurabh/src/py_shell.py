'''shell implementation in python'''

import subprocess
import os

def run_cmd(cmd):
    '''run shell commmand'''
    subprocess.call(cmd, shell=True)

try:
    from termcolor import colored
except ImportError:
    run_cmd("sudo pip install termcolor")


def change_directoy(path):
    "change directory"
    try:
        os.chdir(path)
    except OSError as error:
        print colored(error, 'cyan')

def list_files_or_dir(path='.'):
    '''list content from path'''
    try:
        data = os.listdir(path)
        full_path_data = map(lambda x: (path + "/" + x, x), data)
        for item in filter (lambda x: os.path.isdir(x[0]), full_path_data):
            print colored(item[1], 'blue'),
        for item in filter (lambda x: not os.path.isdir(x[0]), full_path_data):
            print item[1],
        print "\n"
    except OSError as error:
        print colored(error, 'cyan')

def make_dir(path):
    '''create directory at path'''
    try:
        os.mkdir(path)
    except OSError as error:
        print colored(error, 'cyan')

def remove_dir(path):
    '''remove directory at path'''
    try:
        os.rmdir(path)
    except OSError as error:
        print colored(error, 'cyan')

def remove(path):
    '''remove from path'''
    try:
        os.remove(path)
    except OSError as error:
        print colored(error, 'cyan')

def get_pwd():
    '''return current working directory'''
    try:
        return os.getcwd()
    except OSError as error:
        print colored(error, 'cyan')
