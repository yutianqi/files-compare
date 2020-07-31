#!/usr/bin/env python
# coding=utf8

import datetime
import os
import hashlib
from file_item import FileItem
from easy_sqlite import EasySqlite

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
                fileItem = FileItem(getMd5(os.path.join(root, file)), root, file)
                records.append(fileItem)
    save(records)


def save(records):
    saveToFile('ret.csv', records)
    # saveToSqliteDb('ret.sqlite', records)


def saveToFile(fileFullPath, records):
    with open(fileFullPath, 'w+') as file:
        for record in records:
            print(record.toCsvString())
            file.write(record.toCsvString())


def saveToSqliteDb(dbFileFullPath, records):
    db = EasySqlite(dbFileFullPath)
    for record in records:
        db.execute(record.toInsertSql())


def getMd5(fileFullPath):
    with open(fileFullPath, 'rb') as md5file:
        md5 = hashlib.md5(md5file.read()).hexdigest()
        return md5


if '__main__' == __name__:
    main()
