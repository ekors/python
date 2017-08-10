#! /usr/bin/python

import os,stat,sys

file=sys.argv[1]

def getFileMode():
	mode=int(oct(stat.S_IMODE(os.stat(file).st_mode)))
	return mode

def setFileMode():
	mode=int(sys.argv[2])
	if mode == getFileMode():
		print('File %s is already has the same permissions!' % (file))
		exit(1)
	else:
		os.chmod(file, getFileMode())
		print('mode of %s was changed to %s successfully' % (file, mode))


if __name__ == '__main__':
	if len(sys.argv) == 2:
		print(getFileMode())
	elif len(sys.argv) == 3:
		setFileMode()
	else:
		print('Usage: {script} {filename} - for getting fileMode\n{script} {filename} {mode} - for setting fileMode')
		exit(1)