#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import functools
from collections import OrderedDict
from operator import index
import os
import math
import yaml

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
docs_dir = os.path.join(project_root, 'docs')

# 加载配置文件
with open(os.path.join(script_dir, 'config.yaml'), 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

names = config['names']
orders = config['orders']

ignore = ['assets', 'css', 'img', 'none.md', 'index.md']

def read_docs(source, object_pairs_hook=OrderedDict):
    source = os.path.join(project_root, source)

    class OrderedLoader(yaml.Loader):
        pass

    def _construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))

    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        _construct_mapping)

    with open(source, 'r', encoding='utf-8') as file:
        data = yaml.load(file, OrderedLoader)
    return data

def mk_docs(content = ''):

    nav = list()
    docs_dir = os.path.join(project_root, 'docs')
    folders = os.listdir(docs_dir)
    folders.sort()
    for file in folders:
        if file not in ignore:
            doc = single_doc(os.path.join(docs_dir, file))
            if doc is not None:
                nav.append(doc)

    def cmp(m, n):
        i_m = math.inf
        i_n = math.inf
        for i, v in enumerate(orders):
            if v == list(m.keys())[0]:
                i_m = i
            if v == list(n.keys())[0]:
                i_n = i
        return i_m - i_n
    
    nav.sort(key=functools.cmp_to_key(cmp))
    content['nav'] = nav
    return content

def single_doc(file_path):
    if (os.path.isfile(file_path)):
        if os.path.basename(file_path) == 'none.md':
            return {'敬请期待': os.path.relpath(file_path, docs_dir)}

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f.readlines():
                    if (line.startswith("#")):
                        name = line[1:].strip()
                        print('add file', name)
                        return {name : os.path.relpath(file_path, docs_dir)}
                return {os.path.basename(file_path).split('.')[0] : os.path.relpath(file_path, docs_dir)}
        except (UnicodeDecodeError, IOError) as e:
            print(f"Error reading file {file_path}: {e}")
            return None

    else:
        dirs = list()
        files = os.listdir(file_path)
        files.sort()
        for file in files:
            child = single_doc(os.path.join(file_path, file))
            if child is not None:
                dirs.append(child)
        if not dirs:
            none_file = os.path.join(file_path, 'none.md')
            if os.path.exists(none_file):
                with open(none_file, 'r', encoding='utf-8') as f:
                    for line in f.readlines():
                        if (line.startswith("#")):
                            name = line[1:].strip()
                            return {'敬请期待': os.path.relpath(none_file, docs_dir)}
                    return {'敬请期待': 'none.md'}
        name = os.path.basename(file_path)
        return {names[name] if name in names else name : dirs}

def write_docs(target='mkdocs.yml', data = None, object_pairs_hook=OrderedDict):
    if data is not None:
        class OrderedDumper(yaml.Dumper):
            pass

        def _dict_representer(dumper, data):
            return dumper.represent_mapping(
                yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
                data.items())

        OrderedDumper.add_representer(object_pairs_hook, _dict_representer)

        target_path = os.path.join(project_root, target)
        if os.path.exists(target_path):
            os.remove(target_path)
        with open(target_path, 'w', encoding="utf-8") as file:
            yaml.dump(data, file, OrderedDumper, default_flow_style=False, allow_unicode=True)

if __name__ == "__main__":
    data = read_docs(source='mkdocs.yml')
    docs = mk_docs(data)
    docs['nav'][0]['首页'].insert(0, {'概述': 'index.md'})
    write_docs('mkdocs.yml', docs)