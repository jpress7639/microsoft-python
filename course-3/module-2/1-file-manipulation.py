# File manipulation for routine tasks

# Essential Python Modules for file operations: os, shutil, and glob

# File operations — the ability to create, read, write, move, and delete files and directories 
# keep countless Python applications running smoothly
# almost every Python program interacts with the file system in some way

# The os module
# os module is your direct line to the operating system
# giving you the ability to perform a wide range of actions on files and directories

# Creating and Deleting:
# os.mkdir() - to create new folders (or directories) using 
# os.rmdir() - lets you remove it
# os.mknod() - creates empty files
# os.remove() - removes a file

# Renaming and Moving:
# os.rename() - allows you to change a file's name or even move it to a different location

# Navigating the File System:
# os.getcwd() - tells you exactly where you are in the file system (your current working directory)
# os.chdir() - lets you move to a different location

# File Information:
# os.stat() - to give you detailed information about a file

# Path Manipulation: 
# os.path submodule helps you navigate these paths with ease
# os.path.join() - join different parts of a path together using 
# os.path.basename() -  extract just the filename from a path
# os.path.exists() - check if a particular path exists

# The shutil module 
# shutil module - as your helpful file management assistant
# shutil takes it a step further, offering convenient shortcuts for common tasks

# Copying files and directories:
# shutil.copy() - duplicates the file 
# shutil.copytree() - copies a folder and all its contents

# Moving files and directories: 
# shutil.move() - relocates a file or folder 

# Deleting files and directories:
# shutil.rmtree() is equivalent to clearing an entire section of the library

# The glob module
# glob module - a powerful search engine 
# allowing you to find files and directories that match certain patterns

# The heart of glob is the glob.glob() function, which accepts wildcard patterns.
# e.g. *.txt will find all files in a directory that end with .txt

# if you want to search in not only the current directory
# you can set a recursive argyment to Trye within the glob.glob() function as a second parameter
# e.g. glob.glob('**/*.py', recursive=True)

# Basic File Matching:
# glob.glob('*.txt') 
# This command finds all files in the current directory that end with the .txt extension. 
# It's a simple wildcard pattern match.

# Recursive Search: 
# glob.glob('**/*.txt', recursive=True) 
# This command searches for files ending in .txt not only in the current directory but also in all its subdirectories. 
# The recursive=True argument enables this deeper search.

# Multiple File Types:
# glob.glob('*.[txt,pdf]') 
# This command locates files in the current directory that have either a .txt or .pdf extension. 
# The square brackets define a set of possible matches.

# Complex Pattern Matching:
# glob.glob('data/202*/sales_*.csv')
# This command searches the "data" directory for files starting with "sales_" and ending with ".csv" within any subdirectories that start with 202 (so, 2024 or 2025, or even 2026-preview). 
# It combines wildcard characters with specific directory and filename patterns.


# Write a Python script to help lawyers find these PDF documents. The script should:
# Use the glob module to search the specified directory and all its subdirectories 
# for files with the .pdf extension and assign the result to a variable named pdf_files.

# Print pdf_files to display a list of the full file paths of all the 
# PDF documents found (code is provided).



import glob 
pdf_files = glob.glob('documents/**/*.pdf', recursive=True)
print(pdf_files)


# The portability debate
# it's important to acknowledge a potential drawback.
# Some developers argue that relying heavily on these built-in modules can 
# lead to code that's less portable across different operating systems.

# the way files and directories are organized and accessed can vary subtly between Windows, macOS, and Linux.

# If you're building an application that needs to run seamlessly on multiple platforms, 
# you might encounter situations where your code behaves differently 
# or even fails altogether due to these underlying differences.

# the benefits of using these modules far outweigh the potential portability challenges. 
# Python offers additional tools, like the pathlib module, 
# that provide a more object-oriented and potentially more portable approach to file operations.

# Unlocking file system mastery
# Mastering the os, shutil, and glob modules isn't just about learning a few new Python commands 
# – it's about unlocking a whole new level of control over your digital world. 
# These modules equip you with the keys to the file system kingdom, empowering you to navigate its intricate pathways,
#  manipulate its contents, and build applications that seamlessly interact with the world of files and directories.

