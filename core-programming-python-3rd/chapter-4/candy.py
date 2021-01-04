
"""
使用锁和信号量来模拟糖果机

threading包含两种信号量：Semaphore 和 BoundedSemaphore
BoundedSemphore的一个额外功能就是这个计数器的值永远不会超过它的初始值
内部有一个计数器： 计数器值 = 初始值 + release - acquare
"""

from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import ctime, sleep

lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX) # 糖果槽

# 添加糖果
def refill():
    lock.acquire()
    print('Refilling candy ...')
    try:
        candytray.release()
        # print(candytray._value())
        
    except ValueError:
        print('full, skipping')
    else:
        print('OK, inventory', str(candytray._value)) # 显示当前计数器的值
    lock.release()

def buy():
    lock.acquire()
    print('Buying candy ...')
    if candytray.acquire(False): # 当被阻塞的时候返回False
        print('OK, inventory', str(candytray._value))
    else:
        print('empty, skipping')
    lock.release()

def producer(loops):
    for i in range(loops):
        refill()
        sleep(randrange(3))

def consumer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))

def _main():
    print('Starting at: ', ctime())
    nloops = randrange(2, 6)
    print('The candy machine (full with %d bars)' % MAX)
    Thread(target=consumer, args=(randrange(nloops, nloops+MAX+2),)).start()
    Thread(target=producer, args=(nloops,)).start()

@register
def _atexit():
    print('all done at: ', ctime())

if __name__=='__main__':
    _main()



