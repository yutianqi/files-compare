class DuplicateFileItem:

    # md5 = ''
    # oldFolder = ''
    # oldFileName = ''
    # newFiles = []
    # keepItem = ''

    def __init__(self, md5, oldFolder, oldFileName, newFiles = [], keepItem=''):
        self.md5 = md5
        self.oldFolder = oldFolder
        self.oldFileName = oldFileName
        self.newFiles = newFiles
        self.keepItem = keepItem

    def toCsvString(self):
        ret = '{},"{}","{}","{}","{}",{}\n'.format(
            self.md5, self.oldFolder, self.oldFileName, self.newFiles[0][0], self.newFiles[0][1], self.keepItem)
        if len(self.newFiles) > 1:
            for item in self.newFiles[1:]:
                ret += ',,,"{}","{}",{}\n'.format(item[0], item[1], self.keepItem)
        return ret

def main():
    uniqueRecordMap = {}
    duplicateFileItem1 = DuplicateFileItem(
        '1', 'D:\\Code\\Github\\files-compare\\test_env\\files', '1.jpg')
    duplicateFileItem2 = DuplicateFileItem(
        '2', 'D:\\Code\\Github\\files-compare\\test_env\\files', '2.jpg', ['D:\\Code\\Github\\files-compare\\test_env\\files\\3.jpg'])

    uniqueRecordMap['1'] = duplicateFileItem1
    uniqueRecordMap['2'] = duplicateFileItem2
    l = [item[1] for item in uniqueRecordMap.items() if len(item[1].newFiles) == 0]
    # print(uniqueRecordMap.items())
    print(l[0].md5)


if __name__ == '__main__':
    main()

