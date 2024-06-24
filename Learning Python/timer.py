import time
def total(reps, func, *args, **kwargs):
    """
    计算函数运行时间
    """
    repslist = list(range(reps))
    start = time.time()
    for i in repslist:
        ret = func(*args, **kwargs)
    elapsed = time.time() - start
    return (elapsed, ret)

def bestof(reps, func, *args, **kwargs):
    """
    计算函数运行最快时间
    """
    best = 2 ** 32
    for i in range(reps):
        start = time.time()
        ret = func(*args, **kwargs)
        elapsed = time.time() - start
        if elapsed < best:
            best = elapsed
    return (best, ret)

def bestoftotal(reps1, reps2, func, *args, **kwargs):
    """
    计算函数运行最快时间
    """
    return bestof(reps1, total, reps2, func, *args, **kwargs)