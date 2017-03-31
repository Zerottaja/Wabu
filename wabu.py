import random
import time
import os


def wabu():
    while True:
        sec = random.randint(0, 59)
        min = random.randint(0, 59)
        h = random.randint(0, 23)
        kk_list = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP",
                   "OCT", "NOV", "DEC"]
        kk_num = int(time.localtime()[1])
        kk = kk_list[kk_num - 1]
        day = str(time.localtime()[2])
        year = str(time.localtime()[0])

        os.system("date -s '{} {} {} {}:{}:{}'".format(day, kk, year, h, min, sec))
        time.sleep(3600)
    # date -s "2 OCT 2006 18:00:00"
    # os.system("bashCommand")

wabu()