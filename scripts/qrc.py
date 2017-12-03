#! /usr/bin/env python3

# Generate a Qt Resource file from the contents of a list of directories
# qrc.py <dir1> <dir2> ...

import os
import os.path

root_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

dirname = os.path.join(root_dir, 'src')
file_list = []

for root, dirs, files in os.walk(dirname):
    file_list += [os.path.relpath(os.path.join(root, filename), dirname)
                  for filename in files]

file_list.sort()

contents = '<!DOCTYPE RCC>\n<RCC version="1.0">\n\n'

contents += '<qresource>\n'

for filename in file_list:
    if (filename.endswith('.js') or filename.endswith('.qml') or
            filename.endswith('.otf') or filename.endswith('.ttf') or
            filename.endswith('.png') or filename.endswith('.jpg') or
            filename.endswith('.jpeg') or filename.endswith('.svg') or
            filename.endswith('qmldir')):
        contents += '\t<file>' + filename + '</file>\n'

contents += '</qresource>\n\n</RCC>\n'

with open(os.path.join(dirname, 'app.qrc'), 'w') as f:
    f.write(contents)
