"""EX02 - One Shot Wordle - Closer to Wordle!"""

__author__ = "730329470"

secret: str = "python"
user_word: str = input("What is your 6-letter guess? ")
i: int = len(user_word)
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
o: int = 0
g: str = ""

while i != len(secret):
    user_word = input(f"That was not 6 letters! Try again: ");
    i = len(user_word)

if i == len(secret):
    while o < len(secret):
        if user_word[o] == secret[o]:
            g = g + GREEN_BOX
        else:
            found: bool = False
            ai: int = 0
            while found != True and ai < len(secret):
                if user_word[o] == secret[ai]:
                    found = True
                else:
                    ai = ai + 1
            if found == True:
                g = g + YELLOW_BOX
            else:
                g = g + WHITE_BOX
        o = o + 1
    print(g)
    if secret == user_word:
        print("Woo! You got it!")
    else:
        print("Not quite. Play again soon!")



