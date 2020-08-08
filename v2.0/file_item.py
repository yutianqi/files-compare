class FileItem:
    md5 = ''
    folder = ''
    fileName = ''

    def __init__(self, md5, folder, fileName):
        self.md5 = md5
        self.folder = folder
        self.fileName = fileName

    def toCsvString(self):
        return '{},"{}","{}"\n'.format(self.md5, self.folder, self.fileName)

