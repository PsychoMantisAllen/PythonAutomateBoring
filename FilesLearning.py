import os
print(os.path.join('folder1', 'folder2', 'folder3', 'file.png'))
print(os.sep)   # separator in your os
os.getcwd()     # get your current directory
os.chdir()      # change to a new directory

'c:\\folder1\\folder2\\spam.png'    # this is an absolute file path (with the root folder)
'\\folder1\\folder2\\spam.png'      # this is a relative file path

# we can use a dot to represent current folder
# and a dot dot to present the parent folder

# to get the absolute path
os.path.abspath('spam.png')
# to determine whether the root folder is included
os.path.isabs('spam.png')

os.path.relpath('c:\\folder1\\folder2\\spam.png', 'c:\\folder1')
# this will return the relative path
os.path.dirname()   # if we only want the directory name
os.path.basename()  # if we only want the last part of the path
os.path.exists()    # check if a file is actually existed
os.path.isfile()
os.path.isdir()

os.path.getsize()   # return the size of the file in byte in integer
os.listdir()        # return all the files under the folder as a string

# we can check the size of all files under the folder
totalSize = 0
for filename in os.listdir('c:\\automatebook'):
    if not os.path.isfile(os.path.join('c:\\automatebook', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('c:\\automatebook', filename))
print(totalSize)

# if we want to create new folders (and folders inside)
os.makedirs('c:\\delicious\\walnut\\waffles')

# difference between read and readlines is that readlines returns a list of strings
Whatfile = open('c:\\users\\al\\hello.txt')
Whatfile.read()
Whatfile.readlines()

# to make a binary file in Python
import shelve
shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['paopao', 'Sushi', 'Rice']
# cat is the key and the list is the value
shelfFile.close()

list(shelfFile.keys())
list(shelfFile.values())

# copy a single file in Python
import shutil
shutil.copy('c:\\spam.txt', 'c:\\delicious')
shutil.copy('c:\\spam.txt', 'c:\\delicious\\spamspamspam.txt')  # change the file name in the destination

# copy all files under the path to a new folder
shutil.copytree('c:\\delicious', 'c:\\delicious_backup')
# to move the file
shutil.move()
# can use this to rename the file
shutil.move('c:\\abc\\wed.txt', 'c:\\abc\\edc.txt')

# delete a single file
os.getcwd()
os.unlink()

# delete a folder
os.rmdir()  # it has to be empty before deleting as a guarantee towards the folder

# delete the folder and the content
shutil.rmtree()

# all these deletions are dangerous as they are permanent
# if we want to move to trash
# install package send2trash
import send2trash
send2trash.send2trash()

for folderName, subfolders, filenames in os.walk('c:\\delicious'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
    print('The filenames in ' + folderName + ' are: ' + str(filenames))
    print()

    for subfolder in subfolders:
        if 'fish' in subfolder:
            os.rmdir(subfolder)

    for file in filenames:
        if file.endswith('.py'):
            shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup'))

