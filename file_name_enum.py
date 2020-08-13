from enum import Enum, unique

@unique
class FILE_NAME(Enum):
    WORK_DIR = 'D:\\Code\\Github\\files-compare\\files'
    REMOVE_FOLDER = 'D:\\Code\\Github\\files-compare\\test_env\\remove_folder'
    MOVE_FOLDER = 'D:\\Code\\Github\\files-compare\\test_env\\move_folder'
    FILES = '0_files.csv'
    DUPLICATE_FILES = '1_duplicate_files.csv'
    NEW_FOUND_FILES = '2.1_new_found_files.csv'
    FOUND_FILES = '2.2_found_files.csv'
    NOT_EXIST_FILES = '2.3_not_exist_files.csv'

