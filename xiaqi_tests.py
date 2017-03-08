import sys
import datetime
import time
import os
from nose.tools import *
from xiaqiClass import *
from cbrMath import *
from send_email import *

print "Test Start"
startTime = time.clock()

# test Main
#xiaqiIns = xiaqiClass();
#xiaqiIns.start();
try :
    xiaqiIns = xiaqiClass();
    xiaqiIns.start();
except :
    print "Unexpected error:", sys.exc_info()[0]
    print "going to send email..."
    print "Please don't print CTRL+C !!!"
    user = "sanguozhizhang@gmail.com"
    pwd = "cbrcknhws"
    recipient = ['hwslqc@gmail.com','kainan.chen.cn@gmail.com','371967442@qq.com']
    subject = "CBR's program record"
    endTime = time.clock()
    body = "CBR program running time is %r seconds\r\n" % (endTime-startTime)

    script_dir = os.path.dirname(__file__)
    timeList = time.ctime().split(' ')
    fileName = timeList[4]+timeList[1]+timeList[2]+".txt"
    fileStr = "data/"+timeList[4]+timeList[1]+timeList[2]+".txt"
    filePath = os.path.join(script_dir,fileStr)
    send_email(user, pwd, recipient, subject, body, fileName, filePath)

print "CPU time is %r" % (endTime-startTime)
