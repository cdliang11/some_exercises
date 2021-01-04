
"""
使用thread模块提供的简单过线程机制
python3 将thread重命名为_thread
"""

import _thread
from time import sleep, ctime

def loop0():
    print('start loop 0 at: ', ctime())
    sleep(4)
    print('loop 0 done at: ', ctime())

def loop1():
    print('start loop 1 at: ', ctime())
    sleep(2)
    print('loop 1 done at: ', ctime())

def main():
    print('starting at: ', ctime)
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    sleep(6)
    print('all done at: ', ctime())

if __name__=='__main__':
    main()