from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % filename)
    time_to_download = randint(2, 8)
    sleep(time_to_download)
    print('%s下载完成，耗费了%d秒.' % (filename, time_to_download))


def main():
    start = time()
    p1 = Process(target=download_task, args=('python.pdf', ))
    p1.start()
    p2 = Process(target=download_task, args=('I miss you.mp3', ))
    p2.start()
    p3 = Process(target=download_task, args=('Star War.mp4', ))
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    end = time()
    print('总共耗费了%2.f秒.' % (end - start))


if __name__ == "__main__":
    main()
