import os
import re
from sys import argv

# This is V1. Assumes one class per file. No nested classes.
# The existing doc string is only detected if it is directly underneath the class name (no vertical space)
# Docstrings are only detected if they are with double quotes not single quotes.
# This is very ugly fragile code. Enjoy!

INT_GUARENT = """
    I N T E R F A C E   G U A R E N T E E D
    ---------------------------------------
"""


def main():
    if len(argv) != 2:
        raise StandardError("Correct Usage: {0}: PATH_TO_FILE_TO_CONTRACTENATE".format(argv[0]))
    file_path = argv[1]
    if not os.path.exists(file_path):
        raise IOError("{0} file doesn't exist".format(file_path))

    found_class = False
    needs_doc_string = False
    file_contents = None
    methods = []

    with open(file_path, 'r') as filer:
        file_contents = filer.readlines()

    for i in range(len(file_contents)):
        if file_contents[i].startswith('class'):
            found_class = True
            if '\"\"\"' not in file_contents[i+1]:
                needs_doc_string = True
        elif file_contents[i].startswith('    def ') and found_class:
            if file_contents[i].split('def')[1][1] == '_':  # designated private method
                continue
            methods.append(file_contents[i].rstrip())

    # remove dev
    methods = [re.sub('def ', '', x) for x in methods]

    # remove cls and self if exists
    methods = [re.sub('cls, ', '', x) for x in methods]
    methods = [re.sub('self, ', '', x) for x in methods]

    if not needs_doc_string:
        print "No docstring needed"
        return

    with open('temp_file', 'w') as filew:
        for line in file_contents:
            if line.startswith('class'):
                filew.write(line)
                filew.write(generate_docstring(methods))
            else:
                filew.write(line)

    os.rename('temp_file', file_path)


def generate_docstring(methods):
    docstring = '    \"\"\"\n    desc\n'
    docstring += INT_GUARENT
    for i in range(len(methods)):
        docstring += methods[i]
        docstring += '\n'
        docstring += '        -- \n'
        if i < len(methods) - 1:
            docstring += '\n'
    docstring += '    \"\"\"\n'
    return docstring

if __name__ == '__main__':
    main()
