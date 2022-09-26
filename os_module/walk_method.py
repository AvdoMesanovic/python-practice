import os

os.chdir('/Users/avdom/OneDrive/Desktop')

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()
"""Generator that yields a tuple of 3 values as it walks the directory 
tree. For each directory that it sees, it yields the directory path, the
directories within that path, and the files within that path"""