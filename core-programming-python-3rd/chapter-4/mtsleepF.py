
"""
演示锁
"""

from atexit import register
from random import randrange
from threading import Thread, Lock, currentThread
from time import ctime, sleep


# 将默认输出改变为所有元素逗号分隔的字符串
class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)

lock = Lock()

# 随机数量线程（3-6）  每个线程上睡眠（2-4s）
loops = (randrange(2, 5) for x in range(randrange(3, 7)))
remaining = CleanOutputSet()

def loop(nsec):
    myname = currentThread().name
    lock.acquire()
    remaining.add(myname)
    print('[%s] Started %s' % (ctime(), myname))
    lock.release()
    sleep(nsec)
    lock.acquire()
    remaining.remove(myname)
    print('[%s] Completed %s (%d secs)' % (ctime(), myname, nsec))
    print('    (remaining: %s)' % (remaining or 'NONE'))
    lock.release()

def _main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()

@register
def _atexit():
    print('all none at: ', ctime())

if __name__=='__main__':
    _main()
