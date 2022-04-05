import random

def guess(x):

    random_number = random.randint(1, x)
    guess = 0


 
    while guess != random_number:
        guess = int(input(f'Guess a numer between 1 and {x}:'))
        if guess < random_number :
            print("Sorry , guess again. Too low ")
        elif guess > random_number :
            print("Sorry , guess again .Too high") 
    print(f" Perfect, congrats . you have done. {random_number}, correctly  ")                 

guess(5)          
