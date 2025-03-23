# usr/bin/env python3
# -*- codind:utf-8 -*-

import os
import re
import sys, getopt
from urllib.parse import quote
from shutil import copyfile

_out = "PATH.md"
_backup = 'README.md.bkp'

def _write(path = '.', out = 'PATH.md'):
    if os.path.isdir(path):
        for f in os.listdir(path):
            _write(path + '/' + f, out)
    else:
        suffix = os.path.splitext(path)[-1]
        basename = os.path.splitext(os.path.basename(path))[0]
        if suffix == '.md':
            with open(out, 'a') as out_file:
                str = '- [' + basename + '](' + quote(path) +')\n'
                out_file.write(str)    
    
def write_path(out = 'PATH.md'):
    with open(out, 'w') as file:
        file.write('')
    _write('.', out)

def repair(out = "README.md.rpr"):
    write_path()
    copyfile('README.md', _backup)
    index = {}
    with open(_out, 'r') as file:
        for line in file.readlines():
            if len(line.strip()) and re.match(r'- \[.*\]\(.*\)', line):
                l = line.strip()
                name = line[l.find('[') + 1: l.find(']')] + '.md'
                index[quote(name)] = line
    with open(_backup, 'r') as bkp:
        with open(out, 'w') as target:
            target.write('')
            for line in bkp.readlines():
                if len(line.strip()) and re.match(r'- \[.*\]\(.*\)', line):
                    l = line.strip()
                    name = line[l.find('[') + 1: l.find(']')] + '.md'
                    if quote(name) in index:
                        target.write(index[quote(name)])
                else:
                    target.write(line)

def append(out = 'README.md.apd'):
    tmp = 'append.md.tmp'
    write_path(tmp)
    readme = None
    path = None
    with open('README.md') as file:
        readme = file.readlines()
    with open(tmp, 'r+') as file:
        path = file.readlines()
        file.seek(0)
        file.writelines(set(path).difference(set(readme)))
        file.truncate()

def _parse_args(args = []):
    filename = os.path.basename(__file__)
    hint = f'''usage: {filename} <command> [-o <target>] [-h]
    repair      Repair bad path in README.md, or write into specific file with -o.

    write       Generate path for the files ended with '.md'. Use -o to specific target file, 
                or write into 'PATH.md' by default.

    append      Find new files ended with '.md' not included in 'README.md' and write their 
                path into 'APPENDED.md' by default or specific file with -o argment. 

    {filename} -h show all commands
    '''

    ops = ['repair', 'write', 'append']
    if not len(args):
        print(hint)
        exit(1)
    else:
        op = args[0]
        if not op in ops:
            print(hint)
            exit(1)
        args = args[1:]
        try:
            opts, args = getopt.getopt(args, 'ho:', ['out='])
            out = _out
            for opt, arg in opts:
                if opt == '-h':
                    print(hint)
                elif opt in ('-o', '--out'):
                    out = arg
                    print("write into file: " + out)
                else:
                    print('******')
            print('start ' + op)
            if op == 'repair':
                repair(out)
            elif op == 'write':
                write_path()
            elif op == 'append':
                append()
        except getopt.GetoptError as e:
            print(e)
            print(hint)
            pass
        
if __name__ == "__main__":
    _parse_args(sys.argv[1:])
    