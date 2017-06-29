import os

def shell():
    while True:
         pwd=os.getcwd()
         cmd=input('probin@shell:'+pwd+'$ ')
         l=cmd.split(' ')
         if cmd=='clear':
           os.system("clear")
         elif cmd=='exit':
             exit(0)
         elif l[0]=='cat':
             f=open(l[1],"r")
             str=f.read()
             print(str)
         elif l[0]=='rm':
             os.remove(l[1])
         elif l[0]=='mkdir':
             os.mkdir(l[1])
         elif l[0]=='rmdir':
             os.rmdir(l[1])
         elif l[0]=='cd':
             os.chdir(l[1])
         elif l[0]=='pwd':
             print(pwd)
         elif l[0]=='ls':
             fl=os.listdir(pwd)
             for f in fl:
                 print(f)
         elif l[0]=='cp':
             f1=open(l[1],"r")
             f2=open(l[2],"w")
             buffer=f1.read()
             f2.write(buffer)
             f1.close()
             f2.close()
         else:
             os.system(cmd)



def main():
    shell()




main()
