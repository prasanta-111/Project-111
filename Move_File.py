import os
from_dir = "Downloads"
to_dir = "/Documents_Files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

path="/Downloads/feather"
root,ext = os.path.splitext(path)
print(list_of_files)


