#! /usr/bin/python
import sys

data = sys.argv[1]

def formattedQuery():
    data_splited = data.split('\n')
    ch_list = []
    for str in data_splited:
        str = str.lstrip()
        str = str.rstrip()
        ch_list.append(str)
    return ''.join(ch_list)