#!/usr/bin/env python
# coding=utf8

import datetime
import os
import hashlib
from file_item import FileItem

SCAN_PATHS = ['D:\Duke\Sounds']


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
                fileItem = FileItem(getMd5(os.path.join(root, file)), '"' + root + '"', '"'+file+'"')
                records.append(fileItem)
    save(records)


def save(records):
    # saveToFile('ret.csv', records)
    saveToSqliteDb('ret.sqlite', records)


def saveToFile(fileFullPath, records):
    lines = []
    for record in records:
        lines.append(record.toString())

    with open(fileFullPath, 'w+') as file:
        file.writelines(lines)


def saveToSqliteDb(dbFileFullPath, records):
    db = EasySqlite(dbFileFullPath)

    lines = []
    for record in records:
        lines.append(record.toString())

    with open(fileFullPath, 'w+') as file:
        file.writelines(lines)




def getMd5(fileFullPath):
    with open(fileFullPath, 'rb') as md5file:
        md5 = hashlib.md5(md5file.read()).hexdigest()
        return md5


if '__main__' == __name__:
    main()
