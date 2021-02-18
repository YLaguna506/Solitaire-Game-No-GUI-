
from card import Card

class Foundation:

    def __init__(self):
        self.Cards = []
        self.card_counter = 1
        self.Cards.append(Card(1, 'H')) #dummy card, later replaced
        self.hasAcard = False

    def addCard_ontop(self, card):
        self.Cards.append(card)
        self.card_counter += 1

    def give_topcardF(self):
        temp = self.Cards[(len(self.Cards) - 1)]
        self.Cards.pop()
        return temp

    def plusCardCounter(self):
        self.card_counter += 1

    def minusCardCounter(self):
        self.card_counter -= 1

    def hasA(self):
        return self.hasAcard

    def setA(self):
        self.hasAcard = True

    def getCardCounterF(self):
        return self.card_counter

    def getCardF(self, index):
        return self.Cards[index]

    def getTopCardF(self):
        return self.Cards[self.card_counter - 1]

    def setCardF(self, card, index):
        self.Cards[index] = card

    def setTopCardF(self, card):
        self.Cards.append(card)

    def isFull(self):
        if self.card_counter == 13:
            return True
        else:
            return False






