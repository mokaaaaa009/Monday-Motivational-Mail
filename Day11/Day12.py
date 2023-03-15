import random

cnt = 0
myNumber = random.randint(1, 100)


def guessing(number):
    flage = False
    if myNumber == int(number):
        flage = True
        print("You got it !!!")
        return flage
    elif myNumber > int(number):
        print("Too low.\nGuess again.")
    else:
        print("Too High.\nGuess again.")
    return flage


print("Welcome to the Number Guessing Game!")
print("I;m thinking of a number between 1 and 100")
level = input("Choose a difficulty Type'easy' or 'hard': ")
def game():
  myNumber = random.randint(1, 100)
  if level == "hard":
    cnt = 5
    while cnt != 0:
        flage = guessing(number=input("Make a guess: "))

        if flage == False:
            print(f"You have {cnt} attempts remaining to guess the number .\n")
        else:
            break
        cnt -= 1
  else:
    cnt = 10
    while cnt != 0:
        flage = guessing(number=input("Make a guess: "))
        if flage == False:
            print(f"You have {cnt} attempts remaining to guess the number .\n")
        else:
            break
        cnt -= 1
    if cnt == 0:
        print(f"Bad Luck the Number is: {myNumber}\n")
endgame='Y'
while endgame == 'Y':
 game()
 endgame=input("Press 'y' to Play Again 'n' to Exit ")