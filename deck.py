import random
from card import Card
from Stack import Stack


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
        for i in range(300):
            pos_1 = random.randint(0, 51)
            pos_2 = random.randint(0, 51)
            while pos_2 == pos_1:
                pos_1 = random.randint(0, 51)
                pos_2 = random.randint(0, 51)
            self.Cards[pos_1], self.Cards[pos_2] = self.Cards[pos_2], self.Cards[pos_1]

    def printDeck(self):
        for i in range(52):
            print(self.Cards[i])

    # different from one on stack
    def give_topcard(self):
        temp = self.Cards[(len(self.Cards) - 1)]
        self.Cards.pop()
        return temp

    def display_topcard(self):
        temp = self.Cards[(len(self.Cards) - 1)]
        temp.setFace_Up()
        return temp


def setFace_Up_2(card):
    card.setFace_Up()


def getTopcard_pos(stack):
    for i in range(stack.getCardCounter() + 1):
        if i > stack.getCardCounter():
            break
        # print(type(stack.Cards[i]))
        elif stack.Cards[i].getFace():
            indexx = i
            return indexx


def getBotcard_pos(stack):
    for x in range(stack.getCardCounter() + 1):
        if x > stack.getCardCounter():
            break
        elif stack.Cards[x] == "":
            index = x - 1
            return index


def move_instacks(card1, card2, stack1, stack2):
    # print(getTopcard_rank(stack1))
    #print(card1.getRank())
    #print(card2.getRank() - 1)
    if card1.getRank() == card2.getRank() - 1 and card1.getColor() != card2.getColor():
        # print("SE PUEDE")
        #print(getTopcard_pos(stack1))
        #print(stack1.getCardCounter())
        if getTopcard_pos(stack1) + 1 == stack1.getCardCounter():
            stack2.setCard(stack1.getCard(getTopcard_pos(stack1)), getBotcard_pos(stack2)+1)
            setFace_Up_2(stack1.getCard(getTopcard_pos(stack1)-1))
            stack1.setCardCounter_min1()
            stack1.setCard("", getTopcard_pos(stack1)+1)
        else:
            print("Not done yet")

    else:
        print("NO SE PUEDE")


# -- Main --


deck = Deck()
deck.shuffle()

Stacks = [Stack() for _ in range(7)]

x = 7
counter = 0
while len(deck.Cards) != 24:
    for i in range(x):
        if counter == 0:
            Stacks[0].addCard(deck.give_topcard())
            # print(Stacks[0].getCard(counter).getRank())
            setFace_Up_2(Stacks[0].getCard(counter))
            #print(type(Stacks[0].getCard(counter)))
            Stacks[1].addCard(deck.give_topcard())
            Stacks[2].addCard(deck.give_topcard())
            Stacks[3].addCard(deck.give_topcard())
            Stacks[4].addCard(deck.give_topcard())
            Stacks[5].addCard(deck.give_topcard())
            Stacks[6].addCard(deck.give_topcard())
        if counter == 1:
            Stacks[1].addCard(deck.give_topcard())
            setFace_Up_2(Stacks[1].getCard(counter))
            Stacks[2].addCard(deck.give_topcard())
            Stacks[3].addCard(deck.give_topcard())
            Stacks[4].addCard(deck.give_topcard())
            Stacks[5].addCard(deck.give_topcard())
            Stacks[6].addCard(deck.give_topcard())
        if counter == 2:
            Stacks[2].addCard(deck.give_topcard())
            setFace_Up_2(Stacks[2].getCard(counter))
            Stacks[3].addCard(deck.give_topcard())
            Stacks[4].addCard(deck.give_topcard())
            Stacks[5].addCard(deck.give_topcard())
            Stacks[6].addCard(deck.give_topcard())
        if counter == 3:
            Stacks[3].addCard(deck.give_topcard())
            setFace_Up_2(Stacks[3].getCard(counter))
            Stacks[4].addCard(deck.give_topcard())
            Stacks[5].addCard(deck.give_topcard())
            Stacks[6].addCard(deck.give_topcard())
        if counter == 4:
            Stacks[4].addCard(deck.give_topcard())
            setFace_Up_2(Stacks[4].getCard(counter))
            Stacks[5].addCard(deck.give_topcard())
            Stacks[6].addCard(deck.give_topcard())
        if counter == 5:
            Stacks[5].addCard(deck.give_topcard())
            setFace_Up_2(Stacks[5].getCard(counter))
            Stacks[6].addCard(deck.give_topcard())
        if counter == 6:
            Stacks[6].addCard(deck.give_topcard())
            setFace_Up_2(Stacks[6].getCard(counter))

        counter += 1
        x -= 1

# adds blank space to list for output of table
for i in range(8 - len(Stacks[0].Cards)):
    Stacks[0].addCard("")
for i in range(8 - len(Stacks[1].Cards)):
    Stacks[1].addCard("")
for i in range(8 - len(Stacks[2].Cards)):
    Stacks[2].addCard("")
for i in range(8 - len(Stacks[3].Cards)):
    Stacks[3].addCard("")
for i in range(8 - len(Stacks[4].Cards)):
    Stacks[4].addCard("")
for i in range(8 - len(Stacks[5].Cards)):
    Stacks[5].addCard("")
for i in range(8 - len(Stacks[6].Cards)):
    Stacks[6].addCard("")

game_over = False

while not game_over:

    print("%-10s %-20s %-10s %-10s %-10s %s" % (
        "Deck", "Waste", "Foundation 1", "Foundation 2", "Foundation 3", "Foundation 4"))
    print("%-10s %-20s %-12s %-12s %-12s %s" % (
        deck.Cards[0], deck.display_topcard(), deck.Cards[0], deck.Cards[0], deck.Cards[0], deck.Cards[0]))

    print("%-10s %-10s %-10s %-10s %-10s %-10s %s" % (
        "Stack 1", "Stack 2", "Stack 3", "Stack 4", "Stack 5", "Stack 6", "Stack 7"))

    for i in range(8):
        print("%-10s %-10s %-10s %-10s %-10s %-10s %s" % (
            Stacks[0].getCard(i), Stacks[1].getCard(i), Stacks[2].getCard(i), Stacks[3].getCard(i),
            Stacks[4].getCard(i), Stacks[5].getCard(i), Stacks[6].getCard(i)))

    move1, move2 = input("Enter Next Move: (Ex: S1 S3, S4 F2, W1 S5)").split()
    # 1 to 5

    s1 = int(move1[1])
    s2 = int(move2[1])
    s1 -= 1
    s2 -= 1
    # print(s1)
    # print(s2)

    x = Stacks[s1].getCard(getTopcard_pos(Stacks[s1]))
    y = Stacks[s2].getCard(getBotcard_pos(Stacks[s2]))
    #print(type(y))
    move_instacks(x, y, Stacks[s1], Stacks[s2])
