class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.face_up = False
        if self.suit == 'd' or self.suit == 'D' or self.suit == 'h' or self.suit == 'H':
            self.color = "red"
        if self.suit == 'c' or self.suit == 'C' or self.suit == 's' or self.suit == 'S':
            self.color = "black"

    def getRank(self):
        return int(self.rank)

    def getSuit(self):
        return self.suit

    def setFace_Up(self):
        self.face_up = True

    def setFace_Down(self):
        self.face_up = False

    def getFace(self):
        return self.face_up

    def getColor(self):
        return self.color

    def getLetter(self):
        if self.suit == 'd' or self.suit == 'D':
            return "Diamonds"
        if self.suit == 'c' or self.suit == 'C':
            return "Clovers"
        if self.suit == 'h' or self.suit == 'H':
            return "Hearts"
        if self.suit == 's' or self.suit == 'S':
            return "Spades"

    #  def value(self):
    #      if 1 <= self.rank <= 10:
    #          return rank
    #      else:
    #          return 10

    def __str__(self):
        if self.getRank() == 1 and self.face_up:
            return "A" + self.getSuit()
            # return '{} {}'.format("Ace of", self.getLetter())
        elif 1 < self.getRank() <= 10 and self.face_up:
            return str(self.getRank()) + self.getSuit()
            # return '{} {} {}'.format(self.getRank(), "of", self.getLetter())
        elif self.getRank() == 11 and self.face_up:
            return "J" + self.getSuit()
            # return '{} {}'.format("Jack of", self.getLetter())
        elif self.getRank() == 12 and self.face_up:
            return "Q" + self.getSuit()
            # return '{} {}'.format("Queen of", self.getLetter())
        elif self.getRank() == 13 and self.face_up:
            return "K" + self.getSuit()
            # return '{} {}'.format("King of", self.getLetter())
        else:
            return "[--]"


def getPicture(card):  # return string of picture

    if card.getRank() == 1:
        png_name = "A" + card.getSuit() + ".png"
        png_name.replace(" ", "")
        return png_name
    elif 1 < card.getRank() <= 10:
        png_name = str(card.getRank()) + card.getSuit() + ".png"
        png_name.replace(" ", "")
        return png_name
    elif card.getRank() == 11:
        png_name = "J" + card.getSuit() + ".png"
        png_name.replace(" ", "")
        return png_name
    elif card.getRank() == 12:
        png_name = "Q" + card.getSuit() + ".png"
        png_name.replace(" ", "")
        return png_name
    elif card.getRank() == 13:
        png_name = "K" + card.getSuit() + ".png"
        png_name.replace(" ", "")
        return png_nam
    
   # testing testing pull requests
