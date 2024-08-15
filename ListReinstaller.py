# This will be used as a data storing program that will be able to take a python list, store it for later, and reintergrate it back into a python list
file = open("file.txt","r+")
lines = []



x = 0 # x being the line number

def memory_import():
  for line in file.readlines():

    line = line.replace('\x00', '') # replaces null characters with nothing just in case
    
    
    lines.append(line)
    
  var1 = fix_list(list(lines[x]))
  
  

def fix_list(list):
  fixed_list = []
  fixed_item = ''
  for item in list:

    if item == ',':
      fixed_list.append(fixed_item)
      fixed_item = ''
      
    elif item == ' ' or item == '[' or item == ']':
      continue
      
    else:
      fixed_item += item

  if fixed_item != '':
    fixed_list.append(fixed_item)
    
  return fixed_list
      
def memory_export():
  var2 = ['Sam','James','Jack','Josh'] #example

  with open('file.txt', 'w') as y:
    pass
    
  file.writelines(str(var2))
  
  
  


memory_import()
memory_export()

