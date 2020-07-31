class FileItem:
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
    moved = 0
    movedTime = ''
    """
    constructor
    """

    def __init__(self, md5, oldFolder, oldFileName, found='0', foundTime='', newFolder='', newFileName='', moved='0', movedTime=''):
        self.md5 = md5
        self.oldFolder = oldFolder
        self.oldFileName = oldFileName
        self.found = found
        self.foundTime = foundTime
        self.newFolder = newFolder
        self.newFileName = newFileName
        self.moved = moved
        self.movedTime = movedTime

    def toCsvString(self):
        return '{},"{}","{}",{},{},"{}","{},{},{}"\n'.format(self.md5, self.oldFolder, self.oldFileName, self.found, self.foundTime, self.newFolder, self.newFileName, self.moved, self.movedTime)

    def toInsertSql(self):
        return "INSERT INTO FILES ( MD5, OLD_DIR, OLD_FILE_NAME, FOUND, FOUND_TIME, NEW_DIR, NEW_FILE_NAME, MOVED, MOVED_TIME ) VALUES ('{}', '{}','{}',{},datetime('{}'),'{}','{}',{},datetime('{}'))".format(self.md5, self.oldFolder, self.oldFileName, self.found, self.foundTime, self.newFolder, self.newFileName, self.moved, self.movedTime)


'''
fileItem = FileItem('md5','dir','fileName')
print(fileItem.toCsvString())
'''
