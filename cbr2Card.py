import sys
import os
def toString(x):
    return {
        9: 'T',
        10:'J',
        11:'Q',
        12:'K',
        0: 'A',
    }.get(x,str(x+1))
def printPos(peopleNum,c0,c1):
    script_dir = os.path.dirname(__file__)
    fileStr = "lib/2c"+str(peopleNum)+"p.txt"
    rel_path = os.path.join(script_dir,fileStr)

    try :
        filePointer = open(rel_path,'r')
    except :
        print "Unexpect error to open file:", sys.exc_info()[0]
        sys.exit(0)

    # change c0 c1 to string in file to compare
    sameSuit = (c0.suit==c1.suit)  
    numb0 = c0.numb - 1
    numb1 = c1.numb - 1


    if numb0 != 0 and (numb0 <= numb1 or numb1==0):
        s = toString(numb0) + toString(numb1)
    else:
        s = toString(numb1) + toString(numb0)

    if sameSuit :
        s = s+'s'
    cnt = 0
    for line in filePointer:
        cnt += 1
        strList = line.split(' ')

        if strList[0] == s:
            print " CBR, you card is [%r], numb %r out of 169." % (s,cnt)
            print " CBR, you card win  rate is  %r percent." % strList[1]
            print " CBR, you card drew rate is  %r percent." % strList[2]
        

