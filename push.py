#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import subprocess

def main():
    println('push to GitHub')
    subprocess.check_output(['git', 'push', 'github'])
    println('push to Gitlab')
    subprocess.check_output(['git', 'push', 'gitlab'])

if __name__ == '__main__':
    main()
