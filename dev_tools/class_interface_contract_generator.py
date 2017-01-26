import os
from sys import argv

# This is V1. Assumes one class per file. No nested classes.
# The existing doc string is only detected if it is directly underneath the class name (no vertical space)
# Docstrings are only detected if they are with double quotes not single quotes.

INT_GUARENT = """
    I N T E R F A C E S  G U A R E N T E E D\n
    ----------------------------------------\n
"""


def main():
    if len(argv) != 2:
        raise StandardError("Correct Usage: {0}: PATH_TO_FILE_TO_CONTRACTENATE".format(argv[0]))
    file_path = argv[1]
    if not os.path.exists(file_path):
        raise IOError("{0} file doesn't exist".format(file_path))

    class_name = None
    found_class = False
    needs_doc_string = False
    file_contents = None

    with open(file_path, 'r') as filer:
        file_contents = filer.readlines()

    for i in range(len(file_contents)):
        if file_contents[i].startswith('class'):
            class_name = file_contents[i].split(' ')[1].split('(')[0]
            if '\"\"\"' not in file_contents[i+1]:
                needs_doc_string = True

    print class_name
    print needs_doc_string



if __name__ == '__main__':
    main()
