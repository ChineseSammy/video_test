# coding:utf-8

import time
from celery import task


@task
def sayhello():
    print('ready...')
    time.sleep(2)
    print(111)