Final project for python class.

Solitaire Game Project 

It has deck class, stack class, card class, Foundation class and main program in Solitaireapp.

The deck class has a card class array of 52, it creates it entirely with the corresponding cards. When creating the object, the
shuffle function executes.  This function shuffles the deck so that they never have the same order.

Stack class was created to create stacks 1 - 7, or the Tableau.
The stacks contain an array of card class plus empty strings, this was done to use the print that was used.
This is why card counter is included in the stack class.

The main program is found in Solitaireapp.

The program still has input errors, if  exactly 2 values are not entered.
There are bugs if you move a column of cards between the tableau and an empty stack.

RULES FOR THE SCORE:
Waste to Tableau	5
Waste to Foundation	10
Tableau to Foundation	10
Turn over Tableau card	5
Foundation to Tableau	−15
Recycle waste when playing by ones	−100 
(minimum score is 0)

SELECTED WASTE RULE:
Turning one card at a time to the waste, with no limit on passes through the deck.

![soli1](https://user-images.githubusercontent.com/77646834/178113043-05e39615-c7d7-4785-a15b-fa3745fc9ea7.PNG)
