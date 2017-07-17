# -*- coding: utf-8 -*-

BROKER_URL = 'redis://127.0.0.1:6379'               # 指定 Broker
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'  # 指定 Backend
CELERY_TIMEZONE='Asia/Shanghai'                     # 指定时区，默认是 UTC
# CELERY_TIMEZONE='UTC'
CELERY_IMPORTS = (                                  # 指定导入的任务模块
    'celery_app.task1'
)