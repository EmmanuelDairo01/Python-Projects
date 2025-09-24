print(r'''
*******************************************************************************
............    ........     ..........   ...........   ...                   . .            .........        .        .        ...........
 ...........    ........     .........    .             . .                 . .              .       .       .  .     . .       .
  ..........    .... ....    .........    .             . .                .  .              .       .      .    .   .   .      .
   .........    ...   ...    ........     ...........   . .                .  .              .       .     .      . .     .     ............
    ........   ...     ...   .......      .             . .                 .  .             .       .    .        .       .    .
     .......  ...       ...........       .             . .............       .  .           .       .   .                  .   .
      ...........         ........        ...........   ...............         .  .         .........  .                    .  ............
                          
                                    
                                    .
                             /^\     .
                        /\   "V"
                       /__\   I      .  .
                      //..\\  I     .
                      \].`[/  I
                      /l\/j\  (]    .  .
                     /. ~~ ,\/I          .
                     \\L__j^\/I       .
                      \/--v}  I     .   .
                      |    |  I   _________
                      |    |  I c(`       ')o
                      |    l  I   \.     ,/      -Row
                    _/j  L l\_!  _//^---^\\_
                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   
*******************************************************************************
''')
print("Welcome to the My Wizard Dungeon ")
print("Your mission is to escape")

choice1= input("Choice were to enter 'Type 'Left' or 'Right''").lower()

if choice1 == "left":
    print("You got swallowed by the dragon HAHAHAHAHAHAHA")
else:
    print("You may proceed")
    choice2 = input("Choice a pot of stew one is posinous the other is safe Type either '1' or '2'").lower()
    if choice2 == "1":
     print("You may proceed")
     choice3 = input("You are at the final crossroad know answer a question pizza or burger enter 1 for pizza and 2 for burger").lower()
     if choice3 == "1":
         print("You escaped but it won;t happen next time")
     else:
           print("Nah pizza wins ha ha ha ah ah ah ah ah ah")
    else:
     print("You got poisoned MUAH AH AHA HA AH AH AHA HA HA AH")
