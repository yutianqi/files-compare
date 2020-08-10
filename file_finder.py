#!/usr/bin/env python
#encoding=utf8

import datetime
import os
import hashlib
import time
from file_item import FileItem
from duplicate_file_item import DuplicateFileItem
from file_name_enum import FILE_NAME
import csv

SCAN_PATHS = ['D:\\Code\\Github\\files-compare\\test_env\\files_new']

DATA_FILE_PATH = os.path.join(FILE_NAME.WORK_DIR.value, FILE_NAME.FILES.value)


def main():
    if not os.path.isfile(DATA_FILE_PATH):
        print('The data file [%s] does not exist.' % (DATA_FILE_PATH))
        return
    oldFileMap = loadOldFileMap()
    newFiles = loadNewFiles()

    # 分析新文件
    newFoundFiles = [item for item in newFiles if item.md5 not in oldFileMap.keys()]
    save(os.path.join(FILE_NAME.WORK_DIR.value, FILE_NAME.NEW_FOUND_FILES.value), newFoundFiles, '# MD5,目录,文件名')

    # 分析已存在文件
    existedFiles = [item for item in newFiles if item.md5 in oldFileMap.keys()]
    foundFiles = []
    for item in existedFiles:
        oldFileItem = oldFileMap.get(item.md5)
        duplicateFileItem = DuplicateFileItem(oldFileItem.md5, oldFileItem.folder, oldFileItem.fileName, item.folder, item.fileName)
        foundFiles.append(duplicateFileItem)
    save(os.path.join(FILE_NAME.WORK_DIR.value, FILE_NAME.FOUND_FILES.value), foundFiles, '# MD5,原目录,原文件名,新目录,新文件名,已处理')

    # 分析不存在文件
    newFileMd5s = [item.md5 for item in newFiles]
    notExistedFiles = [item[1] for item in oldFileMap.items() if item[0] not in newFileMd5s]
    save(os.path.join(FILE_NAME.WORK_DIR.value, FILE_NAME.NOT_EXIST_FILES.value), notExistedFiles, '# MD5,目录,文件名')


def loadOldFileMap():
    print('\nLoading records from %s ...' % (DATA_FILE_PATH))
    fileMap = {}
    invalidRecordAmount = 0
    with open(DATA_FILE_PATH, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        # Ignore the head line
        next(reader)
        for item in reader:
            if len(item) != 3:
                print('Invalid data:' + str(item))
                invalidRecordAmount += 1
                continue
            # print(item)
            fileItem = FileItem(item[0], item[1], item[2])
            fileMap[item[0]] = fileItem

    print('\n * Loaded %d records...' % (len(fileMap)))
    print('\n * Failed %d records...' % (invalidRecordAmount))
    return fileMap


def loadNewFiles():
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
