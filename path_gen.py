# usr/bin/env python3
# -*- codind:utf-8 -*-

import os
from urllib.parse import quote

out = "README1.md"

def write(path = '.'):
    if os.path.isdir(path):
        for f in os.listdir(path):
            write(path + '/' + f)
    else:
        suffix = os.path.splitext(path)[-1]
        basename = os.path.splitext(os.path.basename(path))[0]
        if suffix == '.md':
            with open(out, 'a') as out_file:
                str = '- [' + basename + '](' + quote(path) +')\n'
                out_file.write(str)
    

if __name__ == "__main__":
    with open(out, 'w') as file:
        file.write('')
    write('.')