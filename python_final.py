# soderlund_final_program.py
# Author: Ashley Soderlund
# Description:This program holds many different functions that we have learned
#throughout the semester

from graphics import *

def speedingTicket():
    while True:
        try:
            speedLimit = int(input("Please enter the designated speed limit: "))
        except ValueError:
            print("Enter a valid integer.")
        else:
            break
        
    while True:
        try:
            driverSpeed = int(input("Please enter the clocked speed of the driver: "))
        except ValueError:
            print("Enter a valid integer.")
        else:
            break
    print()
    print("------------------------------------------------------------------------")
    print()

    ticketCost = 0
    milesOver = driverSpeed - speedLimit
    excessiveSpeed = speedLimit + speedLimit

    if driverSpeed > speedLimit:
        print("The driver was driving over the speed limit by", milesOver, "mph.")
        ticketCost = ticketCost + (milesOver * 5)
        if driverSpeed > excessiveSpeed:
            print("The driver's speed was twice the speed limit and will be fined")
            print("and additional $90.")
            ticketCost = ticketCost + 90
    else:
        print("Driver is driving within the speed limit.")

    finalCost = str(ticketCost)
    print("Total cost of the ticket is $" + finalCost + ".")

def drawCircles():
    win = GraphWin("Circle Clicker",400,400)
    circ = Circle(Point(100,100),20)
    circ.setFill('red')
    

    message = Text(Point(200,380), "Click Anywhere to Display a Circle")
    message.draw(win)

    p = win.getMouse()
    c = circ.getCenter()
    dx = p.getX() - c.getX()
    dy = p.getY() - c.getY()
    circ2 = circ.clone()
    circ2.move(dx,dy)
    circ2.draw(win)

    p = win.getMouse()
    c = circ.getCenter()
    dx = p.getX() - c.getX()
    dy = p.getY() - c.getY()
    circ3 = circ.clone()
    circ3.move(dx,dy)
    circ3.draw(win)

    p = win.getMouse()
    c = circ.getCenter()
    dx = p.getX() - c.getX()
    dy = p.getY() - c.getY()
    circ4 = circ.clone()
    circ4.move(dx,dy)
    circ4.draw(win)

    p = win.getMouse()
    c = circ.getCenter()
    dx = p.getX() - c.getX()
    dy = p.getY() - c.getY()
    circ5 = circ.clone()
    circ5.move(dx,dy)
    circ5.draw(win)

    p = win.getMouse()
    c = circ.getCenter()
    dx = p.getX() - c.getX()
    dy = p.getY() - c.getY()
    circ6 = circ.clone()
    circ6.move(dx,dy)
    circ6.draw(win)
    
    message.setText("Click anywhere to quit.")
    win.getMouse()
    win.close()

def drawBullseye():
    win = GraphWin("Drawing a Bullseye",300,300)

    circ5 = Circle(Point(150,150),100)
    circ5.setFill("white")
    circ5.draw(win)

    circ4 = Circle(Point(150,150),80)
    circ4.setFill("black")
    circ4.draw(win)

    circ3 = Circle(Point(150,150),60)
    circ3.setFill("blue")
    circ3.draw(win)

    circ2 = Circle(Point(150,150),40)
    circ2.setFill("red")
    circ2.draw(win)

    circ1 = Circle(Point(150,150), 20)
    circ1.setFill("yellow")
    circ1.draw(win)
    
    button = Text(Point(150,280),"Click Anywhere to Quit")
    button.draw(win)
    win.getMouse()
    win.close()

def userNames():
    fNames = open("C:/temp/user_names.txt", "r")

    print("Full Name - UserID")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    for line in fNames:
        first,last = line.split()
        userNames = (first[0]+last[0:5]).upper()
        print(first, last, "-", userNames)
     
    fNames.close()

def temp():
    win = GraphWin("Celsius Converter", 400, 300)
    win.setCoords(0.0,0.0,3.0,4.0)

    Text(Point(1,3),"   Celsius Temperature: ").draw(win)
    Text(Point(1,1),"Fahrenheit Temperature: ").draw(win)
    inputText = Entry(Point(2.25, 3),5)
    inputText.setText("0.0")
    inputText.draw(win)
    outputText = Text(Point(2.25,1)," ")
    outputText.draw(win)
    button = Text(Point(1.5,2.0),"Convert It")
    button.draw(win)
    Rectangle(Point(1,1.5), Point(2, 2.25)).draw(win)

    win.getMouse()

    celsius = float(inputText.getText())
    fahrenheit = 9.0/5.0 * celsius + 32

    outputText.setText(round(fahrenheit,2))
    button.setText("Quit")

    win.getMouse()
    win.close()

def birthdayChorus():
    print("Happy Birthday to you!")
    
def happpyBday(firstName):
    print("Happy Birthday dear,", firstName)

def itemPrice(firstName):
    print("Let's calculate the sales tax for a purchase you have,", firstName)
    while True:
        try:
            salePrice = int(input("Enter the sale price of a product: "))
        except ValueError:
            print("Enter an integer.")
        else:
            break
        
    salesTax = .065 

    taxRate = salePrice * salesTax
    totalPrice = salePrice + taxRate

    print()
    print(firstName, "here is the information about your item:")
    print("---------------------------------------------------")
    print("Sale Price", salePrice)
    print("Sales Tax:", salesTax)
    print("Total Cost:", totalPrice)
    print()

def distLightning(userName):
    while True:
        try:
            timeSeconds = int(input("Enter the amount of time, in seconds, from the visual strike to the sound of the lightning strike: "))
        except ValueError:
            print("Enter an integer.")
        else:
            break
        
    feetDistance = (timeSeconds * 1100)
    milesDistance = (feetDistance / 5280)

    milesDistance = int(milesDistance)

    print()
    print("The strike is", feetDistance,"feet away.")
    print("The strike is", milesDistance,"miles away.")

    if milesDistance < 1:
        print(userName, "RUN FOR COVER!")
    elif milesDistance > 2:
        print(userName, "you are safe.")

        
#Holds the menu
def menu():
    print()
    print("|---------------------------------------------------------|")
    print("|                        Menu                             |")
    print("|---------------------------------------------------------|")
    print("|       1) A Greeting Message                             |")
    print("|       2) Calculating the Total Price of an Item         |")
    print("|       3) Calculating Distance to Lightning Strike       |")
    print("|       4) Converting Celsius to Farenheit                |")
    print("|       5) Creating UserID from an Input File             |")
    print("|       6) Happy Birthday Song                            |")
    print("|       7) Judging a Speeding Ticket                      |")
    print("|       8) Creating a Bullseye Graphic                    |")
    print("|       9) Creating Circles by Clicking the Mouse         |")
    print("|       10) Exit Program                                  |")
    print("|---------------------------------------------------------|")
    print()

def validInput(option):
    check = 0
    while check == 0:
            if int(option) < 1 or int(option) > 10:
                 print("Not a valid input.")
                 #try statement from chapter 7
                 while True:
                     try:
                         option = int(input("Enter an acceptable option (1-10): "))
                         print()
                     except ValueError:
                         print("Make sure number is between 1 and 10")
                     else:
                         break
            else:
                check = 1
    return (option)

def main():
    #Asks user for their name, using try statement(from chapter 7) to make sure it is correct value
    while True:
        try:
            userName = input("Enter in your first and last name please: ")
            firstName, LastName = userName.split()
            print()
            print("Thank you,", userName)
        except ValueError:
            print("Make sure to enter two words with a space between them.")
        else:
            #ValueError was not thrown
            break
   

    #Sentinal to enter while loop
    option = 1

    while int(option) != 10: 
        menu()

        #Exception Handling from Chapter 7, try statement
        while True:
            try:
                option = int(input("Please enter a number from the menu (1-10), " +  userName + ": "))
                print()
            except ValueError:
                print("Not a valid input.")
            else:
                #ValueError was not thrown
                break
                             
        #Calls validInput() to make sure numerical values inputed are between 1 and 10
        option = validInput(int(option))


        #If statements to direct which part of the program the user chose
        if int(option) == 1:
            print("Welcome", firstName, "to this program! There are a lot of options")
            print("to use, so I hope you try them out and have some fun.")
            print()
            input("Press <Enter> to continue.")
        elif int(option) == 2:
            print("This option will have you enter a price of an item and will calculate")
            print("the final price after sales tax.")
            print()
            itemPrice(firstName)
            print()
            input("Press <Enter> to continue.")
        elif int(option) == 3:
            print("This option will have you enter the seconds between a flash of lightning")
            print("and the sound of the thunder and calculate how far the lightning stike is")
            print("away from your position.")
            print()
            distLightning(userName)
            print()
            input("Press <Enter> to continue.")
        elif int(option) == 4:
            print("This option will allow you to convert the temperature in Celsius to the")
            print("temperature in Farenheit in a separate graphical window.")
            print()
            temp()
            print()
            input("Press <Enter> to continue.")
        elif int(option) == 5:
            print("This option will take a list of names and create usernames in all capital")
            print("letters in the form first name initial followed by first five letters of")
            print("the last name.")
            print()
            userNames()
            print()
            input("Press <Enter> to continue.")
        elif int(option) == 6:
            print("This option sings Happy Birthday.")
            print()
            birthdayChorus()
            birthdayChorus()
            happpyBday(firstName)
            birthdayChorus()
            print()
            input("Press <Enter> to continue.")
            print()
        elif int(option) == 7:
            print("This option has the user enter the posted speed limit and the driver's")
            print("speed and will determine how much the speeding ticket will cost depending")
            print("on how fast they were driving.")
            print()
            speedingTicket()
            print()
            input("Press <Enter> to continue.")
        elif int(option) == 8:
            print("This option opens a second window and draws a bullseye out of circles.")
            drawBullseye()
            print()
            input("Press <Enter> to continue.")
        elif int(option) == 9:
            print("This option allows you to click certain locations five times and draws")
            print("a circle at those locations.")
            print()
            drawCircles()
            print()
            input("Press <Enter> to continue.")
           
                    

    #End comment that thanks the user for playing no matter how they end            
    print()
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
    print("Thank you for using this program,", userName)
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
            
    
              

main()
