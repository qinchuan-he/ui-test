# -*- coding: utf-8 -*-
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import requests



# 批量任务线程池版
def batch_processing(task_func, args_list): # 参数: 函数名字 函数所需参数
    if len(args_list) == 1:
        return [task_func(*args_list[0])]
    else:
        results = []
        with ThreadPoolExecutor(max_workers=5) as executor:  # 线程池
            future_set = set()
            for args in args_list:
                future = executor.submit(task_func, *args)
                future_set.add(future)

            for future in as_completed(future_set):  # 阻塞等待所有任务完成
                try:
                    result = future.result()
                except Exception as e:
                    print(e)
                else:
                    results.append(result)
            executor.shutdown()
        print(results)
        return results





def test(value1, value2=None):
    start=time.time()
    for i in range(50):
        url = 'https://cyprex.fir.ai/api/account/user/judge/register/'
        data_1 = {'key':'mobile','value':'13248131618'}
        res = requests.post(url=url,data=data_1)
    use_time=time.time()-start
    return use_time

#
def test_result(future):
    print(future.result())


if __name__ == "__main__":
    import numpy as np
    from concurrent.futures import ThreadPoolExecutor
    threadPool = ThreadPoolExecutor(max_workers=4,thread_name_prefix='a_')
    # future = threadPool.submit(test, 1)
    a=0
    for i in range(2):
        future = threadPool.submit(test, i)
        future.add_done_callback(test_result)
    threadPool.shutdown(wait=True)
    # print(a)





