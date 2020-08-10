#!/usr/bin/env python
#encoding=utf8

import datetime
import os
import hashlib
import time
from file_item import FileItem
from duplicate_file_item import DuplicateFileItem
from file_name_enum import FILE_NAME


SCAN_PATHS = ['D:\\Code\\Github\\files-compare\\test_env\\files']
# SCAN_PATHS = ['D:\\Duke\\独家记忆\\Images\\']


TIME_STAMP = str(time.time())


def main():
    initPath()
    records = scanPath()
    save(os.path.join(FILE_NAME.WORK_DIR.value, FILE_NAME.FILES.value),
         records, '# MD5,目录,文件名')
    duplicateRecords = getDuplicateRecords(records)
    save(os.path.join(FILE_NAME.WORK_DIR.value, FILE_NAME.DUPLICATE_FILES.value),
         duplicateRecords, '# MD5,原目录,原文件名,新目录,新文件名,保留项')


def initPath():
    if not os.path.exists(FILE_NAME.WORK_DIR.value):
        os.makedirs(FILE_NAME.WORK_DIR.value)


def scanPath():
    print('\nScaning...')
    records = []
    for path in SCAN_PATHS:
        print('-> %s' % (path))
        total = 0
        for root, dirs, files in os.walk(path):
            for file in files:
                md5 = getMd5(os.path.join(root, file))
                fileItem = FileItem(md5, root, file)
                records.append(fileItem)
                total += 1
        print('   Total files: %d' % (total))
    return records


def getDuplicateRecords(records):
    print('\nFinding duplicate files...')
    uniqueRecordMap = {}
    duplicateRecords = []
    duplicate = 0
    for record in records:
        oldObj = uniqueRecordMap.get(record.md5)
        if oldObj == None:
            uniqueRecordMap[record.md5] = DuplicateFileItem(record.md5, record.folder, record.fileName)
        else:
            oldObj.newFolder = record.folder
            oldObj.newFileName = record.fileName
            duplicateRecords.append(oldObj)
            duplicate += 1
    print('-> Duplicate files: %d' % (duplicate))
    return duplicateRecords


def save(filePath, records, headLine = ''):
    print('\nSaving...')
    with open(filePath, 'w+', encoding='utf-8') as file:
        file.write(headLine + '\n')
        for record in records:
            # print('   %s' % (record))
            file.write(record.toCsvString())
            
    print('-> %s created...' % (filePath))


def getMd5(fileFullPath):
    with open(fileFullPath, 'rb') as md5file:
        md5 = hashlib.md5(md5file.read()).hexdigest()
        return md5


if '__main__' == __name__:
    main()
