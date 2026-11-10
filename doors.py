# So basicly what this code do is make the computer chose(random chose) between 3 door and afher his frist guess we gonna revel that a door he (not the one he chosed) is not the right door and we gonna see if changing the door make the posibikity of guessing the other door higher sorry for the bad typo
from random import randint , choice

def door(times=1000):
    global change_guess
    global dontchange_guess
    global time
    time = times
    change_guess = 0
    dontchange_guess = 0
    for i in range(times):

        therightdoor = randint(1,3)
        computerguess = randint(1,3)
        revealed = choice([n for n in range(1,4) if n != therightdoor and n!= computerguess ])
        if computerguess != revealed:
            if computerguess == therightdoor:
                dontchange_guess+=1
            else:
                change_guess+=1

door(10000000)

print("\n\n\n")
print(f"change guesses : {change_guess/time*100}\ndontchange_guess: {dontchange_guess/time*100}")