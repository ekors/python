#! /usr/bin/python

import os,stat,sys

file=sys.argv[1]

def getFileMode():
	mode=int(oct(stat.S_IMODE(os.stat('os_module.py').st_mode)))
	return mode

def setFileMode():
	mode=sys.argv[2]
	if mode == getFileMode():
		print('File ' + file + 'is already has the same permissions!')
		exit(1)
	else:
		octalRepr=int(mode,8)
		os.chmod(file, octalRepr)
		print('mode of ' + file + ' was changed to ' + mode +' successfully')


if __name__ == '__main__':
	if len(sys.argv) == 2:
		print(getFileMode())
	elif len(sys.argv) == 3:
		setFileMode()
	else:
		print('Usage: {script} {filename} - for getting fileMode\n{script} {filename} {mode} - for setting fileMode')
		exit(1)