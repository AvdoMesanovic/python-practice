# This will be the example that is being imported

'''Any code in the file that is receiving the import will also be run.
This print statement is to see when that happens.'''
print('Imported my_module...')

test = 'Test String'

def find_index(to_search, target):
  '''Find the index of a value in a sequence'''
  for i, value in enumerate(to_search):
    if value == target:
      return i
  
  return -1