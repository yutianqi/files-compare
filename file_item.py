class FileItem:
    """my first class: FooClass"""

    version = 0.1

    """
    constructor
    """
    def __init__(self, md5, dir, fileName):
        self.md5 = md5
        self.dir = dir
        self.fileName = fileName

    def toString(self):
        line = ','.join((self.md5, self.dir, self.fileName))
        return line + '\n'

    def showver(self):
        print(self.version)

    def addMe2Me(self, x):
        """applu + operation to argument"""
        return x+x
