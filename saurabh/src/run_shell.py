'''run python shell'''

import py_shell
try:
    from termcolor import colored
except ImportError:
    py_shell.run_cmd("sudo pip install termcolor")

CMD_DICT = {
    'cd': py_shell.change_directoy,
    'ls': py_shell.list_files_or_dir,
    'mkdir': py_shell.make_dir,
    'rmdir': py_shell.remove_dir,
    'rm': py_shell.remove
}

while 1:
    print colored(py_shell.get_pwd() + ">> ", 'red'),
    CMD = raw_input()
    ARGS = map(str.strip, CMD.split())
    try:
        CMD_DICT[ARGS[0]](ARGS[1])
    except KeyError:
        if ARGS[0] == 'exit':
            break
        print colored("Not a valid command", 'cyan')
    except IndexError:
        if ARGS[0] == 'ls':
            CMD_DICT['ls']()
        else:
            print "Invalid command"
