from random import randint

# if guess = random:
#     for x in range(0,10):
#     random = randint(0,100)
#     print(random)
#
# guess = input("Please enter no: ")
x = randint(1,100)
guess = int(input("Please insert number: "))
count = 1

while x <= 100 and x >=1:
    count += 1
    if guess > x:
        print("The guess is too high")
        guess = int(input("Please guess a number again: : "))

    elif guess < x:
        print("The guess is too Low")
        guess = int(input("Please guess a number again: : "))

    else:
        print("your guesses are correct")
        print("tries: ", + count)
        break






