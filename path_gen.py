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
        s = os.path.splitext(path)
        if s[-1] == '.md':
            with open(out, 'a') as out_file:
                str = '- [' + s[-2] + '](' + quote(path) +')\n'
                out_file.write(str)
    

if __name__ == "__main__":
    os.remove(out)
    write('.')