import os

def cat(fname):
	fh=open(fname,"r")
	data=fh.read()
	print data


def main():
	os.system("clear")	
	while True:
		cmdStr=raw_input("rocksh@deb~$ ")
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
			os.chdir(cmdList[1])
		elif cmdList[0]=="ls":
			print "\n".join(os.listdir(os.getcwd()))
		elif cmdList[0]=="rm":
			os.remove(cmdList[1])
		else:
			os.system(cmdStr)


main()
