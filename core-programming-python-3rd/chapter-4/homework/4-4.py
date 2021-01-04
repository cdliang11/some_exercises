
"""
习题4-4：线程和文件
"""


import threading
import time
import random
import string


def randnGenString(numlines):
    with open('4-12.txt', 'w', encoding='utf-8') as f:
        for i in range(numlines):
            f.write(''.join(random.sample(string.ascii_letters + string.digits, 30)))
            f.write('\n')

# 统计字符
def counter(f):
    # global findstr, total_count
    count = 0
    for char in f:
        if findstr in char:
            count+=1
    total_count.append(count)

def _main():
    global total_count, findstr
    total_count = []
    threadnum = int(input('please input thread number: '))
    filename = '4-12.txt'
    findstr = 'a'
    text = open(filename).readlines()
    start = time.time()
    threads = []
    for i in range(threadnum):
        t = threading.Thread(target=counter, args=(text[i::threadnum],))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    
    end = time.time()
    print("multithread using %.5f seconds" % (end - start))
    print('string "%s" occurs %d times ' % (findstr, sum(total_count)))

    total_count = []
    start = time.time()
    counter(text)
    end = time.time()
    print("singlethread using %.5f seconds " % (end - start))
    print('string "%s" occurs %d times ' % (findstr, sum(total_count)))

if __name__ == '__main__':
    randnGenString(10000)
    _main()



