import random
from card import Card
from Stack import Stack
from Foundation import Foundation
from deck import Deck


def setFace_Up_2(card):
    card.setFace_Up()


def getTopcard_pos(stack):
    for i in range(stack.getCardCounter() + 1):
        if i > stack.getCardCounter():
            break

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


def wasteSuitPos(card):
    if card.getSuit() == 'h' or card.getSuit() == 'H':
        return 0
    if card.getSuit() == 's' or card.getSuit() == 'S':
        return 1
    if card.getSuit() == 'd' or card.getSuit() == 'D':
        return 2
    if card.getSuit() == 'c' or card.getSuit() == 'C':
        return 3


def moveWastetoStack(card1, card2, stack1):

    global score

    if card2 == "":

        if len(deck.Cards) == 1:
            print("se vacio el deck")
            stack1.setCard(deck.give_topcard(),0)
            stack1.setCardCounter_plus1()
            deck[0] = ""
        else:

            stack1.setCard(deck.give_topcard(), 0)
            setFace_Up_2(deck.getDeckcard(len(deck.Cards) - 1))
            stack1.setCardCounter_plus1()

        # Waste to Tableau +5 points
        print("Waste to Tableau +5 points")
        score += 5

    elif card1.getRank() == card2.getRank() - 1 and card1.getColor() != card2.getColor():

        if len(deck.Cards) == 1:
            print("se vacio el deck")
            stack1.setCard(deck.give_topcard(), getBotcard_pos(stack1) + 1)
            stack1.setCardCounter_plus1()
            deck[0] = ""
        else:

            stack1.setCard(deck.give_topcard(), getBotcard_pos(stack1) + 1)
            setFace_Up_2(deck.getDeckcard(len(deck.Cards) - 1))
            stack1.setCardCounter_plus1()

        # Waste to Tableau +5 points
        print("Waste to Tableau +5 points")
        score += 5

    else:
        print("NO SE PUEDE")


def moveWastetoFoundationVacio(card, Foundation):
    if card.getRank() == 1:
        card.setFace_Up()
        Foundation.setCardF(card, 0)
        deck.give_topcard()
        Foundation.setA()

    else:
        print("NO SE PUEDE")


def moveWastetoFoundation(card1, card2, Foundation):
    if card1.getRank() == card2.getRank() + 1:

        card1.setFace_Up()
        Foundation.setTopCardF(card1)
        deck.give_topcard()
        Foundation.plusCardCounter()

        # Waste to Foundation +10 points
        global score
        score += 10
        print("Waste to Foundation +10 points")

    else:
        print("NO SE PUEDE")


def moveStacktoFoundationVacio(card, stack, foundation):
    global score
    if card.getRank() == 1:
        foundation.setCardF(card, 0)

        if getBotcard_pos(stack) == getTopcard_pos(stack) and stack.getCardCounter() != 1:
            setFace_Up_2(stack.getCard(getTopcard_pos(stack) - 1))
            # Turn over Tableau Card +5 points
            score += 5
            print("Turn over Tableau Card")

        stack.setCardCounter_min1()
        foundation.setA()
        if stack.getCardCounter() == 0:
            stack.setCard("", 0)
        else:
            stack.setCard("", getTopcard_pos(stack) + 1)

    else:
        print("NO SE PUEDE, NOT A")


def moveStacktoFoundation(card1, card2, stack, foundation):
    global score
    if card1.getRank() == card2.getRank() + 1:

        foundation.setTopCardF(card1)
        if getBotcard_pos(stack) == getTopcard_pos(stack) and stack.getCardCounter() != 1:
            setFace_Up_2(stack.getCard(getTopcard_pos(stack) - 1))
            # Turn over Tableau Card +5 points
            score += 5
            print("Turn over Tableau Card")

        stack.setCardCounter_min1()
        foundation.plusCardCounter()
        if stack.getCardCounter() == 0:
            stack.setCard("", getTopcard_pos(stack))
        else:
            stack.setCard("", getTopcard_pos(stack) + 1)

        # Tableau to Foundation +10 points
        score += 10
        print("Tableau to Foundation +10 points")


    else:
        print("NO SE PUEDE, NUMERO NO COINCIDE")


def moveFoundationtoStack(card1, card2, foundation, stack):
    if card1.getRank() == card2.getRank() - 1 and card1.getColor() != card2.getColor():

        if foundation.getCardCounterF() == 1:
            print("se vacio un Foundation")
            stack.setCard(foundation.getTopCardF(), getBotcard_pos(stack) + 1)
            stack.setCardCounter_plus1()
            foundation.setCardF(Card(1, 'H'), 0)  # dummy card
        else:

            stack.setCard(foundation.give_topcardF(), getBotcard_pos(stack) + 1)
            foundation.minusCardCounter()
            stack.setCardCounter_plus1()

        # Foundation to Tableau -15 points
        global score
        score -= 15
        print("Foundation to Tableau -15 points")

    else:
        print("NO SE PUEDE, NO COINCIDE NUMERO")


def move_instacks(card1, card2, stack1, stack2):

    global score
    if card2 == "":

        if getTopcard_pos(stack1) + 1 == stack1.getCardCounter():

            if stack1.getCardCounter() == 1:
                print("se vacio un stack")
                stack2.setCard(stack1.getCard(getTopcard_pos(stack1)), 0)
                stack1.setCardCounter_min1()
                stack2.setCardCounter_plus1()
                stack1.setCard("", getTopcard_pos(stack1))
            else:

                stack2.setCard(stack1.getCard(getTopcard_pos(stack1)), 0)
                setFace_Up_2(stack1.getCard(getTopcard_pos(stack1) - 1))

                # Turn over Tableau Card +5 points
                score += 5
                print("Turn over Tableau Card")

                stack1.setCardCounter_min1()
                stack2.setCardCounter_plus1()
                stack1.setCard("", getTopcard_pos(stack1) + 1)
        else:
            print("Not done yet")

    elif card1.getRank() == card2.getRank() - 1 and card1.getColor() != card2.getColor():

        if getTopcard_pos(stack1) + 1 == stack1.getCardCounter():

            if stack1.getCardCounter() == 1:
                print("se vacio un stack")
                stack2.setCard(stack1.getCard(getTopcard_pos(stack1)), getBotcard_pos(stack2) + 1)
                stack1.setCardCounter_min1()
                stack2.setCardCounter_plus1()
                stack1.setCard("", getTopcard_pos(stack1))
            else:

                stack2.setCard(stack1.getCard(getTopcard_pos(stack1)), getBotcard_pos(stack2) + 1)
                setFace_Up_2(stack1.getCard(getTopcard_pos(stack1) - 1))

                # Turn over Tableau Card +5 points
                score += 5
                print("Turn over Tableau Card")

                stack1.setCardCounter_min1()
                stack2.setCardCounter_plus1()
                stack1.setCard("", getTopcard_pos(stack1) + 1)
        else:

            temp_list = []
            n = 0
            var = stack1.getCard(n)
            while var != "":
                if var.getFace():
                    temp_list.append(var)
                n += 1
                var = stack1.getCard(n)

            for i in range(len(temp_list)):

                stack2.setCard(temp_list[i], getBotcard_pos(stack2) + 1)
                if i == 0 and stack1.getCardCounter() != 1:
                    setFace_Up_2(stack1.getCard(getTopcard_pos(stack1) - 1))
                    # Turn over Tableau Card +5 points
                    score += 5
                    print("Turn over Tableau Card")

                stack2.setCardCounter_plus1()
                stack1.setCardCounter_min1()
                stack1.setCard("", getTopcard_pos(stack1) + 1 + i)

    else:
        print("NO SE PUEDE")


def getMax_Lines():
    max = Stacks[0].getCardCounter()
    for i in range(len(Stacks)):
        if max < Stacks[i].getCardCounter():
            max = Stacks[i].getCardCounter()

    return max


def blankspacesforoutput(Stacks):
    # adds blank space to list for output of table
    for i in range(20 - len(Stacks[0].Cards)):
        Stacks[0].addCard("")
    for i in range(20 - len(Stacks[1].Cards)):
        Stacks[1].addCard("")
    for i in range(20 - len(Stacks[2].Cards)):
        Stacks[2].addCard("")
    for i in range(20 - len(Stacks[3].Cards)):
        Stacks[3].addCard("")
    for i in range(20 - len(Stacks[4].Cards)):
        Stacks[4].addCard("")
    for i in range(20 - len(Stacks[5].Cards)):
        Stacks[5].addCard("")
    for i in range(20 - len(Stacks[6].Cards)):
        Stacks[6].addCard("")


def startgame(deck, Stacks):
    totalstacks = 7
    counter = 0
    while len(deck.Cards) != 24:
        for i in range(totalstacks):
            if counter == 0:
                Stacks[0].addCard(deck.give_topcard())
                setFace_Up_2(Stacks[0].getCard(counter))
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
            totalstacks -= 1


# -- Main --


deck = Deck()
deck.shuffle()
score = 0

Stacks = [Stack() for _ in range(7)]
Foundations = [Foundation() for _ in range(4)]

# incluir foundation con carta vacia? tal vez para el GUI sea util
startgame(deck, Stacks)

blankspacesforoutput(Stacks)

game_over = False
counter_Recycles = 1
deckQ = len(deck.Cards)

while not game_over:

    if (Foundations[0].getCardCounterF() == 13 and Foundations[1].getCardCounterF() == 13
            and Foundations[2].getCardCounterF() == 13 and Foundations[3].getCardCounterF() == 13):
        game_over = True
        break

    # prints game board - deck row
    print("\n")
    print("%-10s %-20s %-10s %-10s %-10s %s" % (
        "Deck", "Waste", "Foundation 1", "Foundation 2", "Foundation 3", "Foundation 4"))
    print("%-10s %-20s %-12s %-12s %-12s %s" % (
        deck.Cards[0], deck.display_topcard(), Foundations[0].getTopCardF(), Foundations[1].getTopCardF(),
        Foundations[2].getTopCardF(), Foundations[3].getTopCardF()))

    # prints game board - stack row
    print("%-10s %-10s %-10s %-10s %-10s %-10s %s" % (
        "Stack 1", "Stack 2", "Stack 3", "Stack 4", "Stack 5", "Stack 6", "Stack 7"))
    max_lines = getMax_Lines()
    for i in range(max_lines):
        print("%-10s %-10s %-10s %-10s %-10s %-10s %s" % (
            Stacks[0].getCard(i), Stacks[1].getCard(i), Stacks[2].getCard(i), Stacks[3].getCard(i),
            Stacks[4].getCard(i), Stacks[5].getCard(i), Stacks[6].getCard(i)))

    print("Score: ", score)
    print("Enter 'Q G' to quit game")
    move1, move2 = input("Enter Next Move: (Ex: S1 S3, S4 F, W S5, W F, W C)").split()

    if(move1[0] == "q" or move1[0] == "Q") and (move2[0] == "g" or move2[0] == "G"):
        #falta validacion de entrada

        print("Game quited")
        break

    # shuffles waste card
    elif (move1[0] == "w" or move1[0] == "W") and (move2[0] == "C" or move2[0] == "c"):
        deck.shuffleWastecard()
        counter_Recycles += 1
        if counter_Recycles == deckQ:

            # Waste Recycled Completely -100 points
            score -= 100
            print("Waste Recycled Completely -100 points")

            deckQ = len(deck.Cards)
            counter_Recycles = 0
            if score < 0:
                score = 0

    # Moves card from Waste to Stack/Tableau
    elif (move1[0] == "w" or move1[0] == "W") and (move2[0] == "s" or move2[0] == "S"):
        while (not move2[1].isnumeric()) or (len(move2) > 2):
            move2 = input("Enter Move 2 correctly: ")

        if len(deck.Cards) == 0:
            print("Deck empty")

        else:
            s1 = int(move2[1])
            s1 -= 1
            x = deck.display_topcard()
            y = Stacks[s1].getCard(getBotcard_pos(Stacks[s1]))
            moveWastetoStack(x, y, Stacks[s1])

    # Moves card from Waste to Foundation
    elif (move1[0] == "w" or move1[0] == "W") and (move2[0] == "f" or move2[0] == "F"):

        if len(deck.Cards) == 0:
            print("Deck empty")

        else:

            x = deck.display_topcard()

            if Foundations[wasteSuitPos(x)].getCardCounterF() == 1 and not Foundations[wasteSuitPos(x)].hasA():
                moveWastetoFoundationVacio(x, Foundations[wasteSuitPos(x)])

                # Waste to Foundation +10 points
                score += 10
                print("Waste to Foundation +10 points")

            else:

                y = Foundations[wasteSuitPos(x)].getTopCardF()
                moveWastetoFoundation(x, y, Foundations[wasteSuitPos(x)])

    # Moves card from Stack/Tableau to another Stack/Tableau
    elif (move1[0] == "s" or move1[0] == "S") and (move2[0] == "s" or move2[0] == "S"):

        while (not move1[1].isnumeric()) or (len(move1) > 2):
            move1 = input("Enter Move 1 correctly: ")
        while (not move2[1].isnumeric()) or (len(move2) > 2):
            move2 = input("Enter Move 2 correctly: ")

        s1 = int(move1[1])
        s2 = int(move2[1])
        s1 -= 1
        s2 -= 1
        # print(s1)
        # print(s2)

        if Stacks[s1].getCardCounter() == 0:
            print("Empty Stack Selected")

        else:

            x = Stacks[s1].getCard(getTopcard_pos(Stacks[s1]))
            y = Stacks[s2].getCard(getBotcard_pos(Stacks[s2]))
            # print(type(y))
            move_instacks(x, y, Stacks[s1], Stacks[s2])

    # Moves card from Stack/Tableau to Foundation
    elif (move1[0] == "s" or move1[0] == "S") and (move2[0] == "f" or move2[0] == "F"):
        while (not move1[1].isnumeric()) or (len(move1) > 2):
            move1 = input("Enter Move 1 correctly: ")

        s1 = int(move1[1])
        s1 -= 1

        if Stacks[s1].getCard(0) == str:
            print("Empty Stack Selected")

        else:
            x = Stacks[s1].getCard(getBotcard_pos(Stacks[s1]))

            if Foundations[wasteSuitPos(x)].getCardCounterF() == 1 and not Foundations[wasteSuitPos(x)].hasA():
                moveStacktoFoundationVacio(x, Stacks[s1], Foundations[wasteSuitPos(x)])

                # Tableau to Foundation +10 points
                score += 10
                print("Tableau to Foundation +10 points")

            else:

                y = Foundations[wasteSuitPos(x)].getTopCardF()
                moveStacktoFoundation(x, y, Stacks[s1], Foundations[wasteSuitPos(x)])

    # Moves card from Foundation to Stack/Tableau
    elif (move1[0] == "f" or move1[0] == "F") and (move2[0] == "s" or move2[0] == "S"):

        while (not move1[1].isnumeric()) or (len(move1) > 2):
            move1 = input("Enter Move 1 correctly: ")
        while (not move2[1].isnumeric()) or (len(move2) > 2):
            move2 = input("Enter Move 2 correctly: ")

        s1 = int(move1[1])
        s2 = int(move2[1])
        s1 -= 1
        s2 -= 1

        if not Foundations[s1].hasA() or Stacks[s2].getCard(0) == "":
            print("Empty Stack or Foundation Selected")

        else:

            x = Foundations[s1].getTopCardF()
            y = Stacks[s2].getCard(getBotcard_pos(Stacks[s2]))
            moveFoundationtoStack(x, y, Foundations[s1], Stacks[s2])

    else:
        print("What are you doing?")

#Outside Game
if not game_over:
    print("You lost!")
    print("Score After Session: ", score)

else:
    print("You WON!")
    print("Score After Session: ", score)
