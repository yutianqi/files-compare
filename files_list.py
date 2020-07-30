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
    records = []
    for path in SCAN_PATHS:
        for root, dirs, files in os.walk(path):
            for file in files:
                records.append((getMd5(os.path.join(root, file)),
                                '"' + root + '"', '"'+file+'"'))
    save(records)


def save(records):
    saveToFile('ret.csv', records)


def saveToFile(fileFullPath, records):
    lines = []
    for record in records:
        # record.toString();
        # line = ','.join(record[0], record[1], record[2])
        line = ','.join(record)
        print(line)
        lines.append(line + '\n')

    with open(fileFullPath, 'w+') as file:
        file.writelines(lines)


def getMd5(fileFullPath):
    with open(fileFullPath, 'rb') as md5file:
        md5 = hashlib.md5(md5file.read()).hexdigest()
        return md5


if '__main__' == __name__:
    main()
