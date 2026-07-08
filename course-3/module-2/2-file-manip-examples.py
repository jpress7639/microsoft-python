# Practical file manipulation examples

# File manipulation - the art of interacting with and managing files and directories on your computer, 
# is a cornerstone of Python programming

# Renaming Files
# e.g. images with generic names IMG_001.jpg, etc. 
# With Python - you can effortlessly rename a whole batch of files using a loop. 

# Python's os.rename() function takes over - smoothly performing the actual renaming operation behind the scenes.

# e.g. 
import os
for i in range(1, 11):
   old_name = f"IMG_{i:03d}.jpg"
   new_name = f"vacation_photo_{i}.jpg"
   os.rename(old_name, new_name)

# Expected result: The 10 image files (IMG_001.jpg through IMG_010.jpg) 
# would now be renamed vacation_photo_1.jpg through vacation_photo_10.jpg, giving them more meaningful names.

# we iterate over a range of numbers and construct the old and new file names using f-strings. 
# The os.rename() function then does the heavy lifting of renaming the files.


# Suppose you're on the hunt for all the PDF files within this vast directory.
# glob module steps in as your trusty search companion


# glob.glob() function acts like your magnifying glass, 
# efficiently scanning the current directory based on the clues you provide.
# By using a pattern like *.pdf, you're essentially saying, "Show me everyone with a PDF badge."

# e.g. 
# if your directory contains files like "report.pdf", "invoice.pdf", and "image.jpg", 
# glob.glob("*.pdf") will return a list containing "report.pdf" and "invoice.pdf"

# e.g. 
import glob
pdf_files = glob.glob("*.pdf")
for pdf_file in pdf_files:
   print(pdf_file)

# Expected output:
# report.pdf
# invoice.pdf

# ^ glob.glob("*.pdf") searches the current directory for all files ending with .pdf 
# and returns a list of matching file paths

# Organizing files based on criteria
# if you have a directory overflowing with images, each captured on a different date
# os and shutil modules - transforms this organizational dream into reality

# Python can dissect this filename, recognizing that it was taken on June 15, 2023. 
# It then systematically iterates through every file in the directory, performing this analysis for each image. 

# Working with file content
# Python also excels at interacting with the actual content within files

# The built-in open() function, 
# coupled with techniques like reading line by line or leveraging the csv module for structured data, 
# simplifies the extraction of valuable information

# The open() function, when used with the 'w' (write) or 'a' (append) mode, 
# provides the flexibility to write text or structured data to files

# Addressing potential challenges
# NOTE: it's important to be aware of and prepared for a few potential challenges that can arise
# File permission errors - one common hurdle

# To avoid this - use os.access() function to verify if you have the permissions

# Another hurdle - file encoding
# if you open a file with the wrong encoding, you might end up with garbled or unreadable text
# Python's open() function allows you to specify the encoding when opening a file, 
# ensuring that characters are interpreted correctly.

# Third -  unexpected situations can still occur
# A file you expect to be present might be missing, 
# or a network connection might drop while you're transferring a file
# try-except blocks, allows you to gracefully manage these unexpected events

