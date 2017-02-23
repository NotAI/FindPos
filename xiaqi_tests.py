from nose.tools import *
import sys
from xiaqiClass import *
from cbrMath import *
import datetime
import time

print "Test Start"
startTime = time.clock()
#print startTime
# test Main
xiaqiIns = xiaqiClass();
xiaqiIns.start();
print "Test is end."

# test cbrMath
#result = find10([10,11,12,13,1,23,24])
#for i in range (0,10):
#    result = findpos3(10,2,30,40,5)
#print "resulst is %r" % result


endTime = time.clock()
print "CPU time is %r" % (endTime-startTime)
