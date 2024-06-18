import os
import shutil


path = '/Users/magma/Desktop/Middle/Courses/python-bro/chapter_02/files/test.txt'

try:
    os.remove(path=path)   # delete a file
    # os.rmdir(path=path)  # remove empty directory fn
    # shutil.rmtree(path)  # it is a dangerous fn
except FileNotFoundError:
    print('That file was not found')
except PermissionError:
    print('You do not have permission to delete that')
else:
    print('{} was deleted'.format(path))
