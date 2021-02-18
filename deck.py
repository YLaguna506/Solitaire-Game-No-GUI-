import random
from card import Card
from Stack import Stack
from Foundation import Foundation


class Deck:

    def __init__(self):
        self.Cards = []
        for i in range(52):
            if 0 <= i <= 12:
                self.Cards.append(Card(i + 1, 'H'))
            if 13 <= i <= 25:
                self.Cards.append(Card(i - 12, 'D'))
            if 26 <= i <= 38:
                self.Cards.append(Card(i - 25, 'C'))
            if 39 <= i <= 51:
                self.Cards.append(Card(i - 38, 'S'))

    def shuffle(self):
        for i in range(1000):
            pos_1 = random.randint(0, 51)
            pos_2 = random.randint(0, 51)
            while pos_2 == pos_1:
                pos_1 = random.randint(0, 51)
                pos_2 = random.randint(0, 51)
            self.Cards[pos_1], self.Cards[pos_2] = self.Cards[pos_2], self.Cards[pos_1]

    def getDeckcard(self, index):
        return self.Cards[index]

    def shuffleWastecard(self):
        if len(self.Cards) == 1:
            print("Only one or none cards left in Deck.")
        else:
            temp = self.Cards[len(self.Cards) - 1]
            temp.setFace_Down()
            y = len(self.Cards)

            while y > 0:
                y -= 1
                if y == 0:
                    self.Cards[0] = temp
                else:
                    self.Cards[y] = self.Cards[y - 1]

    def printDeck(self):
        for i in range(52):
            print(self.Cards[i])

    # different from one on stack
    def give_topcard(self):
        temp = self.Cards[(len(self.Cards) - 1)]
        self.Cards.pop()
        return temp

    def display_topcard(self):
        self.Cards[(len(self.Cards) - 1)].setFace_Up()
        return self.Cards[(len(self.Cards) - 1)]

