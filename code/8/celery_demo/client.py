# -*- coding: utf-8 -*-
from celery_app import task1
task1.add.apply_async(args=["http://xi.baidu.com"])
print 'hello world'