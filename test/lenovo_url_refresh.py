
# 刷新联想页面
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.insert(0,rootPath)

from  common.comfunction import OpenBrowser
from time import sleep
import threading


# 刷新联想页面多线程
def refresh_url():
    mode = 1
    url = 'http://124.77.120.212:8060/data/fetch?params=eyJmaWxlX2lkIjoiOTQzMDQiLCJ2aWV3X3R5cGUiOiJwcmV2aWV3IiwiZmlsZV9uYW1lIjoiMeWfuuehgO+8muS4h+S4iOmrmOalvOW5s+WcsOi1tyDigJTigJQgUmVkaXMg5Z+656GA5pWw5o2u57uT5p6ELnBkZiIsInJldiI6ImM5NWU4Mzc4YjE4MzQ1M2I5ODg0N2ZmYzk1YTU0YWUyIiwidXNlcl9pZCI6IjI3In0=&sign=61b27d1b7593de213f97a498b0b6549d'

    driver = OpenBrowser(mode)
    driver.get(url)
    for i in range(100):
        sleep(3)
        driver.refresh()
        print('刷新次数: %d'%i)
    sleep(7)
    driver.quit()

class myThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self) -> None:
        refresh_url()

def run_thread():
    a0 = myThread()
    a1 = myThread()
    a2 = myThread()
    a3 = myThread()
    a4 = myThread()
    a5 = myThread()

    a0.start()
    a1.start()
    a2.start()
    a3.start()
    a4.start()
    a5.start()

    a0.join()
    a1.join()
    a2.join()
    a3.join()
    a4.join()
    a5.join()


if __name__=='__main__':
    # refresh_url()
    run_thread()








