"""EX06: Practice with making a dicitonary."""

__author__ = "730329470"


def invert(webster: dict[str, str]) -> dict[str, str]: 
    """Inverting a dictionary."""
    inv_web: dict[str, str] = {}
    value: str = ""
    for key in webster:
        value = webster[key]
        inv_web[value] = key
    return inv_web


def favorite_color(merriam: dict[str, str]) -> str:
    """What is the most popular color."""
    color: str = ""
    i: int = 0
    final_color: str = ""
    new_dict: dict[str, int] = {}
    for key in merriam:
        color = merriam[key]
        if color in new_dict:
            new_dict[color] += 1
        else:
            new_dict[color] = 1
    for key in new_dict:
        if new_dict[key] > i:
            i = new_dict[key]
            final_color = key
    return final_color
  

def count(chosen: list[str]) -> dict[str, int]: 
    """Count the amount of times a value appears."""
    final_count: dict[str, int] = {}
    for counter in chosen:
        if counter in final_count:
            final_count[counter] += 1
        else:
            final_count[counter] = 1
    
    return final_count