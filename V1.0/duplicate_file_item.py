class DuplicateFileItem:
    """
    my first class: FooClass
    """

    md5 = ''
    oldFolder = ''
    oldFileName = ''
    found = 0
    foundTime = ''
    newFolder = ''
    newFileName = ''
    keepItem = ''
    """
    constructor
    """

    def __init__(self, md5, oldFolder, oldFileName, found='0', foundTime='', newFolder='', newFileName='', keepItem=''):
        self.md5 = md5
        self.oldFolder = oldFolder
        self.oldFileName = oldFileName
        self.found = found
        self.foundTime = foundTime
        self.newFolder = newFolder
        self.newFileName = newFileName
        self.keepItem = keepItem

    def toCsvString(self):
        return '{},"{}","{}",{},{},"{}","{}",{}\n'.format(self.md5, self.oldFolder, self.oldFileName, self.found, self.foundTime, self.newFolder, self.newFileName, self.keepItem)
        # return '''{}, {}, {}, {}, {}, {}, {}\n'''.format(self.md5, self.oldFolder, self.oldFileName, self.found, self.foundTime, self.newFolder, self.newFileName)

    def toInsertSql(self):
        return "INSERT INTO FILES ( MD5, OLD_DIR, OLD_FILE_NAME, FOUND, FOUND_TIME, NEW_DIR, NEW_FILE_NAME, KEEP_ITEM ) VALUES ('{}', '{}','{}',{},datetime('{}'),'{}','{}','{}')".format(self.md5, self.oldFolder, self.oldFileName, self.found, self.foundTime, self.newFolder, self.newFileName, self.keepItem)

