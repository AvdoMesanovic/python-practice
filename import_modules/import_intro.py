'''If two python files are in the same directory, 
they can be directly imported to one another'''

'''When we import a file, it runs all of the code from the module that
we import, so that's how it creates all of the functions and variables
to the other file'''

import my_module as mm
# Import statement, my_module also now referred to as mm

courses = ['History', 'Math', 'Physics', 'CompSci']

index = mm.find_index(courses, 'Math')
print(index)

# If wanted to import everything from a file, could do:
# from my_module import *
'''However, this is the worst way to do it because now you can't tell what
came from the imported file and what didn't, which would make finding
and fixing problems much harder'''