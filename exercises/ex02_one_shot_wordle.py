"""EX02 - One Shot Wordle - Closer to Wordle!"""

__author__ = "730329470"

secret: str = "python"
user_word: str = input(f"What is your { len(secret) }-letter guess? ")
i: int = len(user_word)
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
o: int = 0
g: str = ""

while i != len(secret):
    user_word = input(f"That was not { len(secret) } letters! Try again: ")
    i = len(user_word)
    # use f string!
    # make I the length of the new user_word

if i == len(secret):
    # emojis have to come before the final sayings
    while o < len(secret):
        if user_word[o] == secret[o]:
            g = g + GREEN_BOX
        else:
            found: bool = False
            ai: int = 0
            # ai needs to repeat for each index
            while not found and ai < len(secret):
                if user_word[o] == secret[ai]:
                    found = True
                else:
                    ai = ai + 1
            if found:
                g = g + YELLOW_BOX
            else:
                g = g + WHITE_BOX
        o = o + 1
    print(g)
    if secret == user_word:
        print("Woo! You got it!")
    else:
        print("Not quite. Play again soon!")