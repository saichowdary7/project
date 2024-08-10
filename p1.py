import os

all_entries = os.listdir("static/dataset")

files = [entry for entry in all_entries if not os.path.isdir(entry)]

print('Files:', files)


#for x in files:

path="static/dataset/"+files[0]
dir_list = os.listdir(path)
print("Files and directories in '", path, "' :")
# prints all files
for f in dir_list:
  x=f.split(".")
  
    
