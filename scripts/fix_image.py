# usr/bin/env python3
# -*- codind:utf-8 -*-
from email.mime import image
import os
import re
import shutil
import sys

def fix_file_image_path(root, file):
    if not file.endswith('.md'):
        print('ignore file', file)
        return False
    dirs = os.path.join('build', root)
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    source_file = os.path.join(root, file)
    target_file = 'build/' + source_file
    with open(source_file, 'r', encoding='utf-8') as source, open(target_file, 'w', encoding='utf-8') as target:
        for line in source:
            images = re.findall(r'(?:!\[.*\]\((.*?)\))', line)
            for image in images:
                if re.match(r'^https?:/{2}\w.+$', image) is None:
                    dirname, filename = os.path.split(image)
                    realpath = os.path.relpath('./docs/img/'  + filename, root + file)
                    print('fix image path', image, ' to ', realpath)
                    line = line.replace(image, realpath)
            target.write(line)
        bak_dir = 'build/backup/'
        if os.path.exists(bak_dir):
            shutil.rmtree(bak_dir)
        os.mkdir(bak_dir)
        shutil.move(source_file, bak_dir)
        shutil.move(target_file, root)

def fix_image_path(path='docs'):
    for root, dirs, files in os.walk(path, topdown=False):
        for file in files:
            fix_file_image_path(root, file)

if __name__ == '__main__':
    if(len(sys.argv) > 1):
        file_path, filename = os.path.split(sys.argv[1])
        print(file_path, filename)
        fix_file_image_path(file_path, filename)
    else:
        fix_image_path('./docs/')