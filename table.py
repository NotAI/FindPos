class table(object):

    # card0 and card1 is expected to be int number between [0,53]
    def __init__(self,board, bet, d0=0, d1=0, d2=0, d3=0, d4=0):
        self.board = board;
        self.bet = bet;
        self.d0 = d0
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.d4 = d4

    def updateTable(self, board,bet):
        self.board = board;
        self.bet = bet;

    def updateCard(self, d3=0, d4=0):
        self.d3 = d3
        self.d4 = d4
