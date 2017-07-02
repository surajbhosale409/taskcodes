"""Main File for running shell"""

import shell_library as sl

command_Dictionary = {
    "ls"   : sl.listFile,
    "cd"   : sl.changeDirectory,
    "clear": sl.clearScreen,
    "mkdir": sl.makeDir,
    "rm"   : sl.removeDir,
    "cp"   : sl.copy
}


def start():
    sl.clearScreen()
    commands = command_Dictionary.keys()
    while True:
        command = input(sl.getHostId()+sl.getCwd()+"? ")
        command = command.split()

        if command[0]=="exit":
            break

        if command[0] not in commands:
            print("Invalid Command")
            continue

        command_Dictionary[command[0]](command[1:])

start()
