import sys
from people import *
from table import *
from card import *
from outputString import *
import cbrMath
import cbr2Card
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
        try:
            threeCard = raw_input("First Card>")
            suit = int(threeCard.split(' ')[0])
            numb = int(threeCard.split(' ')[1])
            d0 = card(suit, numb)
            threeCard = raw_input("Second Card>")
            suit = int(threeCard.split(' ')[0])
            numb = int(threeCard.split(' ')[1])
            d1 = card(suit, numb)
            threeCard = raw_input("Third Card>")
            suit = int(threeCard.split(' ')[0])
            numb = int(threeCard.split(' ')[1])
            d2 = card(suit, numb)
        except ValueError:
            print "Could not convert data to an integer."
        except:
            print "Unexpected error:", sys.exc_info()[0]
            sys.exit(0)

        #tableIns = table(board,bet,d0,d1,d2)
        tableIns = table(0,0,d0,d1,d2)
        return tableIns

    def creatCBR(self):
        #print askForLocation;
        #try:
        #    location = int(raw_input("location>"))
        #except:
        #   print "Please only input integer."
        #   sys.exit(0)

        print askForHand
        try:
            twoCard = raw_input("First Card>")
            suit = int(twoCard.split(' ')[0])
            numb = int(twoCard.split(' ')[1])
            c0 = card(suit,numb)
            twoCard = raw_input("Second Card>")
            suit= int(twoCard.split(' ')[0])
            numb= int(twoCard.split(' ')[1])
            c1 = card(suit,numb)
        except ValueError:
            print "Could not convert data to an integer."
        except:
            print "Unexpected error:", sys.exc_info()[0]
            sys.exit(0)

        #cbr = people(c0,c1,location);
        cbr = people(c0,c1,1);
        return cbr

    def printPoss(self,posList,combList):
        print outputPos % (combList[9], posList[9], combList[8], posList[8], combList[7], posList[7],
                           combList[6], posList[6], combList[5], posList[5], combList[4], posList[4],
                           combList[3], posList[3], combList[2], posList[2], combList[1], posList[1], combList[0], posList[0],)


    def start(self):
        print askForPeople;
        try:
            self.peopleNum = int(raw_input("people number>"))
        except:
            print "Please only input integer."
            sys.exit(0)
        
        while (True):
            cbr = self.creatCBR()

            # Read in files to print current hand power
            cbr2Card.printPos(self.peopleNum,cbr.c0,cbr.c1)

            fold = raw_input("f ?>")
            if fold == "f" or fold == "F":
                continue

            # Read in 3 desk card
            table = self.creatTable()  # leave for future algorithm
            
            # Calculate 5 card possiblity and output

            posForFiveCard,combForFiveCard = cbrMath.findpos(cbr.c0, cbr.c1, table.d0, table.d1, table.d2)
            self.printPoss(posForFiveCard,combForFiveCard)

            # F or get 6th card number
            d3Str = raw_input("f or 4th card in table>")
            if d3Str == "f" or d3Str == "F":
                continue
            else:
                suit = int(d3Str.split(' ')[0])
                numb = int(d3Str.split(' ')[1])
                d3 = card(suit,numb)
                table.updateCard(d3)

            posForSixCard,combForSixCard = cbrMath.findpos(cbr.c0, cbr.c1, table.d0, table.d1, table.d2, table.d3)
            self.printPoss(posForSixCard,combForSixCard)
            
            # F or get 7th card number
            d4Str = raw_input("f or 5th card in table>")
            if d4Str == "f" or d4Str == "F":
                    continue
            else:
                suit = int(d4Str.split(' ')[0])
                numb = int(d4Str.split(' ')[1])
                d4 = card(suit,numb)
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
