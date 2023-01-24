# creating a random interger 
import random
jackpot_num = random.randint(0, 50)

# taking input from user
guess_num = int(input("guess a number between 0 to 50: "))

#here while guess is not = to jackpot, it will run the loop or else it will print last stmt
while guess_num != jackpot_num: 
    if guess_num < jackpot_num:
        print("guess higher") 
    else:
        print("guess lower")
        
    guess_num = int(input("guess a number between 0 to 50: "))

print("correct answer") 