#!/usr/bin/env python
# coding=utf8

import datetime
import os
import hashlib


SCAN_PATHS = ['D:\Duke\Images']



# Duke
#   Images
#   Sounds
#   Videos
#   Documents




def main():
    lines = []
    for path in SCAN_PATHS:
        for root, dirs, files in os.walk(path):
            for file in files:
                line = ','.join((getMd5(os.path.join(root, file)), '"' + root + '"', '"'+file+'"'))
                print(line)
                lines.append(line + '\n')
    save('ret.csv', lines)


def save(fileFullPath, lines):
    with open(fileFullPath, 'w+') as file:
        file.writelines(lines)


def getMd5(fileFullPath):
    with open(fileFullPath, 'rb') as md5file:
        md5 = hashlib.md5(md5file.read()).hexdigest()
        return md5


if '__main__' == __name__:
    main()
