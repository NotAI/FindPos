class people(object):

    # card0 and card1 is expected to be int number between [0,53]
    def __init__(self,card0, card1, location=1):
        self.c0 = card0;    # 0 means unknown
        self.c1 = card1;
        self.location = location;

    def updateCard(self, card0,card1):
        self.c0 = card0;
        self.c1 = card1;

    def updateLocation(self, location):
        self.location = location;

    # 0 is blinds, 1 is small blinds, max-1 is dealer
    def locationInc(self, max_location):
        if self.location < max_location-1:
            self.location += 1;
        else:
            self.location = 0;
