from enum import Enum, unique

@unique
class FILE_NAME(Enum):
    WORK_DIR = 'D:\\Code\\Github\\files-compare\\files'
    REMOVE_FOLDER = 'D:\\Code\\Github\\files-compare\\test_env\\remove_folder'
    FILES = '0_files.csv'
    DUPLICATE_FILES = '1_duplicate_files.csv'

