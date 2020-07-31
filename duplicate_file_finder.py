#!/usr/bin/env python
# coding=utf8

import datetime
import os
import hashlib
from file_item import FileItem
from easy_sqlite import EasySqlite

# SCAN_PATHS = ['D:\\Duke\\Code\\GitHub\\files-compare\\files']
SCAN_PATHS = ['D:\\Duke\\独家记忆\\Images\\待删除的副本']

# Duke
#   Images
#   Sounds
#   Videos
#   Documents


def main():
    records = {}

    for path in SCAN_PATHS:
        print('Scaning path: ' + path)
        total = 0
        duplicate = 0
        for root, dirs, files in os.walk(path):
            for file in files:
                total += 1
                md5 = getMd5(os.path.join(root, file))
                # print(file)
                # print(md5)
                oldObj = records.get(md5)
                if oldObj == None:
                    fileItem = FileItem(md5, root, file)
                    records[fileItem.md5] = fileItem
                else:
                    print('重复文件' + oldObj.oldFolder + "\\" + oldObj.oldFileName + " " + root + "\\" + file)
                    duplicate += 1
        print('Total files: ' + str(total))
        print('Duplicate files: ' + str(duplicate))













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
