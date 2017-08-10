#! /usr/bin/python3

import pyperclip, sys

def underscoreAdd():
    if len(sys.argv) < 2:
        str = input("Paste/enter some text: ").replace(" ", "_")
    else:
        str = ' '.join(sys.argv[1:]).replace(' ', '_')
    pyperclip.copy(str)
    print(str)

if __name__=='__main__':
    underscoreAdd()
