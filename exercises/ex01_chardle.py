"""EX01 - Chardle - A cute step toward Wordle"""

__author__ = "730329470"


word: str = input("Enter a 5-character word: ")

if len(word) != 5:
    print(" Error: Word must contain 5 characters")
    exit()

single: str = input("Enter a single character: ")

if len(single) != 1:
    print( "Error: Character must be a single character.")
    exit()

match: int = 0

print("Searching for " + single + " in " + word)

if single == word[0]:
    print(single + " found at index 0")
    match = match + 1

if single == word[1]:
    print(single + " found at index 1")
    match = match + 1
    

if single == word[2]:
    print(single + " found at index 2")
    match = match + 1

if single == word[3]:
    print(single + " found at index 3")
    match = match+ 1

if single == word[4]:
    print(single + " found at index 4")
    match = match + 1

if match == 0:
    print("No instances of " + single + " found in " + word)
else:
    if match == 1:
        print("1 instance of " + single + " found in " + word)
    else:
        if match == 2:
            print("2 instances of " + single + " found in " + word)
        else:
            if match == 3:
                print(" 3 instances of " + single + " found in " + word)
            else:
                if match == 4:
                    print(" 4 instances of " + single + " found in " + word)
                else:
                    if match == 5:
                        print( "5 instances of " + single + " found in " + word)
