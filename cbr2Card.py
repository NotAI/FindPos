import sys
import os
import random

type0 = ["1009","1008","1007"]
type1 = ["0109","0108","0107","0148","0136","0146"]
type2 = ["0139","0039","0149","0049","0118","0018","0128","0028","0138","0038","0117","0017","0127","0027"]
type3 = ["0115","0114","0113","0112","0111"]
type4 = ["0124","0123","0122"]
type5 = ["0134","0133","0132"]
type6 = ["0015","0014","0013"]
type7 = ["2009","2008","2007"]        
type8 = ["2006","2005","2004"]        
type9 = ["3009","3008","3007","3006"]        
type10 = ["0119","0019"]
type11 = ["0129","0029"]        

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
        
def preFlop(line): # can add location, money information later
    randNum = random.randint(0,99)
    print "CBR AI suggest:"
    strList = line.split(' ')
    cardType = strList[-1]
    #print "cardType: %r" % cardType[0:-1]
    if cardType in type0:
        print "--> Raise no matter location, doc didn't say raise how much BB"
        print "--> if (other people raise again):"
        print "-->    AA,KK continue raise, QQ consider people strength, call or raise"
    elif cardType in type1:
        if (randNum < 90):
            print "--> If in early location: Call in 4BB"
            print "--> If in late location: Raise in 3BB"
        else :
            print "--> If in early location: Fold"
            print "--> If in late location: Raise in 3BB"
    elif  cardType in type2:
        if (randNum < 80):
            print "--> Call"
        else :
            print "--> Fold"
    elif  cardType in type3:
        if (randNum < 60):
            print "--> Call"
        else :
            print "--> Fold"
    elif  cardType in type4:
        if (randNum < 40):
            print "--> Call"
        else :
            print "--> Fold"
    elif  cardType in type5:
        if (randNum < 30):
            print "--> Call"
        else :
            print "--> Fold"
    elif  cardType in type6:
        if (randNum < 20):
            print "--> Call"
        else :
            print "--> Fold"
    elif  cardType in type7:
        print "-->If in early location:"
        if (randNum < 70):
            print "--> Raise"
        else :
            print "--> Call"
        print "-->If in mid/late location:"
        if (randNum < 80):
            print "--> Raise in 4/5 BB"
        else :
            print "--> Call"
    elif  cardType in type8:
        print "-->If in early location:"
        if (randNum < 30):
            print "--> Raise"
        else :
            print "--> Call"
        print "-->If in mid/late location:"
        if (randNum < 80):
            print "--> Raise in 4/5 BB"
        else :
            print "--> Call"
    elif  cardType in type9:
        print "-->If in early location:"
        print "--> WHAT THE FUCK IS MOST TIME CALL? SOMETIME RAISE? PROGRAM NEED NUMBER!!!"
    elif  cardType in type10:
        print "-->If in early location:"
        if (randNum < 75):
            print "--> Raise"
        else :
            print "--> Call"
        print "-->If in mid/late location:"
        if (randNum < 90):
            print "--> Raise"
        else :
            print "--> Call"
    elif  cardType in type10:
        print "-->If in early location:"
        if (randNum < 75):
            print "--> Raise"
        else :
            print "--> Call"
        print "-->If in mid/late location:"
        if (randNum < 90):
            print "--> Raise"
        else :
            print "--> Call"
        print "-->If someone raise again: Fold"
    else:
        print "--> Fold"

    return 0
