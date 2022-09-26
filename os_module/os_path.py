import os

os.chdir('/Users/avdom/OneDrive/Desktop')

print(os.eviron.get('USERPROFILE')) # Gets location of specified directory
file_path = os.path.join(os.eviron.get('USERPROFILE'), 'test.txt')
"""Most effective way to create paths"""
print(file_path)

print(os.path.basename('/tmp/test.txt'))
"""Grabs the base name of a path
# test.txt"""

print(os.path.dirname('/tmp/test.txt'))
"""Grabs the directory name of a path
# /tmp"""

print(os.path.split('/tmp/test.txt'))
"""Grabs both
# (''/tmp', 'test.txt')"""

print(os.path.exists('/tmp/test.txt'))
"""Determines if a path exists, would come up as false here"""

# os.path.isdir() - Determines if something is a directory
# os.path.isdir() - Determines if something is a file

print(os.path.splitext('/tmp/test.txt')) 
"""Splits the file root of the path and extension"""

# print(dir(os.path)) - Prints all accessible methods to os.path