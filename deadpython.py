#!/usr/bin/python3

import os
from termcolor import colored

ver = '0.05'

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
        elif (c == 'h'):
            print('p - ping')
            print('c - clear')
            print('q - quit')
            print('h - help')
            continue
        else:
            print('I don\'t know such a command master! : ', c)
