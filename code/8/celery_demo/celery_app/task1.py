# -*- coding: utf-8 -*-
import time
from celery_app import app
@app.task
def scan(url):
    print "scan %s" % url
    time.sleep(2)
