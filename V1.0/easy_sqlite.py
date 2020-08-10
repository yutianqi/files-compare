#!/usr/bin/env python
# coding=utf8

import sqlite3
  
class EasySqlite:
    """
    sqlite数据库操作工具类
    database: 数据库文件地址，例如：db/mydb.db
    """
    _connection = None
 
    def __init__(self, database):
        # 连接数据库
        self._connection = sqlite3.connect(database)
 
    def _dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d
 
    def execute(self, sql, args=[], result_dict=True, commit=True)->list:
        """
        执行数据库操作的通用方法
        Args:
        sql: sql语句
        args: sql参数
        result_dict: 操作结果是否用dict格式返回
        commit: 是否提交事务
        Returns:
        list 列表，例如：
        [{'id': 1, 'name': '张三'}, {'id': 2, 'name': '李四'}]
        """
        if result_dict:
            self._connection.row_factory = self._dict_factory
        else:
            self._connection.row_factory = None
        # 获取游标
        _cursor = self._connection.cursor()
        # 执行SQL获取结果
        _cursor.execute(sql, args)
        if commit:
            self._connection.commit()
        data = _cursor.fetchall()
        _cursor.close()
        return data
 
 
if __name__ == '__main__':
    db = EasySqlite('ret.sqlite')

    db.execute('''CREATE TABLE FILES (
            MD5 CHAR ( 64 ) PRIMARY KEY NOT NULL,
            OLD_DIR CHAR ( 2048 ) NOT NULL,
            OLD_FILE_NAME CHAR ( 2048 ) NOT NULL,
            FOUND INTEGER,
            FOUND_TIME DATETIME,
            NEW_DIR CHAR ( 2048 ) NOT NULL,
            NEW_FILE_NAME CHAR ( 2048 ) NOT NULL
        );
    ''')
    # INSERT INTO FILES ( MD5, OLD_DIR, OLD_FILE_NAME, FOUND, FOUND_TIME, NEW_DIR, NEW_FILE_NAME ) VALUES ('b1fea87ea735f25bbfe04acfe846fde1', 'D:\Duke\Sounds', 'rainymood.mp4', 1, '2020-07-30 12:34:56', 'D:\Duke\Sounds', 'rainymood.mp4')
    # db.execute("INSERT INTO FILES (MD5,DIR,FILE_NAME) VALUES ({}, {}, {})".format("'b1fea87ea735f25bbfe04acfe846fdee'", "'D:\Duke\Sounds'", "'rainymood.mp4'"))




