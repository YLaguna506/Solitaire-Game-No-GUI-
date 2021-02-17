
from card import Card

class Foundation:

    def __init__(self):
        self.Cards = []
        self.card_counter = 0

    def addCard_ontop(self, card):
        self.Cards.append(card)
        self.card_counter += 1

    def give_topcardF(self):
        temp = self.Cards[(len(self.Cards) - 1)]
        self.Cards.pop()
        return temp

    def getCardCounterF(self):
        return self.card_counter

    def getCardF(self, index):
        return self.Cards[index]

    def setCardF(self, card, index):
        self.Cards[index] = card

    def isFull(self):
        if self.card_counter == 13:
            return True
        else:
            return False






