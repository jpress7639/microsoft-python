# Import the Argparse, OS, and glob packages for Later
import argparse
import glob
import os


# Instantiate the Argparse package.
parser = argparse.ArgumentParser()
# Create an argument called listfiles that prints specific file types:
parser.add_argument("--listfiles", help="Lists specific files within the directory.")
# Create an argument called long that prints all file types:
parser.add_argument("--long", help="Lists all files within the directory.")
args = parser.parse_args()

# Call in terminal as --Listfiles LISTFILES
if args.listfiles: # Specify python files only:
    listed_files = [f for f in glob.glob("*.py")]
    print(listed_files)

# Call in terminal as --long LONG
if args.long:
    # Extract all files:
    listed_files = os.listdir()
    print(listed_files)
