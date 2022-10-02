# usr/bin/env python3
# -*- codind:utf-8 -*-
import functools
from importlib.abc import Loader
import yaml
from collections import OrderedDict
import os
import math

ignore = ['assets', 'css', 'img']
names = {
    'CS': 'CS理论基础',
    'Java': 'Java基础',
    'Kotlin': 'Kotlin基础',
    'tools': '工具与工程化'
}

def read_docs(source, object_pairs_hook=OrderedDict):
    class OrderedLoader(yaml.Loader):
        pass

    def _construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))

    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        _construct_mapping)

    with open(source, 'r') as file:
        data = yaml.load(file, OrderedLoader)
    return data

def mk_docs(content = ''):

    nav = list()
    for file in os.listdir('docs'):
        if file in ignore:
            pass
        else:
            doc = single_doc('./docs/' + file)
            if doc is not None:
                nav.append(doc)

    pre_nav = content['nav']

    def cmp(m, n):
        i_m = math.inf
        i_n = math.inf
        for i, v in enumerate(pre_nav):
            if list(v.keys())[0] == list(m.keys())[0]:
                i_m = i
            if list(v.keys())[0] == list(n.keys())[0]:
                i_n = i
        print("m", m)
        print("n", n)
        print("i_m,i_n", i_m, i_n)
        return i_m - i_n
    
    nav.sort(key=functools.cmp_to_key(cmp))
    content['nav'] = nav
    return content

def single_doc(file_path):
    if (os.path.isfile(file_path)):
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                if (line.startswith("#")):
                    name = line[1:].strip()
                    print('add file', name)
                    return {name : os.path.relpath(file_path, './docs')}
            return {os.path.basename(file_path).split('.')[0] : os.path.relpath(file_path, './docs')}
    else:
        dirs = list()
        for file in os.listdir(file_path):
            child = single_doc(file_path + '/' + file)
            if child is not None:
                dirs.append(child)
        name = os.path.basename(file_path)
        return {names[name] if name in names else name : dirs}

def write_docs(target='mkdocs.yml', data = None, object_pairs_hook=OrderedDict,):
    if data is None:
        pass
    else:
        class OrderedDumper(yaml.Dumper):
            pass

        def _dict_representer(dumper, data):
            return dumper.represent_mapping(
                yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
                data.items())

        OrderedDumper.add_representer(object_pairs_hook, _dict_representer)
    
        if os.path.exists(target):
            os.remove(target)
        with open(target, 'w', encoding="utf-8") as file:
            yaml.dump(data, file, OrderedDumper, default_flow_style=False, allow_unicode=True)

if __name__ == "__main__":
    data = read_docs(source='mkdocs.yml')
    docs = mk_docs(data)
    write_docs('mkdocs copy.yml', docs)