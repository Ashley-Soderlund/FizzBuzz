#Ashley Soderlund
#1/22/20
#Calculator Program

math = 2
while math != "e":
    math = input("Enter a mathmatical equation or 'e' to exit: ")
    if math != "e":
        print(eval(math))
