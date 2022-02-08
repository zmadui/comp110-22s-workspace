"""Ex03 - 6 Tries Wordle."""

__author__ = "730329470"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(word: str, main_char: str) -> bool:
    """Given a word and character as a parameter, determine if the character is present in the word."""
    assert len(main_char) == 1
    i: int = 0
    while i < len(word):
        if main_char != word[i]:
            i += 1
        else:
            return True
    return False


def emojified(guess: str, secret: str) -> str:
    """Insert an emoji based on if the character in the guess matches with a charcter in the secret."""
    assert len(guess) == len(secret)

    i: int = 0
    emoji: str = ""
    while i < len(secret):
        if guess[i] == secret[i]:
            emoji = emoji + GREEN_BOX
        else:
            if contains_char(secret, guess[i]):
                emoji = emoji + YELLOW_BOX 
            else:
                emoji = emoji + WHITE_BOX
        i += 1
    return emoji


def input_guess(expected: int) -> str:
    """Determine if the guess is the correct length."""
    guess: str = input(f"Enter a {expected} character word: ")
    while len(guess) != expected:
        guess = input(f"That was not {expected} letters! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    n: int = 0
    word_entered: str = ""
    won: bool = False
    while n < len(secret) + 1 and won == False:
        print(f"=== Turn {n+1}/6 ===")
        word_entered = input_guess(len(secret))
        print(emojified(word_entered, secret))
        n += 1 
        if word_entered == secret:
            won = True
    if won == True:
        print(f"You won in {n}/6 turns!")
    else:
        if won == False:
            print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()