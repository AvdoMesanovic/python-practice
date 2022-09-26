# Using this method, you can select what you want to import from a file

from my_module import find_index, test 
# Imports both the find_index and test variable
# Could also do import find_index as fi (or any desired name)

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(index)
print(test)

'''To see what locations the system checks when you're importing files,
you could do:'''
# print(sys.path)
'''Could add locations to sys.path through windows using enviroment 
variables, the terminal, or in VSCode'''
'''To import through VSCode in a fyle, type:'''
# import sys
# sys.path append(...)