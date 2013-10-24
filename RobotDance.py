#HW4
#Carey Crook
#Section B01
#GTID: 902944489
#careymcrook@gmail.com
#I worked on the homework assignment alone, using only this semester's course materials.

from Myro import *
init ()


def danceSing():
    forward(1,1)
    turnLeft(1,1.5)
    forward(1,1)
    danceMove1 = 0
    while danceMove1 < 10:
        forward(1,.2)
        turnLeft(1,.1)
        danceMove1 += 1
    danceMove2 = 0
    while danceMove2 < 10:
        backward(1,.2)
        turnRight(1,.1)
        danceMove2 += 1
    danceMove3 = 0
    while danceMove3 < 4:
        forward(1,1)
        backward(1,1)
        turnRight(1,.4)
        danceMove3 += 1
    x = makeSong("e .5;e .5; e 1; e .5; e .5; e 1; e .5; g .5; c .5; d .5; e 2;e .5;e .5; e 1;e .5; e .5; e 1; e .5; g .5; c .5; d .5; e 2;e .5;e .5; e 1; e .5; e .5; e 1; e .5; g .5; c .5; d .5; e 2;")
    playSong(x)

def menu():
    print("1. The Twerk")
    print("2. The X")
    print("3. Jingle Bells")
    print("0. Exit")
    userInput = input("Which dance step/song would you like?")
    userInput = int(userInput)
    if userInput < 4:
        if userInput == 1:
            y = 0
            while y < 10:
                turnLeft(1,.1)
                turnRight(1,.1)
                y += 1
            return
        elif userInput == 2:
            forward(1,1)
            backward(1,2)
            forward(1,1)
            turnLeft(1,.75)
            forward(1,1)
            backward(1,2)
            forward(1,1)
            return
        elif userInput == 3:
            x = makeSong("e .5;e .5; e 1; e .5; e .5; e 1; e .5; g .5; c .5; d .5; e 2;")
            playSong(x)
            return
        else:
            print("Have a good day!")
            return
    else:
        print("I'm sorry, I don't know that one.")
        menu()
        return