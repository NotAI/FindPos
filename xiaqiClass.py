import sys
import time
import os
from people import *
from table import *
from card import *
from outputString import *
import cbr2Card
import cbrMath
class xiaqiClass(object):

    def __init__(self):
        self.peopleNum = 0;
        self.board = 0;
        self.bet = 0;

    def creatTable(self):
        #print askForBoard
        #board = int(raw_input("board>"))

        #print askForBet
        #bet = int(raw_input("bet>"))

        print askForDeck3
        while True :
            try:
                threeCard = raw_input("First Card>")
                suit = int(threeCard[0])
                numb = int(threeCard[1:])
                d0 = card(suit,numb)

                threeCard = raw_input("Second Card>")
                suit= int(threeCard[0])
                numb= int(threeCard[1:])
                d1 = card(suit,numb)

                threeCard = raw_input("Third Card>")
                suit= int(threeCard[0])
                numb= int(threeCard[1:])
                d2 = card(suit,numb)
                break
            except:
                print "Unexpected error:", sys.exc_info()[0]
                print "please re-enter your hand"
                pass

        #tableIns = table(board,bet,d0,d1,d2)
        tableIns = table(0,0,d0,d1,d2)
        return tableIns

    def creatCBR(self): #print askForLocation; #try: #    location = int(raw_input("location>")) #except: #   print "Please only input integer." #   sys.exit(0) print askForHand
        while True :
            try:
                twoCard = raw_input("First Card>")
                suit = int(twoCard[0])
                numb = int(twoCard[1:])
                c0 = card(suit,numb)
                twoCard = raw_input("Second Card>")
                suit= int(twoCard[0])
                numb= int(twoCard[1:])
                c1 = card(suit,numb)
                break
            except:
                print "Unexpected error:", sys.exc_info()[0]
                print "please re-enter your hand"
                pass

        #cbr = people(c0,c1,location);
        cbr = people(c0,c1,1);
        return cbr

    def printPoss(self,posList,combList):
        print outputPos % (combList[9], posList[9], combList[8], posList[8], combList[7], posList[7],
                           combList[6], posList[6], combList[5], posList[5], combList[4], posList[4],
                           combList[3], posList[3], combList[2], posList[2], combList[1], posList[1], combList[0], posList[0],)

    def openTodayFile(self):
        script_dir = os.path.dirname(__file__)
        fileName = time.ctime().split(' ')
        fileStr = "data/"+fileName[4]+fileName[1]+fileName[2]+".txt"
        filePath = os.path.join(script_dir,fileStr)
        filePointer= open(filePath, "a")
        return filePointer
    
    def write_pirntFold(self,fp):
        tmpStr = "\tCBR FOLD.\r\n"
        fp.write(tmpStr)
        print "===================================="
        print "====CBR FOLD, start next game======="
        print "===================================="

    def start(self):
        fp = self.openTodayFile()

        while True :
            print askForPeople;
            try:
                self.peopleNum = int(raw_input("people number>"))
                if self.peopleNum>1 and self.peopleNum<=10 :
                    fp.write("peopleNum: %s\r\n" % self.peopleNum)
                    break
                else :
                    print "People number is not valid. Please re-enter"
                    continue
            except:
                print "Unexpected error:", sys.exc_info()[0]
                print "please re-enter the people number"
                pass
        gameCnt = 0
        while (True):
            fp.closed
            # write this game data to today's file
            fp = self.openTodayFile()
            gameCnt += 1
            cbr = self.creatCBR()
            tmpStr = "\tGAME %s: CBR has card %s %s, %s %s.\r\n" % (gameCnt,cbr.c0.suit,cbr.c0.numb,cbr.c1.suit,cbr.c1.numb)
            fp.write(tmpStr)

            # Read in files to print current hand power
            line = cbr2Card.printPos(self.peopleNum,cbr.c0,cbr.c1)
            print "--------------------------------------------------------------------------"
            cbr2Card.preFlop(line)

            fold = raw_input("f ?>")
            if fold == "f" or fold == "F":
                self.write_pirntFold(fp)
                continue

            # Read in 3 desk card
            table = self.creatTable()  # leave for future algorithm
            tmpStr = "\t         Table has card %s %s, %s %s, %s %s.\r\n" % (table.d0.suit,table.d0.numb,table.d1.suit,table.d1.numb,table.d2.suit,table.d2.numb)
            fp.write(tmpStr)
            
            # Calculate 5 card possiblity and output

            posForFiveCard,combForFiveCard = cbrMath.findpos(cbr.c0, cbr.c1, table.d0, table.d1, table.d2)
            self.printPoss(posForFiveCard,combForFiveCard)

            # F or get 6th card number
            while True :
                try:
                    d3Str = raw_input("f or 4th card in table>")
                    if d3Str == "f" or d3Str == "F":
                        fold = "f"
                        break
                    else :
                        suit = int(d3Str[0])
                        numb = int(d3Str[1:])
                        d3 = card(suit,numb)
                        tmpStr = "\t         Table 4th card %s %s\r\n" % (d3.suit, d3.numb)
                        fp.write(tmpStr)
                        break
                except:
                    print "Unexpected error:", sys.exc_info()[0]
                    print "please re-enter the 4th card"
                    pass
            if fold == "f" :
                self.write_pirntFold(fp)
                continue
            else :
                table.updateCard(d3)

            posForSixCard,combForSixCard = cbrMath.findpos(cbr.c0, cbr.c1, table.d0, table.d1, table.d2, table.d3)
            self.printPoss(posForSixCard,combForSixCard)
            
            # F or get 7th card number
            while True :
                try:
                    d4Str = raw_input("f or 5th card in table>")
                    if d4Str == "f" or d4Str == "F":
                        fold = "f"
                        break
                    else :
                        suit = int(d4Str[0])
                        numb = int(d4Str[1:])
                        d4 = card(suit,numb)
                        tmpStr = "\t         Table 5th card %s %s\r\n" % (d4.suit, d4.numb)
                        fp.write(tmpStr)
                        break
                except:
                    print "Unexpected error:", sys.exc_info()[0]
                    print "please re-enter the 5th card"
                    pass
            if fold == "f" :
                self.write_pirntFold(fp)
                continue
            else :
                table.updateCard(d3,d4)
                
            cbrMath.findpos(cbr.c0, cbr.c1, table.d0, table.d1, table.d2, table.d3, table.d4)

            print "-------------------BELOW IS THE CHANCE FOR 5 CARD IN TABLE------------------------------"
            posForSevCard,combForSevCard = cbrMath.findpos(table.d0, table.d1, table.d2, table.d3, table.d4)
            self.printPoss(posForSevCard,combForSevCard)
            print "----------------------------------------------------------------------------------------"
            print "----------------------------------------------------------------------------------------"
            print "---------------------------START NEXT ROUNG GAME NOW------------------------------------"
            print "----------------------------------------------------------------------------------------"
            print "----------------------------------------------------------------------------------------"
