from time import time,sleep
from random import randint

def download_task(filename):
    print('start downloading%s...' % filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print('%sdownload! It cost %d seconds' % (filename, time_to_download))

def main():
    start = time()
    download_task('Python从入门到入坟.pdf')
    download_task('捶桌.gif')
    download_task('No one survived.mp4')
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))

if __name__ == "__main__":
    main()