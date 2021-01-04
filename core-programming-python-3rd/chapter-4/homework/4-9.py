

"""
创建一个线程来统计一组（可能很大）文本文件中包含多少行。
"""

import threading
import os

# 用于统计文本行数的线程类
class MyThreadLine(threading.Thread):
    def __init__(self, path):
        threading.Thread.__init__(self)  # 父类初始化
        self.path = path
        self.line = -1
    
    def run(self):
        # f = open(self.path)
        # data = f.read()
        # f.close()
        # num_lines = data.count('\n')
        num_lines = sum(1 for line in open(self.path, encoding='utf-8'))
        self.line = num_lines
        print(self.path.split('\\')[-1], self.line)


path = '..'

threadlist = []
def _main():

    filelist = os.listdir(path)
    print(filelist)
    for filename in filelist:
        if filename[-3:] == '.py':
            filepath = path + '\\' + filename
            # print(filepath)
            t = MyThreadLine(filepath) #创建线程类对象
            t.start() # 线程开始干活
            threadlist.append(t)
    
    for t in threadlist:
        t.join()

    linelist = []
    for t in threadlist:
        linelist.append([t.path.split('\\')[-1], t.line])
    print(linelist)



if __name__ == '__main__':
    _main()