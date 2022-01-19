# Python-Solitaire-Game-Project
Solitaire Game Project 

Por ahora tiene clase deck, clase stack, clase card, clasee Foundation y programa principal en Solitaireapp.

La clase deck tiene un array de clase card de 52, lo crea por completo con las cartas correspondientes al crear el objeto
se creo funcion shuffle para que nunca tengan el mismo orden.

Se creo clase stack para crear los stacks 1 - 7, o el Tableau 
Los stacks contienen un array de clase card mas strings vacios, esto se hizo para usar el print que se uso.
Por esto se incluyo counter de cartas en la clase de stack.

El programa principal se encuentra en Solitaireapp.

El programa todavia tiene errores en el input, si es que no se entran 2 valores. 
Hay errores si mueves columna de cartas entre el tableau, y esta vacia un stack.

REGLAS PARA EL SCORE:
Waste to Tableau	5
Waste to Foundation	10
Tableau to Foundation	10
Turn over Tableau card	5
Foundation to Tableau	−15
Recycle waste when playing by ones	−100 
(minimum score is 0)

REGLA DE EL WASTE ESCOGIDA:
Turning one card at a time to the waste, with no limit on passes through the deck.
