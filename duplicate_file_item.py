class DuplicateFileItem:

    md5 = ''
    oldFolder = ''
    oldFileName = ''
    newFolder = ''
    newFileName = ''
    keepItem = ''

    def __init__(self, md5, oldFolder, oldFileName, newFolder='', newFileName='', keepItem=''):
        self.md5 = md5
        self.oldFolder = oldFolder
        self.oldFileName = oldFileName
        self.newFolder = newFolder
        self.newFileName = newFileName
        self.keepItem = keepItem

    def toCsvString(self):
        return '{},"{}","{}","{}","{}",{}\n'.format(self.md5, self.oldFolder, self.oldFileName, self.newFolder, self.newFileName, self.keepItem)

