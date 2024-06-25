"""
递归 Relaod 所有模块
"""

import types
from importlib import import_module, reload
# from imp import reload

def status(module):
    """
    打印模块状态
    """
    print('reloading ' + module.__name__)


def tryreload(module):
    try:
        # import_module(module)
        reload(module)
    except:
        print('Failed to reload' + module.__name__)


def transitive_reload(modules, visited):
    """
    递归 Relaod 所有模块
    """
    for module in modules:
        if type(module) == types.ModuleType and not module in visited:
            status(module)
            tryreload(module)
            visited.add(module)
            transitive_reload(module.__dict__.values(), visited)


def transitive_reload2(modules, visited):
    """
    递归 Relaod 所有模块
    """
    for module in modules:
        if type(module) == types.ModuleType and not module in visited:
            status(module)
            tryreload(module)
            visited.add(module)
            transitive_reload2(module.__dict__.values(), visited)

def transitive_reload3(modules, visited):
    """
    递归 Relaod 所有模块
    """
    while modules:
        module = modules.pop()
        status(module)
        tryreload(module)
        visited.add(module)
        modules.extend(m for m in module.__dict__.values() if type(m) == types.ModuleType and not m in visited)



def reloadall(*modules):
    transitive_reload(modules, set())

def reloadall2(*modules):
    transitive_reload(list(modules), set())


def reloadall3(*modules):
    transitive_reload(list(modules), set())




def my_tester(reloader, modname):
    """
    测试函数
    """
    import sys, importlib
    if len(sys.argv) > 1: modname = sys.argv[1]
    module = importlib.import_module(modname)
    reloader(module)


if __name__ == '__main__':
    my_tester(reloadall, 're')
    # my_tester(reloadall, 'dir1.main')
    print('-'*50)
    my_tester(reloadall2, 're')
    # my_tester(reloadall2, 'dir1.main')
    print('-'*50)
    my_tester(reloadall3, 're')
    # my_tester(reloadall3, 'dir1.main')
    # my_tester(reloadall, 'formats')
