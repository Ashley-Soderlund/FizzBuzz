#Ashley Soderlund
#1/29/19
#Various programs using math to do different functions

def pi_function():

    #get the odd numbers in the sequence
    running_total = 0
    current_sign = 1

    for i in range(1,1000000,2):
        running_total = running_total + 1/i * current_sign

        #create the alternating sign
        current_sign *= -1

    #multiply by 4
    running_total *= 4
    
    print(running_total)
    
def factorial(number):
    total = 0
    number += 1

    for i in range (1, number):
        if total == 0:
            total = 1
        total = i * total

    number -= 1

    #Returns the factorial value
    return (total)
    print("--------------------------------------------------------------------")

def collatz(m):
    #Prints the values as they change during the collatz conjecture
    while m != 1:
        print(m)
        if (m % 2) == 0:
            m = m/2
        else:
            m = (m*3)+1
    print(m)
    print("The answer will always make its way to 1, through the given math")
    print("statements, but this is still not 100% proven though it has always")
    print("been true with the tests people have done.")
    print("--------------------------------------------------------------------")
    
def angles(n):
    #Computes the interior angle of a regular polygon with n sides
    degree = 360/n
    print("The degrees of each angle on a shape with", n, "sides equals", degree)
    print("--------------------------------------------------------------------")
    
def least_common_multiple(a,b):
    if a > b:
        greater = a
    else:
        greater = b

    while (True):
        if((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater += 1

    print("The least common multiple of", a, "and", b, "is-")
    #returns the lcm of the two numbers
    return(lcm)
    
    
def main():
    print("Value of pi:")
    pi_function()
    print("--------------------------------------------------------------------")

    print("Factorial of a Number:")
    #Accepts a single positive integer
    number = int(input("Enter a number you want to find the factorial of: "))
    print(factorial(number))
    print("--------------------------------------------------------------------")

    print("The Angles of a Shape Depending on the Number of Sides:")
    #Accepts a positive integer variable n
    n = int(input("Enter the number of sides on a shape of your choice: "))
    angles(n)

    print("Least Common Factor of Two Numbers:")
    a = int(input("Enter the first integer you want to find the least common multiple with: "))
    b = int(input("Enter the second integer: "))
    #Accets two positive integers into the function
    print(least_common_multiple(a,b))
    print("--------------------------------------------------------------------")

    print("Collatz Conjecture of a Number:")
    #Accepts a single positive integer variable m (because having 2 variables
    #with the same name can get confusing, so I didn't use n again)
    m = int(input("Enter a random positive integer to test the collatz conjecture: "))
    collatz(m)        

main()
