import random
import logo_art
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5
def set_difficulty(level_chosen):
    if level_chosen=='easy':
        return EASY_LEVEL_ATTEMPTS
    elif level_chosen=='hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        return
def check_answer(guessed_number,answer,attempts):
    if guessed_number<answer:
        print("your guess is too low")
        return attempts-1
    elif guessed_number>answer:
        print("your guess is to high")
        return attempts-1
    else:
        print(f"ypur guess is correct... the answer was {answer}")
def game1():
    print(logo_art.logo)
    print("let me think of a numnber between 1 to 50")
    answer=random.randint(1,50)
    level=input("chosen level of difficulty.. type 'easy' or 'hard':")
    attempts=set_difficulty(level)
    if attempts!=EASY_LEVEL_ATTEMPTS and attempts!=HARD_LEVEL_ATTEMPTS:
        print("you have entered wrong input please enter valid input")
        return
    guessed_number=0
    while guessed_number!=answer:
        print(f"you have {attempts} attempts remaining to guess the number.")
        guessed_number=int(input("Guess a number:"))
        attempts=check_answer(guessed_number,answer,attempts)
        if attempts==0:
            print("you are out of guesses.... you lose!!")
            return
        elif guessed_number!=answer:
            print("Guess again.")
game1()
