


"""
习题4-8
"""
import sys
sys.path.append("..")
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
# nfuncs = range(len(funcs))

def _main():

    nProduce = randint(1, 4)
    nConsume = randint(1, 3)
    nloops = randint(2, 4)
    q = Queue(100)

    threads = []
    numThreads = nProduce + nConsume
    print(numThreads, nProduce, nConsume)
    # 创建生产者线程
    for i in range(nProduce):
        t = MyThread(funcs[0], (q, nloops), funcs[0].__name__)
        threads.append(t)
    
    for i in range(nConsume):
        t = MyThread(funcs[1], (q, nloops), funcs[1].__name__)
        threads.append(t)

    # for i in nfuncs:
    #     t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
    #     threads.append(t)
    
    for i in range(numThreads):
        # print('xxx')
        threads[i].start()
    
    for i in range(numThreads):
        threads[i].join()
    
    print("all done")

if __name__=='__main__':
    _main()


