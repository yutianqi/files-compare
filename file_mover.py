#!/usr/bin/env python
# coding=utf8

import time
import os
import csv
from duplicate_file_item import DuplicateFileItem
from file_name_enum import FILE_NAME


FILE_PATHS = ["D:\\Code\\Github\\files-compare\\files\\2.2_found_files.csv"]


def main():
    # print(FILE_PATHS)
    for path in FILE_PATHS:
        print("Processing the duplicate files in %s" % (path))

        toMovedRecords = []
        toRemovedRecords = []
        invalidRecords = []

        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            # Ignore the head line
            next(reader)
            fileItem = None
            for item in reader:
                if len(item) != 5:
                    print('Invalid data:' + str(item))
                    invalidRecords.append(item)
                    continue
                if len(item) == 3:
                    toRemovedRecords.append(item)
                    continue
                if len(item) == 5:
                    toMovedRecords.append(item)
                    print(item[0])
                    continue

        print(' %d invalid records. %d files to be removed. %d files to be moved.' % (len(invalidRecords), len(toRemovedRecords), len(toMovedRecords)))
        if len(toRemovedRecords) == 0 and len(toMovedRecords) ==0:
            return
        tips = 'Are you confirm to continue the remove and move operation: yes/no\n> '
        confirm = input(tips)
        if confirm != 'yes':
            print('Operation cancelled.')
            return
        performOperation(toRemovedRecords)
        performOperation(toMovedRecords)


def performOperation(items):
    for item in items:
        oldFilePath = os.path.join(item[1], item[2])
        if len(item) == 5:
            if not os.path.exists(item[3]):
                os.makedirs(item[3])
            newFilePath = os.path.join(item[3], item[4])

            os.rename(oldFilePath, newFilePath)
        else:
            os.remove(oldFilePath)


if '__main__' == __name__:
    main()
