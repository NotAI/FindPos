# Nature definition
# 0 - 10: 5 is default and standard, 0 is most tight, 10 is most loose
# Strong definition
# 0 - 10: 5 is default and standard, 0 is most likely to fold, 10 is most likely to reraise
from people import *

class opeople(people):

    # card0 and card1 is expected to be int number between [0,53]
    def __init__(self,location, nature=5, strong=5, c0=0, c1=0):
        people(self, c0, c1,location)
        self.nature = nature;
        self.strong = strong;

    def updateTable(self, board,bet):
        self.board = board;
        self.bet = bet;

    def updateCard(self, c0=0, c1=0):
        pass
