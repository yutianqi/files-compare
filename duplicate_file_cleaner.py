#!/usr/bin/env python
# coding=utf8

import time
import os
import csv
from duplicate_file_item import DuplicateFileItem
from file_name_enum import FILE_NAME


DUPLICATE_FILE_PATHS = [os.path.join(FILE_NAME.WORK_DIR.value, FILE_NAME.DUPLICATE_FILES.value)]

REMOVE_FOLDER = FILE_NAME.REMOVE_FOLDER.value
# REMOVE_FOLDER = ''


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

    # print(DUPLICATE_FILE_PATHS)

    for path in DUPLICATE_FILE_PATHS:
        print("Processing the duplicate files in %s" % (path))
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            # Ignore the head line
            next(reader)
            fileItem = None
            for item in reader:
                if len(item) != 5:
                    print('Invalid data:' + str(item))
                    continue
                if item[0] != '':
                    removeDuplicateItem(fileItem)
                    fileItem = DuplicateFileItem(item[0], item[1], item[2], [item[3]], item[4])
                else:
                    fileItem.newFiles.append(item[3])
            removeDuplicateItem(fileItem)


def removeDuplicateItem(fileItem):
    if fileItem == None:
        return
    print('-> %s' % (fileItem.md5))
    if fileItem.keepItem == '':
        print('   Not specify keep item...')    
        return
    files = [os.path.join(fileItem.oldFolder, fileItem.oldFileName)]
    files.extend(fileItem.newFiles)

    keepItemIndex = int(fileItem.keepItem)

    print("   %d copies, reserve the [%d] one." % (len(files), keepItemIndex))

    if (keepItemIndex >= len(files)):
        print("   Delete index out of range.")

    reservedFile = files.pop(keepItemIndex)

    if os.path.exists(reservedFile):
        remove(files)
    else:
        print('   Reserved file [%s] not exit. Remove operation cancelled.' % (reservedFile))


def remove(paths):
    for path in paths:
        if not os.path.exists(path):
            print('   > Already removed: ' + path)
            continue
        if REMOVE_FOLDER == '':
            print('   > Removeing: ' + path)
            os.remove(path)
        else:
            print('   > Moveing: ' + path)
            os.rename(path, os.path.join(REMOVE_FOLDER, os.path.basename(path) + '.' + str(time.time())))


if '__main__' == __name__:
    main()
