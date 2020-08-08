#!/usr/bin/env python
# coding=utf8

# Name:         xxx.py
# Purpose:      Run on the old PC. Record all of the files in specified folders.
# Author:       Duke <ytq0415@gmail.com>
# Created:      2020.07.29 20:20

import datetime
import os
import hashlib
from file_item import FileItem
from easy_sqlite import EasySqlite

# Scan folders
SCAN_PATHS = ['D:\\Duke\\Images']

#
DB_FILE_NAME = 'ret.sqlite'

DB = None

# SAVE_TYPE = 'DB'
SAVE_TYPE = 'CSV'

def main():
    if SAVE_TYPE == 'DB':
        initDb()
    records = []
    for path in SCAN_PATHS:
        for root, dirs, files in os.walk(path):
            for file in files:
                fileItem = FileItem(
                    getMd5(os.path.join(root, file)), root, file)
                records.append(fileItem)
    save(records)


def initDb():
    global DB 
    DB = EasySqlite(DB_FILE_NAME)

    table = DB.execute(
        "SELECT * FROM SQLITE_MASTER WHERE TYPE = 'table' AND NAME = 'FILES'")

    if len(table) != 0:
        clear = input('The table [FILES] existed. \n  0: Clear\n  1: Append\n> '.format(DB_FILE_NAME))
        if clear == '0':
            DB.execute("delete from FILES")
    else:
        DB.execute('''CREATE TABLE FILES (
            MD5 CHAR ( 64 ) PRIMARY KEY NOT NULL,
            OLD_DIR CHAR ( 2048 ) NOT NULL,
            OLD_FILE_NAME CHAR ( 2048 ) NOT NULL,
            FOUND INTEGER,
            FOUND_TIME DATETIME,
            NEW_DIR CHAR ( 2048 ),
            NEW_FILE_NAME CHAR ( 2048 ),
            MOVED INTEGER,
            MOVED_TIME DATETIME
        );''')


def save(records):
    if SAVE_TYPE == 'DB':
        saveToSqliteDb(records)
    elif SAVE_TYPE == 'CSV':
        saveToFile('ret.csv', records)
    else:
        print('Invalid SAVE_TYPE: [%s]' % (SAVE_TYPE))


def saveToFile(fileFullPath, records):
    with open(fileFullPath, 'w+') as file:
        for record in records:
            print(record.toCsvString())
            file.write(record.toCsvString())


def saveToSqliteDb(records):
    for record in records:
        DB.execute(record.toInsertSql())


def getMd5(fileFullPath):
    with open(fileFullPath, 'rb') as md5file:
        md5 = hashlib.md5(md5file.read()).hexdigest()
        return md5


if '__main__' == __name__:
    main()
