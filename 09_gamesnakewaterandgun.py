import random

def gamewin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        if you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        if you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        if you == 'w':
            return True

comp = print("computer turn: snake(s) water(w) gun(g)")
randNo = random.randint(1,3)
if randNo == "1":
    comp = 's'
elif randNo == "2":
    comp = 'w'
elif randNo == "3":
    comp = 'g'

you = input("your turn: snake(s) water(w) gun(g)")
print(f"computer choose{comp}")
print(f"you choose {you}")
a = gamewin(comp, you)
if a == None:
    print("the game is tie")
elif a:
    print("you win the game")
else:
    print("you lose")