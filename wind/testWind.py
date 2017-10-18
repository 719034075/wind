#!usr/bin/python
#-*- coding:utf-8 _*-

from WindPy import w
from datetime import *
import matplotlib.pyplot as plt
from datetime import datetime
w.start()
data=w.wsd("600000.SH","open,close,low,high,amt", 'LQ1')
print(data)
w.stop()