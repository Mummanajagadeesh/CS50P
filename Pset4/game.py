import random

while(True):
    try:
        level=int(input("Level:"))
        if level>0:
            break
    except ValueError:
        continue

def prompt_guess():
    while(True):
        try:
            guess=int(input("Guess:"))
            if guess>0:
                return guess
            elif guess==0:
                print("Too small!")
                continue
        except ValueError:
            continue

list1=list(range(1,level+1))
key=random.choice(list1)

while(True):
    guess=prompt_guess()
    if guess<key:
        print("Too small!")
        continue
    elif guess>key:
        print("Too large!")
        continue
    elif guess==key:
        print("Just right!")
        break
