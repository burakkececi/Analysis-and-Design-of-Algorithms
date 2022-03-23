import random
random.seed()
randomNumber = random.randrange(0,100)
i,number = 1, -1
while number != randomNumber:
    number = int(input("Enter the number between 0-100: "))
    if(number < randomNumber):
        print("Up")
    elif (number > randomNumber):
        print("Down")
    else:
        print("Congratulations! Got it on the {}th try. ".format(i))
        break

    i = i + 1

