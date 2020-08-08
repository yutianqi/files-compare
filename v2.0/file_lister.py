#!/usr/bin/env python
# coding=utf8

import datetime
import os
import hashlib
import time
from file_item import FileItem
from file_name_enum import FILE_NAME


SCAN_PATHS = ['D:\\Code\\Github\\files-compare\\files']

TIME_STAMP = str(time.time())
WORK_DIR = 'files\\'
CSV_FIEL_NAME = FILE_NAME.FILES


def main():
    initPath()
    records = scanPath()
    save(records)


def initPath():
    if not os.path.exists(WORK_DIR):
        os.makedirs(WORK_DIR)


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


def save(records):
    print('\nSaving...')
    headLine = '# MD5,目录,文件名'
    filePath = os.path.join(WORK_DIR, CSV_FIEL_NAME)
    with open(filePath, 'w+') as file:
        file.write(headLine + '\n')
        for record in records:
            file.write(record.toCsvString())
    print('-> %s created...' % (filePath))

def getMd5(fileFullPath):
    with open(fileFullPath, 'rb') as md5file:
        md5 = hashlib.md5(md5file.read()).hexdigest()
        return md5


if '__main__' == __name__:
    main()
