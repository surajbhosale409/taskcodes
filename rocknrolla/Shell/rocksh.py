import os,subprocess
from termcolor import colored
from tempfile import mkstemp


def rm(fname):
    try:
        os.remove(fname)
    except:
        print (colored("File Not Found","red"))

def cat(fname):
    try:
        fh=open(fname,"r")
        data=fh.read()
        print (data)
    except:
        print(colored("Invalid Command Use","red"))

def ls(path="."):
    dirContent=os.listdir(path)
    files=list()
    dirs=list()
    for content in dirContent:
        if os.path.isdir(content):
            dirs.append(content)
        else:
            files.append(content)
    d="\t".join(dirs)
    f="\t".join(files)
    if len(d)!=0:
       print (colored(d,'cyan') +"\t"+f)
    else:
       print (f)


def cd(dirName):
    try:
           os.chdir(dirName)
    except PermissionError:
        print (colored("Permission Denied","red"))


def rmdir(dirName):
    os.rmdir(dirName)

def mkdir(dirName):
    os.mkdir(dirName)

def cp(src,dst):
    f1=open(src,"r")
    f2=open(dst,"w")
    data=f1.read()
    f2.write(data)
    f1.close()
    f2.close()

def vim(filename=""):
    fname=mkstemp()
    try:
       subprocess.call("/usr/bin/vim")
    except FileNotFoundError:
       print (colored("Command Not Found","red"))
       choice=input(colored("Do you install it?[Y/N]","green"))
       if choice=='Y' or choice=='y':
           os.system("sudo apt-get install vim")


commands={'rm':rm,'cp':cp,'vim':vim,'cd':cd,'ls':ls,'cat':cat,'rmdir':rmdir,'mkdir':mkdir}


def main():
  os.system("clear")
  print (colored("'RockSH'","red")+""+colored(" A shell by","white")+""+colored(" Suraj R Bhosale","green"))
  while True:
    pwd=os.getcwd()
    currentUser=os.getlogin()
    homeDir="/home/"+currentUser
    rootHomeDir="/root"
    if homeDir in pwd:
        l=list(pwd)
        l=l[len(homeDir):len(pwd)]
        pwd="".join(l)
        pwd="[~]"+pwd
    if rootHomeDir in pwd:
         l=list(pwd)
         l=l[len(rootHomeDir):len(pwd)]
         pwd="".join(l)
         pwd="[/]"+pwd

    cmdStr=input (colored(currentUser+"@rocksh: ","red")+""+colored(pwd+"$ ","green"))

    cmdList=cmdStr.split()


    try:
        commands[cmdList[0]](cmdList[1])
    except TypeError:
        if cmdList[0]=="cp":
            commands[cmdList[0]](cmdList[1],cmdList[2])

    except IndexError:
        if len(cmdList)==1:
           commands[cmdList[0]]()

    except KeyError:
        if cmdList[0]=="exit":
           exit(0)
        elif cmdList[0]=="clear":
           os.system("clear")
        elif cmdList[0]=="pwd":
           print (colored(pwd,"cyan"))
        else:
           print (colored("Command Not Found"))
           #os.system(cmdStr)

main()
