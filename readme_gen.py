# !/usr/bin/env python3
# -*- coding:utf-8 -*-

import re
import os

out = 'README1.md'
ignored = 'aaa'

def _get_ignore_content(path):
    ignore_file = open(path)
    return [line.strip('\n') for line in ignore_file.readlines() if not line.startswith('#') and line.strip('\n')]

def _gen_content(file):
    print('generating README...')
    print(ignored)



if __name__ == '__main__':
    ignored = _get_ignore_content('.content_ignore')
    _gen_content('.')
