# 13-1-22
# stone-paper-scissor

# rules of game
import random     # picks any random value from given option 

def gameWin(computer, player):

# If you and computer choose same option then it will be tie!
    if computer == player:     
        return None
    
# if computer choose stone
    elif computer == 'o':
        if player == 's':
            return False 
        elif player == 'p':
            return True

# if computer choose paper
    elif computer == 'p':
        if player == 'o':
            return False 
        elif player == 's':
            return True  

# if computer choose scissor
    elif computer == 's':
        if player == 'p':
            return False 
        elif player == 'o':
            return True   


# playing time 
print("computer's turn: choose from stone(o) paper(p) and scissor(s)?")
randNo = random.randint(1, 3)
if randNo == 1:
    computer = 'o'
elif randNo == 2:
    computer = 'p'
elif randNo == 3:
    computer = 's'


player = input("player's turn: choose from stone(o) paper(p) and scissor(s)?: ")
a = gameWin(computer, player)


print(f"computer chose {computer}")
print(f"player chose {player}")

if a == None:
    print("This game is tie!")
elif a:
    print("you win!")
else:
    print("you lost (*~*)")


