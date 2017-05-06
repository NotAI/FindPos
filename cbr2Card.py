import sys
import os
import random

type0 = ["3009","3008","3007"]
type1 = ["2009","2008","2007","2006","2005","2004"]
type2 = ["1009","1008","1007","1006"]
type3 = ["0149","0049"]
type4 = ["0139","0039"]
type5 = ["0109","0108","0107","0148","0136","0146"]
type6 = ["0129","0029","0119","0019","0148","0048","0138","0038","0128","0028","0147","0047","0137","0037"]
type7 = ["0145","0144","0143","0142","0141"]        
type8 = ["0134","0133","0132"]        
type9 = ["0124","012","0122"]        
type10 = ["0045","0044","0043"]

def type0Algo(randBB):
    print "--> Raise no matter location, doc didn't say raise how much ????BB"
    print "--> if (other people raise again):"
    if (randBB<50):
        print "-->    AA,KK continue raise 1/3BB, QQ consider people strength, call or raise"
    else:
        print "-->    AA,KK continue raise 1/2BB, QQ consider people strength, call or raise"
            
def type1Algo(loc,randNum,randBB):
    if (loc==0):    # first 1/3 location
        if (randNum < 70):
           print "--> Raise, how much????"
        else :
           print "--> Call"
    else:            # middle or late location
        if (randNum < 80):
           print "--> Raise, "
        else :
           print "--> Call"

        if (randBB < 50):
           print "--> 3BB."
        else :
           print "--> 4BB."

def type2Algo(loc,randNum,randBB):
    if (loc<2):    # first 2/3 location
        if (randNum < 20):
           print "--> Raise, 3BB"
        else :
           print "--> Call"
    else:            # middle or late location
        if (randNum < 80):
           print "--> Raise, 3BB"
        else :
           print "--> Call"
            
def type3Algo(loc,randNum,randBB):
    if (loc==1):    # first 1/3 location
        if (randNum < 75):
           print "--> Raise, ???BB"
        else :
           print "--> Call"
    else:            # middle or late location
        if (randNum < 90):
           print "--> Raise, ????BB"
        else :
           print "--> Call"

def type4Algo(loc,randNum,randBB):
    type3Algo(loc,randNum,randBB);
   
def type5Algo(loc,randNum,randBB):
    if (loc<2):    # first 1/3 location
        if (randNum < 90):
           print "--> Call if in 4BB"
        else :
           print "--> Fold"
    else:            # late location
        if (randBB <50):
            if (randNum < 50):
               print "--> Raise, 3BB"
            else :
               print "--> Call"
        else:
            if (randNum < 90):
               print "--> Call if in 4BB"
            else :
               print "--> Fold"

def type6Algo(loc,randNum,randBB):
    if (randNum < 80):
        print "--> Call if in 4BB"
    else :
        print "--> Fold"
        
def type7Algo(loc,randNum,randBB):
    if (randNum < 60):
        print "--> Call if in 3BB"
    else :
        print "--> Fold"
        
def type8Algo(loc,randNum,randBB):
    if (randNum < 40):
        print "--> Call if in 3BB"
    else :
        print "--> Fold"

def type9Algo(loc,randNum,randBB):
    if (randNum < 30):
        print "--> Call if in 3BB"
    else :
        print "--> Fold"

def type10Algo(loc,randNum,randBB):
    if (randNum < 20):
        print "--> Call if in 3BB"
    else :
        print "--> Fold"
        
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
            #print " CBR, you card win  rate is  %r percent." % strList[1]
            #print " CBR, you card drew rate is  %r percent." % strList[2]
            return line.strip()
        
def preFlop(line,loc=1): # can add location, money information later
    randNum = random.randint(0,99)
    randBB  = random.randint(0,99)
    print "CBR AI suggest:"
    strList = line.split(' ')
    cardType = strList[-1]
    #print "cardType: %r" % cardType[0:-1]
    if cardType in type0:
        type0Algo(randBB)
    elif cardType in type1:
        type1Algo(loc,randNum,randBB)
    elif  cardType in type2:
        type2Algo(loc,randNum,randBB)
    elif  cardType in type3:
        type3Algo(loc,randNum,randBB)
    elif  cardType in type4:
        type4Algo(loc,randNum,randBB)
    elif  cardType in type5:
        type5Algo(loc,randNum,randBB)
    elif  cardType in type6:
        type6Algo(loc,randNum,randBB)
    elif  cardType in type7:
        type7Algo(loc,randNum,randBB)
    elif  cardType in type8:
        type8Algo(loc,randNum,randBB)
    elif  cardType in type9:
        type9Algo(loc,randNum,randBB)
    elif  cardType in type10:
        type10Algo(loc,randNum,randBB)
    else:
        print "--> Fold"

    return 0
