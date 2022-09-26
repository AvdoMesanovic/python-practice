'''Showcasing some of the many modules from the standard library'''

import random # Used for random values
import math # Used for common mathematical calculations
import datetime # Allows you to work with dates and times
import calendar # Similar but different to datetime
import os # Gives access to the underlying operating system

courses = ['History', 'Math,' 'Physics', 'CompSci']

random_course = random.choice(courses)

print(random_course) # Will randomly select a course from courses variable

# ///////////////////////////////////////////////////////////////////////

rads = math.radians(90)

print(rads)
print(math.sin(rads)) # Will print the sin of desred variable

# ///////////////////////////////////////////////////////////////////////

today = datetime.date.today() # Sets variable to current date IRL
print(today)

print(calendar.isleap(2017)) # Determines if a year is a leap year (True)
print(calendar.isleap(2020)) # False

# ///////////////////////////////////////////////////////////////////////

print(os.getcwd()) 
# Prints out current working directory where this script is located

print(os.__file__) 
# Prints out dunder file attribute
# Dunder just means double underscore


