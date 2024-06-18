import os


source = 'written.txt'
destination = '/Users/magma/Desktop/Middle/Courses/python-bro/chapter_02/files/folder_test/moved_content.txt'

try:
    if os.path.exists(destination):
        print('There is already a file there')
    else:
        os.replace(source, destination)
        print('{source} was moved'.format(source=source))

except FileNotFoundError:
    print('{} was not found'.format(source))
