
"""
生产者-消费者问题：在这个场景下，商品或服务的生产者生产商品，然后将
其放入到类似队列的数据结构中。生产商品的时间是不确定的，同样消费者
消费商品的时间也是不确定的。
"""

from random import randint
from time import sleep
from queue import Queue
from myThread import MyThread

def writeQueue(queue):
    print('Producing object for Q ...')
    queue.put('hat', 1)
    print('size now', queue.qsize())

def readQueue(queue):
    val = queue.get(1)
    print('consumed object from Q ... size now', queue.qsize())

def writer(queue, loops):
    for i in range(loops):
        writeQueue(queue)
        sleep(randint(1,3))

def reader(queue, loops):
    for i in range(loops):
        readQueue(queue)
        sleep(randint(2, 5))

funcs = [writer, reader]
nfuncs = range(len(funcs))

def _main():
    nloops = randint(2, 5)
    q = Queue(32)

    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)
    
    for i in nfuncs:
        threads[i].start()
    
    for i in nfuncs:
        threads[i].join()
    
    print("all done")

if __name__=='__main__':
    _main()