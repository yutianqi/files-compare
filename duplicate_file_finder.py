#!/usr/bin/env python
# coding=utf8

import datetime
import os
import hashlib
from duplicate_file_item import DuplicateFileItem
from easy_sqlite import EasySqlite

SCAN_PATHS = ['D:\\Code\\Github\\files-compare\\files']

def main():
    totalRecordList = []
    uniqueRecordMap = {}
    for path in SCAN_PATHS:
        total = 0
        duplicate = 0
        for root, dirs, files in os.walk(path):
            for file in files:
                md5 = getMd5(os.path.join(root, file))
                fileItem = DuplicateFileItem(md5, root, file)
                totalRecordList.append(fileItem)
                total += 1

                oldObj = uniqueRecordMap.get(md5)
                if oldObj == None:
                    uniqueRecordMap[fileItem.md5] = fileItem
                else:
                    oldObj.newFolder = root
                    oldObj.newFileName = file
                    # print('发现重复文件' + oldObj.oldFolder + "\\" + oldObj.oldFileName + " " + root + "\\" + file)
                    duplicate += 1

    print('Total files: ' + str(len(totalRecordList)))
    print('Duplicate files: ' + str(len(totalRecordList) - len(uniqueRecordMap)))

    save(totalRecordList)


def save(totalRecords):
    saveToFile('totalRecords.csv', totalRecords, '# MD5,原目录,原文件名,是否重复,重复发现时间,重复文件,重复文件名,保留选项')
    duplicateRecords = [item for item in totalRecords if item.newFileName != '']
    saveToFile('duplicateRecords.csv', duplicateRecords, '# MD5,原目录,原文件名,是否重复,重复发现时间,重复文件,重复文件名,保留选项')
    # saveToSqliteDb('ret.sqlite', records)


def saveToFile(fileFullPath, records, headLine=''):
    with open(fileFullPath, 'w+') as file:
        if headLine:
            file.write(headLine + '\n')
        for record in records:
            # print(record.toCsvString())
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
