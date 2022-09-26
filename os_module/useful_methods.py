# OS module allows user to interact with the underlying operating system

import os

"""print(dir(os)) 
Shows the attributes and methods accessible in this module"""

"""print(os.getcwd()) 
Gets the current working directory"""

os.chdir('/Users/avdom/OneDrive/Desktop') # Changes working directory

os.mkdir('OS-Demo-2') # Makes a new folder in current working directory

os.makedirs('OS-Demo/Sub-Dir-1') 
"""Can create a directory that's a few levels deep, while
mkdir can not"""

os.rmdir('OS-Demo-2') # Can only remove primary directory
os.removedirs('OS-Demo/Sub-Dir-1') # Can remove primary and intermediate directories
"""rmdir and removedirs correlate to mkdir and makedirs respectively"""

os.mkdir('test')
os.rename('test', 'demo') # Changes the name of a file/folder

print(os.stat('demo')) # Provides information of a file/folder

print(os.listdir()) # Lists the files/folders in current working directory