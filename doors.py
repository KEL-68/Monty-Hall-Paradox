# So basicly what this code do is make the computer chose(random chose) between 3 door and afher his frist guess we gonna revel that a door he (not the one he chosed) is not the right door and we gonna see if changing the door make the posibikity of guessing the other door higher sorry for the bad typo
from random import randint

def door(times=10000):
    global right_guess
    global wrong_guess
    right_guess = 0
    wrong_guess = 0
    for i in range(times):

        therightdoor = randint(1,3)
        computerguess = randint(1,3)
        if therightdoor == computerguess:
            right_guess += 1
            print("computer guessed right 🔴")
        else:
            wrong_guess += 1
            print("computer guessed wrong 🟢")
door(1000000)

print("\n\n\n")
print(f"the computer guessed right  {right_guess} times \n and guessed wrong {wrong_guess} times ")