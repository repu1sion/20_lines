#!/usr/bin/python3

# git diff --stat deadpython.py         - to show new lines

import os
from termcolor import colored

ver = '0.11'

if __name__ == "__main__":

    print(colored('Hi. I\'m Deadpython', 'yellow'), colored(ver, 'yellow'), colored('. What can I do for you master?', 'yellow'))

    while True:
        c = str(input('Enter a command: '))
        # switch operator
        if (c == 'p'):
            print(colored('ping', 'green'))
            os.system('ping -c 4 kernel.org')
            continue            # XXX - without 'continue' it goes to 'else' section in case of 'p' only
        if (c == 'c'):
            os.system('clear')
            continue
        elif (c == 'q'):
            exit()
        elif (c == 'm'):
            print(colored('mem', 'green'))
            os.system('free -m')
            continue
        elif (c == 'f'):
            os.system('sync')
            print(colored('before flushing caches:', 'green'))
            os.system('free -m')
            os.system('sudo sh -c \'echo 3 >/proc/sys/vm/drop_caches\'')
            print(colored('after flushing caches:', 'green'))
            os.system('free -m')
            continue
        elif (c == 'i'):
            print(colored('info about os', 'green'))
            os.system('uname -a')
            os.system('lsb_release -a')
            continue
        elif (c == 'h'):
            print('p - ping')
            print('c - clear')
            print('i - info os')
            print('m - show mem')
            print('f - flush caches')
            print('q - quit')
            print('h - help')
            continue
        else:
            print('I don\'t know such a command master! : ', c)
