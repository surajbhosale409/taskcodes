"""Library File for shell"""

import os
import sys
from getpass import getuser
from socket import gethostname
from shutil import copy2
from termcolor import colored


def clearScreen(arg=""):
    """Clear console screen"""
    try:
        os.system("clear")
    except OSError as error:
        print(error)

def getHostId():
    """Return Username@hostname: """
    try:
        return str(getuser()+"@"+gethostname()+":")
    except:
        print("Error in getHostId")

def getCwd():
    """Returns current working directory by shell naming convention"""
    try:
        path = os.getcwd()

        if path=="/":
            return path

        path = path.split("/")[1:]
        if len(path)>=2:
            if path[0]=="home" and path[1]==getuser():
                path[1]="~"
                path = "/".join(path[1:])
                return path
        elif len(path)<2 :
            return "/"+"/".join(path)


    except OSError as error:
        print (error)

def listFile(path):
    """Lists files and directories in given path"""
    try:
        if path == []:
            path = ["."]
        for (path,dirs,files) in os.walk(path[0]):
            dirs = list(filter (lambda d:not d.startswith("."),dirs))
            for d in dirs:
                print (colored(d,"cyan"),end="\t")

            files = list (filter (lambda x:not x.startswith("."), files))
            for f in files:
                print (colored(f,"white"),end="\t")

            print("")
            break

    except OSError as error:
        print(error)
    except:
        print("Some unknown error",sys.exc_info())

def changeDirectory(path):
    """change current working directory to path"""
    try:
        os.chdir(path[0])
    except OSError as error:
        print(error)
    except IndexError:
        os.chdir("/home/"+getuser()+"/")

def makeDir(path):
    """Create directory at given path"""
    try:
        if path == []:
            raise Exception("mkdir: missing operand")

        # print(path[0])
        os.mkdir(path[0])

    except OSError as error:
        print(error)
    except Exception as error:
        print(error)

def removeDir(path):
    """Remove file at given path"""
    try:
        if path == []:
            raise Exception("rm: missing operand")
        os.rmdir(path[0])
    except OSError as error:
        print(error)
    except Exception as error:
        print(error)

def copy(args):
    """ copy file from source to destination"""
    try:
        copy2(args[0],args[1])
    except IOError as error:
        print(error)
    except IndexError:
        print("cp: missing file operand")
    except:
        print(sys.exc_info())
