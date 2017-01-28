import os
import re
from sys import argv

# This is V1. Assumes one class per file. No nested classes.
# The existing doc string is only detected if it is directly underneath the class name (no vertical space)
# Docstrings are only detected if they are with double quotes not single quotes.
# This is very ugly fragile code. Enjoy!

INT_GUARENT = """
    I N T E R F A C E   G U A R A N T E E D
    ---------------------------------------
"""


def main():
    if len(argv) != 2:
        raise StandardError("Correct Usage: {0}: PATH_TO_FILE_TO_CONTRACTENATE".format(argv[0]))
    file_path = argv[1]
    if not os.path.exists(file_path):
        raise IOError("{0} file doesn't exist".format(file_path))

    current_class = None
    class_methods = {}

    with open(file_path, 'r') as filer:
        file_contents = filer.readlines()

    for i in range(len(file_contents)):
        if file_contents[i].startswith('class'):
            if '\"\"\"' not in file_contents[i+1]:
                current_class = get_class_name_from_line(file_contents[i])
                print current_class
                class_methods[current_class] = []
        elif file_contents[i].startswith('    def '):
            if file_contents[i].split('def')[1][1] == '_' or current_class is None:
                continue
            class_methods[current_class].append(file_contents[i].rstrip())

    for key, methods in class_methods.iteritems():
        # remove def
        methods = [re.sub('def ', '', x) for x in methods]

        # remove cls and self if exists
        methods = [re.sub('cls, ', '', x) for x in methods]
        methods = [re.sub('self, ', '', x) for x in methods]
        class_methods[key] = methods

    if len(class_methods) == 0:
        print "No Docstrings Needing\nExiting."
        return

    with open('temp_file', 'w') as filew:
        for line in file_contents:
            if line.startswith('class'):
                class_name = get_class_name_from_line(line)
                filew.write(line)
                filew.write(generate_docstring(class_methods[class_name]))
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


def get_class_name_from_line(line):
    return line.split(' ')[1].split('(')[0]

if __name__ == '__main__':
    main()
