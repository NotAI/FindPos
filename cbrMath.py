# card win priority
# 10: Royal straight flush
# 9: straight flush
# 8: four of a kind
# 7: full house
# 6: flush
# 5: straight
# 4: three of a kind
# 3: two pair
# 2: one pair
# 1: high card

import numpy
from card import *

def find10(sevenCard):
    rsfList = numpy.zeros((4,5))
    #print rsfList # for debug only
    for i in range(0,7):
        suit = sevenCard[i].suit
        numb = sevenCard[i].numb
        if numb == 1:
            rsfList[suit][4] = 1
        elif numb == 0:
            rsfList[suit][3] = 1
        elif numb >= 10:
            rsfList[suit][numb-10] = 1
    # end i loop
    
    #print rsfList # for debug only

    has10 = all(rsfList[0]) or all(rsfList[1]) or all(rsfList[2]) or all(rsfList[3])
    return has10;

def find9(sevenCard):
    realNumList = [0] * 7
    for i in range(0,7):
        realNumList[i] = sevenCard[i].suit*13 + sevenCard[i].numb
    for i in range(0,7):
        # find if it has x+1 to x+4
        if sevenCard[i].numb > 10:
            continue
        elif sevenCard[i].numb == 10 and realNumList[i]-9 not in realNumList:
            continue
        elif realNumList[i]+1 not in realNumList:
            continue
        elif realNumList[i]+2 not in realNumList:
            continue
        elif realNumList[i]+3 not in realNumList:
            continue
        elif sevenCard[i].numb != 10 and realNumList[i]+4 not in realNumList:
            continue
        else:
            return 1
    return 0;
    
def find8(numbList):
    result = (4 in numbList)
    return result;
    
def find7(numbList):
    result = (3 in numbList) and (2 in numbList)
    return result;

def find6(sevenCard):
    suitList = [0] * 4
    for i in range(0,7):
        suitList[sevenCard[i].suit] += 1
        
    result = (suitList[0] > 4) or (suitList[1] > 4) or (suitList[2] > 4) or (suitList[3] > 4)
    return result
    
def find5(sevenCard,numbList):
    for i in range(0,7):
        # find if it has num+1 to num+4
        if sevenCard[i].numb > 10:
            continue
        elif sevenCard[i].numb == 10 and (numbList[1] == 0):
            continue
        elif (numbList[sevenCard[i].numb + 1] == 0):
            continue
        elif (numbList[sevenCard[i].numb + 2] == 0):
            continue
        elif (numbList[sevenCard[i].numb + 3] == 0):
            continue
        elif sevenCard[i].numb != 10 and (numbList[sevenCard[i].numb + 4] == 0):
            continue
        else:
            return 1
    return 0;

def find4(numbList):
    result = (3 in numbList)
    return result;

def find3(numbList):
    result = (numbList.count(2) > 1)
    return result;

def find2(numbList):
    result = (numbList.count(2) == 1)
    return result;

def creatCard(realNum):
    if realNum%13 == 0:
        numb = 13
    else :
        numb = realNum%13
    c0 = card((realNum-1)/13,numb)
    return c0 

def findpos(c0,c1,d0,d1,d2,d3=0,d4=0):
    nList = [0] * 11
    pList = [0] * 11

    # n1 = 0; n1 is useless, because use p1=1 - others possibility 
    # the main thoughts is to find each case, is there a 10 to 2
    if (d3==0):
        for i3 in range(1,53):
            d3 = creatCard(i3)
            
            invalidd3 = (d3.suit==c0.suit and d3.numb==c0.numb) or (d3.suit==c1.suit and d3.numb==c1.numb) or\
                        (d3.suit==d0.suit and d3.numb==d0.numb) or (d3.suit==d1.suit and d3.numb==d1.numb) or\
                        (d3.suit==d2.suit and d3.numb==d2.numb)
            if invalidd3 :
                continue;

            for i4 in range(i3+1,53):
                d4 = creatCard(i4)
                invalidd4 = (d4.suit==c0.suit and d3.numb==c0.numb) or (d4.suit==c1.suit and d4.numb==c1.numb) or\
                            (d4.suit==d0.suit and d3.numb==d0.numb) or (d4.suit==d1.suit and d4.numb==d1.numb) or\
                            (d4.suit==d2.suit and d3.numb==d2.numb) or (d4.suit==d1.suit and d4.numb==d3.numb)
                if invalidd4 :
                    continue;

                sevenCard = [c0,c1,d0,d1,d2,d3,d4]

                # find number repeat times
                numbList = [0] * 14
                for i in range(0,7):
                    numbList[sevenCard[i].numb] += 1

                if find10(sevenCard):
                    nList[10] += 1
                elif find9(sevenCard):
                    nList[9] += 1
                elif find8(numbList):
                    nList[8] += 1
                elif find7(numbList):
                    nList[7] += 1
                elif find6(sevenCard):
                    nList[6] += 1
                elif find5(sevenCard,numbList):
                    nList[5] += 1
                elif find4(numbList):
                    nList[4] += 1
                elif find3(numbList):
                    nList[3] += 1
                elif find2(numbList):
                    nList[2] += 1
                else:
                    nList[1] += 1 
            # end d4 loop 
        # end d3 loop
        wholeCase = 47*46/2 + 0.0;
    elif (d4==0):
        for i4 in range(1,53):
            d4 = creatCard(i4)
            invalidd4 = (d4.suit==c0.suit and d3.numb==c0.numb) or (d4.suit==c1.suit and d4.numb==c1.numb) or\
                        (d4.suit==d0.suit and d3.numb==d0.numb) or (d4.suit==d1.suit and d4.numb==d1.numb) or\
                        (d4.suit==d2.suit and d3.numb==d2.numb) or (d4.suit==d1.suit and d4.numb==d3.numb)
            if invalidd4 :
                continue;

            sevenCard = [c0,c1,d0,d1,d2,d3,d4]

            # find number repeat times
            numbList = [0] * 14
            for i in range(0,7):
                numbList[sevenCard[i].numb] += 1

            if find10(sevenCard):
                nList[10] += 1
            elif find9(sevenCard):
                nList[9] += 1
            elif find8(numbList):
                nList[8] += 1
            elif find7(numbList):
                nList[7] += 1
            elif find6(sevenCard):
                nList[6] += 1
            elif find5(sevenCard,numbList):
                nList[5] += 1
            elif find4(numbList):
                nList[4] += 1
            elif find3(numbList):
                nList[3] += 1
            elif find2(numbList):
                nList[2] += 1
            else:
                nList[1] += 1 
        # end d4 loop 
        wholeCase = 46.0;
    else :
        sevenCard = [c0,c1,d0,d1,d2,d3,d4]
        # find number repeat times
        numbList = [0] * 14
        for i in range(0,7):
            numbList[sevenCard[i].numb] += 1

        if find10(sevenCard):
            print "CBR has Royal straight flush"
            return 0
        elif find9(sevenCard):
            print "CBR has straight flush"
            return 0
        elif find8(numbList):
            print "CBR has four of a kind"
            return 0
        elif find7(numbList):
            print "CBR has full house"
            return 0
        elif find6(sevenCard):
            print "CBR has flush"
            return 0
        elif find5(sevenCard,numbList):
            print "CBR has straight"
            return 0
        elif find4(numbList):
            print "CBR has a set"
            return 0
        elif find3(numbList):
            print "CBR has two pair"
            return 0
        elif find2(numbList):
            print "CBR has a pair"
            return 0
        else:
            print "CBR has only high Card"
            return 0

    for i in range(1,11):
        pList[i] = 100*nList[i]/wholeCase
    
    #------for debug ------
    #print nList[1:]
    #print pList[1:]
    #------for debug ------

    return pList[1:],nList[1:]

def findpos_1(c0,c1,d0,d1,d2):
    outsList = [0] * 9
    pList = [0] * 10
   
    # the main thoughts is to find the outs for 10 to 2
    nList[10] = find_out10(c0,c1,d0,d1,d2,d3,d4);
    nList[9]  = find_out9(c0,c1,d0,d1,d2,d3,d4);
    nList[8]  = find_out8(c0,c1,d0,d1,d2,d3,d4);
    nList[7]  = find_out7(c0,c1,d0,d1,d2,d3,d4);
    nList[6]  = find_out6(c0,c1,d0,d1,d2,d3,d4);
    nList[5]  = find_out5(c0,c1,d0,d1,d2,d3,d4);
    nList[4]  = find_out4(c0,c1,d0,d1,d2,d3,d4);
    nList[3]  = find_out3(c0,c1,d0,d1,d2,d3,d4);
    nList[2]  = find_out2(c0,c1,d0,d1,d2,d3,d4);
    
    wholeCase = 47*46 + 0.0;

    for i in range(2,11):
        pList[i] = nList[i]/wholeCase
    pList[1]  = 1 - pList[10] - pList[9] - pList[8] - pList[7] - pList[6] - pList[5] - pList[4] - pList[3] - pList[2]

    return pList

def checkStrength(c0,c1): # Check Table and Output strength
    return 0;

