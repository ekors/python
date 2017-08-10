#! /usr/bin/python

import os, stat, sys, re


def getFileMode():
    file = sys.argv[1]
    mode = int(oct(stat.S_IMODE(os.stat(file).st_mode)))
    return mode


def setFileMode():
    file = sys.argv[1]
    mode = sys.argv[2]
    if int(mode) == getFileMode():
        print('File %s is already has the same permissions!' % (file))
        exit(1)
    else:
        octalRepr = int(mode, 8)
        os.chmod(file, octalRepr)
        print('mode of %s was changed to %s successfully' % (file, mode))


def reArgv(some_string):
    if re.match(r'^\d{3}$', some_string):
        return some_string
    else:
        print('Please enter correct fileMode (arg#2)!\n')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(getFileMode())
    elif len(sys.argv) == 3 and reArgv(sys.argv[2]):
        setFileMode()
    else:
        print('Usage: {script} {filename} - for getting fileMode\n{script} {filename} {mode} - for setting fileMode')
        exit(1)
