# ScriptTemplate.py
# Author: Ashley Soderlund
# Description: Program will simulate a game of craps

from random import randrange

def rollDice():
    diceOne = randrange(1,7)
    diceTwo = randrange(1,7)
    print("Dice one:", diceOne)
    print("Dice two:", diceTwo)
    total = diceOne + diceTwo
    return total

def menu():
    print()
    print("|----------------------------|")
    print("|          Menu              |")
    print("|----------------------------|")
    print("|       1) Play Craps        |")
    print("|       2) Exit              |")
    print("|----------------------------|")
    print()

def validInput(option):
    check = 0
    while check == 0:
            if option < 1 or option > 2:
                 print("Not a valid input.")
                 option = int(input("Enter an acceptable option (1-2): "))
                 print()
            else:
                check = 1
    return (option)

def main():
    #Asks user for their name
    userName = input("Enter in your name please: ")
    print()
    print("Thank you,", userName)
    input("Press <Enter> to continue.")
    print()

    #Sentinal to enter while loop
    option = 1

    while option != 2:
        menu()

        #Asks for user input
        option = int(input("Please enter a number from the menu (1-2), " +  userName + ": "))
        print()

        #Calls validInput() to make sure values inputed are 1 or 2
        option = validInput(option)

        #Turns start out at 0
        n = 0

        #The game when user chooses option 1.
        if option == 1:
            #Gets the first roll of the dice
            total = rollDice()
            #Number of turns
            n = n+1
            
            print(userName +"'s 1 st Roll Total:", total)
            print("--------------------------------------")
            print()

            #Decides if user wins, loses, or moves on depending on their first roll
            if total == 2 or total == 3 or total == 12:
                print()
                print(userName,  "I am sorry to inform you, that you have lost on your first roll because you rolled a", total)
                break
            elif total == 7 or total == 11:
                print()
                print(userName, "you have won the game on your first roll because you rolled a", total)
                break

            #sentinal value to enter the following loops
            total2 = 20
    
            while total2 != 7:
                if total2 != 7:

                    #Simulates the user throwing the dice adn give them time to read
                    input("Press <Enter> to roll again, "+ userName)
                    print()

                    #Calls rollDice() to get a new set of values 
                    total2 = rollDice()
                    #n is the number of turns the users has used
                    n = n+1

                    #if statements makes sure correct number matches (nd/rd/th) ending
                    if n == 2:
                        print(userName + "'s",n, "nd Roll Total:", total2)
                        print("--------------------------------------")
                        print()
                    elif n == 3:
                        print(userName + "'s",n, "rd Roll Total:", total2)
                        print("--------------------------------------")
                        print()
                    else:
                        print(userName + "'s",n, "th Roll Total:", total2)
                        print("--------------------------------------")
                        print()

                    #Decides if user win, loses, or keeps going depending on rolls after their first one
                    if total2 == total:
                        print()
                        print(userName, "you have won the game on your", n,"(nd/rd/th) turn because you rolled a", total2)
                        print(userName, "your first and", n,"(nd/rd/th) turn had matching values!")
                        break
                    elif total2 == 7:
                        print()
                        print(userName, "sadly, you have lost the game because you rolled a", total2, "on your", n, "(nd/rd/th) turn.")
                        break
                else:
                    break
            break

    #End comment that thanks the user for playing no matter how they end            
    print()
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
    print("Thank you for playing the game!")
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
            
    
              

main()
