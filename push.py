#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import subprocess

def main():
    print('push to GitHub')
    subprocess.check_output(['git', 'push', 'github'])
    print('\npush to Gitlab')
    subprocess.check_output(['git', 'push', 'gitlab'])

if __name__ == '__main__':
    main()
