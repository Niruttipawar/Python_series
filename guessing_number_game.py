import random

num=random.randint(1,10)

guess=int(input("Guess the number :-"))

while guess==num:
    print("you guessed the right number")
    break

else:
    print("you guessed the wrong number")