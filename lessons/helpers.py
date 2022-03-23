"""Demonstrate defining a module imported elsewhere."""


THE_ANSWER: int = 42


def main() -> None:
    print(powerful(2, 10))
    print("helpers.py run as a module")


def powerful(x: float, n: float) -> float:
    """Raises x to the power of n."""
    return x ** n


# Idiom for making a module able to run as a program
# or have its global deinitions import 
if __name__ == "__main__":
    main()
else:
    # It is not idiomatic to have an else branch
    print(f"helpers.py was evaluated: {__name__}")