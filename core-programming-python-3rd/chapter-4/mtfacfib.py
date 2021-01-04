
"""
使用myThread类实现斐波那契、阶乘、累加
"""

from myThread import MyThread
from time import ctime, sleep

#斐波那契
def fib(x):
    sleep(0.005)
    if x < 2:
        return 1
    return (fib(x-2) + fib(x-1))

# 阶乘
def fac(x):
    sleep(0.1)
    if x < 2:
        return 1
    return (x +  fac(x - 1))

# 累加
def _sum(x):
    sleep(0.1)
    if x < 2:
        return 1
    return (x + _sum(x - 1))

funcs = (fib, fac, _sum)
n = 12

def main():
    nfunc = range(len(funcs))
    print(nfunc)
    print('----single thread----')
    for i in nfunc:
        print('starting', funcs[i].__name__, 'at: ', ctime())
        print(funcs[i](n))
        print(funcs[i].__name__, 'finished at: ', ctime())
    
    print('\n----multiple threads----')
    threads = []
    for i in nfunc:
        t = MyThread(funcs[i], (n,), funcs[i].__name__)
        threads.append(t)
    for i in nfunc:
        threads[i].start
    for i in nfunc:
        threads[i].join()
        print(threads[i].getResult())
    print('all done')

if __name__=='__main___':
    main()