"""
递归 Relaod 所有模块
"""

import types
from imp import reload


def status(module):
    """
    打印模块状态
    """
    print('reloading ' + module.__name__)


def tryreload(module):
    try:
        reload(module)
    except:
        print('Failed to reload' + module.__name__)


def transitive_reload(module, visited):
    """
    递归 Relaod 所有模块
    """
    if not module in visited:
        status(module)
        tryreload(module)
        visited[module] = True
        for attrobj in module.__dict__.values():
            if type(attrobj) == types.ModuleType:
                transitive_reload(attrobj, visited)


def reloadall(*modules):
    visited = {}
    for module in modules:
        if type(module) == types.ModuleType:
            transitive_reload(module, visited)


def my_tester(reloader, modname):
    """
    测试函数
    """
    import sys, importlib
    if len(sys.argv)>1: modname = sys.argv[1]
    module = importlib.import_module(modname)
    reloader(module)


if __name__ == '__main__':
    my_tester(reloadall, 'formats')
    import Py