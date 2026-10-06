import os 

# Handling Current Working Directory
cwd = os.getcwd() 
print("Current working directory:", cwd)

# Changing Current Working Directory

def current_path(label):
    print(f"Current Working Directory {label}")
    print(os.getcwd())
    print()

#current_path("before")
# os.chdir('../')
# current_path("after")
# os.chdir('/..')
# current_path("after change")
    
directory = "demo"

parent_dir = os.getcwd()

path = os.path.join(parent_dir, directory)

print("Path: ", path)

# os.mkdir(path)

# Listing out Files and Directories 

dir_list = os.listdir(parent_dir)

print("Files and directories ", parent_dir )
print(dir_list)

# File Metadata

file = "sample.txt"
stats = os.stat(file)
print(stats.st_size, "bytes")

print("OS name", os.name)



