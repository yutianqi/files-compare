#!/usr/bin/env python
# coding=utf8

import time
import datetime
import os
import hashlib
import csv
from duplicate_file_item import DuplicateFileItem
from easy_sqlite import EasySqlite


CONFIG_FILE_PATHS = ['D:\\Code\\Github\\files-compare\\duplicateRecords.csv']

REMOVE_FOLDER = 'D:\\Code\\Github\\files-compare\\remove_folder'
# REMOVE_FOLDER = ''

def main():
    if REMOVE_FOLDER == '':
        tips = 'Are you confirm to delete the duplicate files permanently: yes/no\n> '
        confirm = input(tips)
        if confirm != 'yes':
            return
        elif REMOVE_FOLDER != '' and not os.path.isdir(REMOVE_FOLDER):
            print('REMOVE_FOLDER [%s] does not exist.' % (REMOVE_FOLDER))
            return

    for path in CONFIG_FILE_PATHS:
        with open(path, 'r') as f:
            reader = csv.reader(f)
            # Ignore the head line
            next(reader)
            for item in reader:
                if len(item) != 8:
                    print('Invalid data:' + str(item))
                print(item)
                fileItem = DuplicateFileItem(
                    item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
                # print(fileItem.md5)
                oldFile = os.path.join(fileItem.oldFolder, fileItem.oldFileName)
                newFile = os.path.join(fileItem.newFolder, fileItem.newFileName)
                keepItem = fileItem.keepItem
                while(keepItem != '0' and keepItem != '1'):
                    tips = 'Select the file to be reserved: \n  0: {}\n  1: {}\n> '.format(oldFile, newFile)
                    keepItem = input(tips)
                if keepItem == '0':
                    remove(newFile, fileItem.newFileName)
                elif keepItem == '1':
                    remove(oldFile, fileItem.oldFileName)


def remove(path, fileName):
    if REMOVE_FOLDER == '':
        print('Removeing: ' + path)
        # os.remove(path)
    else:
        print('Moveing: ' + path)
        os.rename(path, os.path.join(REMOVE_FOLDER, fileName + '.' + str(time.time())))
    

if '__main__' == __name__:
    main()
