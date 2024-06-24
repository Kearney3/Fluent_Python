import time


def total(func, *args, **kwargs):
    """
    计算函数运行时间
    """
    _reps = kwargs.pop('reps', 1000)
    repslist = list(range(_reps))
    start = time.time()
    for i in repslist:
        ret = func(*args, **kwargs)
    elapsed = time.time() - start
    return (elapsed, ret)


def total2(func, *args, _reps=1000, **kwargs):
    """
    计算函数运行时间
    """
    repslist = list(range(_reps))
    start = time.time()
    for i in repslist:
        ret = func(*args, **kwargs)
    elapsed = time.time() - start
    return (elapsed, ret)


def bestof(func, *args, **kwargs):
    """
    计算函数运行最快时间
    """
    _reps = kwargs.pop('reps', 5)
    best = 2 ** 32
    for i in range(_reps):
        start = time.time()
        ret = func(*args, **kwargs)
        elapsed = time.time() - start
        if elapsed < best:
            best = elapsed
    return (best, ret)


def bestoftotal(func, *args, **kwargs):
    """
    计算函数运行最快时间
    """
    reps1 = kwargs.pop('reps1', 5)
    return min(total(func, *args, **kwargs) for i in range(reps1))
