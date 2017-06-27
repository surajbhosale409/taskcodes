import os

def cat(fname):
    fh=open(fname,"r")
    data=fh.read()
    print (data)


def main():
   os.system("clear")
   print ("'RockSH' A shell by Suraj R Bhosale")
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

     cmdStr=input(currentUser+"@rocksh:"+pwd+"$ ")
     cmdList=cmdStr.split()
     if cmdList[0]=="exit":
      exit(0)
     if cmdList[0]=="clear":
      os.system("clear")
     elif cmdList[0]=="cat":
      cat(cmdList[1])
     elif cmdList[0]=="mkdir":
      os.mkdir(cmdList[1])
     elif cmdList[0]=="rmdir":
      os.rmdir(cmdList[1])
     elif cmdList[0]=="cd":
         try:
             os.chdir(cmdList[1])
         except PermissionError:
             print ("Permission Denied")
     elif cmdList[0]=="ls":
      print ("\n".join(os.listdir(os.getcwd())))
     elif cmdList[0]=="rm":
      os.remove(cmdList[1])
     else:
      os.system(cmdStr)

main()
