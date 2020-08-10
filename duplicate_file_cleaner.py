#!/usr/bin/env python
# coding=utf8

import time
import os
import csv
from duplicate_file_item import DuplicateFileItem
from file_name_enum import FILE_NAME


CONFIG_FILE_PATHS = [os.path.join(FILE_NAME.WORK_DIR.value, FILE_NAME.DUPLICATE_FILES.value)]

# REMOVE_FOLDER = FILE_NAME.REMOVE_FOLDER.value
REMOVE_FOLDER = ''


def main():
    if REMOVE_FOLDER == '':
        tips = 'Are you confirm to delete the duplicate files permanently: yes/no\n> '
        confirm = input(tips)
        if confirm != 'yes':
            print('Please config remove folder first.')
            return
    elif not os.path.isdir(REMOVE_FOLDER):
        print('REMOVE_FOLDER [%s] does not exist.' % (REMOVE_FOLDER))
        return

    # print(CONFIG_FILE_PATHS)

    for path in CONFIG_FILE_PATHS:
        print(path)
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            # Ignore the head line
            next(reader)
            for item in reader:
                if len(item) != 6:
                    print('Invalid data:' + str(item))
                    continue
                print(item)
                fileItem = DuplicateFileItem(
                    item[0], item[1], item[2], item[3], item[4], item[5])
                removeDuplicateItem(fileItem)


def removeDuplicateItem(fileItem):
    # print(fileItem.md5)
    oldFile = os.path.join(fileItem.oldFolder, fileItem.oldFileName)
    newFile = os.path.join(fileItem.newFolder, fileItem.newFileName)
    keepItem = fileItem.keepItem
    while(keepItem != '0' and keepItem != '1'):
        tips = 'Select the file to be reserved: \n  0: {}\n  1: {}\n> '.format(
            oldFile, newFile)
        keepItem = input(tips)
    if keepItem == '0':
        if os.path.exists(oldFile):
            remove(newFile, fileItem.newFileName)
        else:
            print('Old file [%s] not exit. Remove operation cancelled.' % (oldFile))
    elif keepItem == '1':
        if os.path.exists(newFile):
            remove(oldFile, fileItem.oldFileName)
        else:
            print('New file [%s] not exit. Remove operation cancelled.' % (newFile))


def remove(path, fileName):
    if REMOVE_FOLDER == '':
        print('Removeing: ' + path)
        os.remove(path)
    else:
        print('Moveing: ' + path)
        os.rename(path, os.path.join(REMOVE_FOLDER, fileName + '.' + str(time.time())))


if '__main__' == __name__:
    main()
