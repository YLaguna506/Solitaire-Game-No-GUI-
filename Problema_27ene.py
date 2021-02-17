import random
from graphics import *

class Card:

    def __init__(self, rank, suit, window, face_shape, face_display):
        self.rank = rank
        self.suit = suit
        self.win = window
        self.face_shape = face_shape
        self.face_display = face_display

        self.face_shape.draw(self.win)
        self.face_shape.undraw()

    def drawFace(self, face_display):
        self.face_display.draw(self.win)

    def getRank(self):
        return int(self.rank)

    def getSuit(self):
        return self.suit

    def getLetter(self):
        if self.suit == 'd' or self.suit == 'D':
            return "Diamonds"
        if self.suit == 'c' or self.suit == 'C':
            return "Clovers"
        if self.suit == 'h' or self.suit == 'H':
            return "Hearts"
        if self.suit == 's' or self.suit == 'S':
            return "Spades"

    def value(self):
        if 1 <= self.rank <= 10:
            return rank
        else:
            return 10

    def __str__(self):
        if self.getRank() == 1:
            return '{} {}'.format("Ace of", self.getLetter())
        elif 1 < self.getRank() <= 10:
            return '{} {} {}'.format(self.getRank(), "of", self.getLetter())
        elif self.getRank() == 11:
            return '{} {}'.format("Jack of", self.getLetter())
        elif self.getRank() == 12:
            return '{} {}'.format("Queen of", self.getLetter())
        elif self.getRank() == 13:
            return '{} {}'.format("King of", self.getLetter())


def getPicture(card): #return string of picture

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
        return png_name



# --- Main ---

rank = 0
suit = ''
letters = ['D', 'C', 'H', 'S']
quantity = eval(input("How many cards will be generated?"))

#creating display face of card with right size
point1 = Point(350, 210)
point2 = Point(380, 240)

win = GraphWin("Card Display", 1000, 1000)

card = [Card(rank, suit, win, Rectangle(point1, point2), 0) for _ in range(quantity)]

for i in range(quantity):
    rank = random.randint(1, 13)
    suit = random.choice(letters)
    card[i].rank = rank
    card[i].suit = suit

print("All cards created randomly: ")
for i in range(quantity):
    print("Card #", i+1, ":", card[i])

selection = eval(input("Which card would you like to display on window?")) # validar 1 to range(quantity)

cardSelected = card[selection-1]

cardImage = Image(Point(550,500), getPicture(cardSelected))
card = Card(rank, suit, win, Rectangle(Point(450, 310), Point(480, 340)), cardImage)

print("Click screen to quit")
cardImage.draw(win)
win.getMouse()

