"""An example of for in syntax."""

names: list[str] = ["Kris", "Kaki", "Ezri", "Marc"]

#Example of iterating through names using a while loop
i: int = 0
print("while output:")
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

print("for..in output:")
for name in names:
    print(name)