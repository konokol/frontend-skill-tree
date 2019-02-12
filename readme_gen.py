# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import re

out = 'README1.md'

def _get_ignore_content(path):
    ignore_file = open(path)
    return [line.strip('\n') for line in ignore_file.readlines() if not line.startswith('#') and line.strip('\n')]

def _gen_content():
    print('generating README...')
    li = _get_ignore_content('.content_ignore')
    print(li)
    pass

if __name__ == '__main__':
    _gen_content()
