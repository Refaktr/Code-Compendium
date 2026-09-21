"""
Python - File Handling - Opening a File

Opening and reading text files.

Keywords:
    open
    read
    encoding
    UTF-8
    file handling
"""

file_location = "/path/to/file.txt"


# ------------------------------------------------------------
# Basic file opening
# ------------------------------------------------------------

# "r" means read mode.
# The file is automatically closed when the "with" block ends.

with open(file_location, "r") as file:
    file_contents = file.read()


# ------------------------------------------------------------
# Opening a file using UTF-8 encoding
# ------------------------------------------------------------

"""
Using UTF-8 explicitly is recommended when working with text
files because it makes the expected text encoding clear and
avoids relying on the operating system's default encoding.
"""

with open(file_location, "r", encoding="utf-8") as file:
    file_contents = file.read()


# ------------------------------------------------------------
# Useful open() modes
# ------------------------------------------------------------

"""
"r"  = Read
"w"  = Write (overwrites the existing file)
"a"  = Append (adds to the end of the file)
"x"  = Create a new file, failing if it already exists

Commonly used:
    open(file_location, "r", encoding="utf-8")
"""