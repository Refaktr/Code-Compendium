"""
Python - File Handling - Writing a File

Writing text to a file.

Keywords:
    open
    write
    encoding
    UTF-8
    file handling
"""

file_location = "/path/to/file.txt"


# ------------------------------------------------------------
# Basic file writing
# ------------------------------------------------------------

# "w" means write mode.
# The file is automatically closed when the "with" block ends.

with open(file_location, "w") as file:
    file.write("Text content or variable holding text.")


# ------------------------------------------------------------
# Writing using UTF-8 encoding
# ------------------------------------------------------------

# Explicitly specifying UTF-8 ensures the text is written
# using the same encoding regardless of the operating system.

with open(file_location, "w", encoding="utf-8") as file:
    file.write("Text content or variable holding text.")


# ------------------------------------------------------------
# Important
# ------------------------------------------------------------

# "w" will overwrite the existing contents of the file.
#
# If the file already contains:
#
#     Hello World
#
# and we run:
#
#     file.write("Goodbye")
#
# the file will contain:
#
#     Goodbye
#
# Use "a" (append mode) when you want to add content to the
# existing file instead of replacing it.
