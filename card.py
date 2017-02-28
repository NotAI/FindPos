class card(object):

    # card0 and card1 is expected to be int number between [0,53]
    def __init__(self, suit, numb):
        self.suit = suit    # 0 means unknown
        self.numb = numb

    def updateCard(self,  suit, numb):
        self.suit = suit    # 0 means unknown
        self.numb = numb
        
    def pi(self):    # print all information 
        print "suit is %r" % self.suit
        print "numb is %r" % self.numb
