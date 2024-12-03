# coding=utf-8
from datetime import datetime, timedelta

import time


def tday():
    date = datetime(2024, 11, 21)
    date = datetime.now()
    new_date = date + timedelta(days=180)
    # day1 = datetime(time.time())
    print(date)
    print(new_date)
    # print(day1)

if __name__ == "__main__":

    tday()







