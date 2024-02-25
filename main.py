import os


# to get the curent directory
curent_dir = os.getcwd()
print(curent_dir)

# to change directory to the root
os.chdir("/")
print(os.getcwd()) #print curent dir



# to change directory to ...
os.chdir("/Users/macintosh/python_projects/os_functions")
print(os.getcwd()) #print curent dir

# to see what is in curent dir
files = os.listdir(os.getcwd())
print(files)

# to see what is inside a giving directory
files = os.listdir("/Users/macintosh")
print(files)

# to create a directory if it doesnt exist(alsocheck: os.mkdir("test")
os.makedirs("/Users/macintosh/python_projects/os_functions/aaa",exist_ok=True)

# to create directory and subdirectory (directory aaa then inside bbb inside ccc
os.makedirs("/Users/macintosh/python_projects/os_functions/aaa/bbb/ccc",exist_ok=True)

# to delete a single directory
os.chdir("/Users/macintosh/python_projects/os_functions/aaa/bbb")
os.rmdir("ccc")

# to combine file name with path
os.chdir("/Users/macintosh/python_projects/os_functions") #change dir to os_functions
cur_dir = os.getcwd() # get curent dir in variable
file1 = "text.txt" # get file name in a variable
combined = os.path.join(cur_dir,file1) # get the full path with file name in a variable
print(combined) # also: os.path.join(cur_dir,"folder1","OneMoreFolder",file1)

# to check if the path exist
path_exist = (os.path.exists("/Users/macintosh/python_projects/os_functions"))
print(path_exist) # will return True or False

# to check if the exist path is a file or folder
path_file = "/Users/macintosh/python_projects/os_functions/test.txt"
check_file = (os.path.isfile(path_file))
print (check_file) # will output True if it s a file (also we can replace isfile by isdir)

# to get info about a file
info_file = (os.stat(path_file))
print (info_file) # will print all file info

size_file = (os.stat(path_file).st_size)
print(size_file) # will print only file size

# to get the path of envirement variables (useful for prog to work on any computer)
v1= os.environ.get("PATH")
print(v1)

# to get the username login on the computer
user_name= (os.getlogin())
print(user_name)