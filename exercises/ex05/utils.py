"""EX: 05 Making the perfect list.""" 

__author__ = "730329470"


def only_evens(numbers: list[int]) -> list[int]:
    """Return the even numbers in a list."""
    i: int = 0
    end_list: list[int] = []
    while i < len(numbers):
        if numbers[i] % 2 == 0:
            end_list.append(numbers[i])
            i += 1
        else:
            i += 1
    return end_list


def sub(numbers: list[int], x: int, y: int) -> list[int]:
    """Generate a subset of a list."""
    end_list: list[int] = []
    if len(numbers) == 0 or x > len(numbers) or y <= 0:
        return end_list
    if len(numbers) > 0:
        if x < 0:
            x = 0
        if y > len(numbers):
            y = len(numbers) 
        i: int = x
        while i >= x and i < y:
            end_list.append(numbers[i])
            i += 1
    else: 
        end_list = []
    return end_list


def concat(beginning_list: list[int], final_list: list[int]) -> list[int]:
    """Combining two lists."""
    i: int = 0
    while i < len(final_list):
        beginning_list.append(final_list[i])
        i += 1
    return beginning_list