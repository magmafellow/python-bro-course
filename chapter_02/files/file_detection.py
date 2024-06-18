import os

path = '/Users/magma/Desktop/Middle/Courses/python-bro/chapter_02/files/folder_test'

if os.path.exists(path):
    print('That location exists')
    if os.path.isfile(path):
        print('That is a file')
    elif os.path.isdir(path):
        print('That is a directory')
else:
    print('That location does not exist')
