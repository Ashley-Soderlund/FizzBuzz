#Ashley Soderlund
#1/24/20
#FizzBuzz Game

for number in range (1,101):
    answer = ""
    if (number % 3 == 0):
        answer += "fizz"
    if (number % 5 == 0):
        answer += "buzz"
    if (len(answer) == 0):
        print(number)
    else:
        print(answer)
