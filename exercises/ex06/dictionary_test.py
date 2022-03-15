"""EX06: Practice with testing a dicitonary."""

__author__ = "730329470"

from dictionary import invert 
from dictionary import favorite_color
from dictionary import count


def test_invert() -> None:
    """Testing for" invert part one."""
    webster: dict[str, str] = {'zoe': 'obumneke', 'amber': 'maduike'}
    assert invert(webster) == {'obumneke': 'zoe', 'maduike': 'amber'}


def test_invert_part_two() -> None:
    """Testing for invert part two."""
    webster: dict[str, str] = {'rubber': 'eraser', 'color': 'colour'}
    assert invert(webster) == {'eraser': 'rubber', 'colour': 'color'}


def test_invert_part_part_three() -> None:
    """Testing for invert part two."""
    webster: dict[str, str] = {}
    assert invert(webster) == {}


def test_favorite_color() -> None:
    """Testing for favorite color part one."""
    merriam: dict[str, str] = {'amber': 'blue', 'zoe': 'green', 'audrey': 'blue'}
    assert favorite_color(merriam) == 'blue'


def test_favorite_color_part_two() -> None:
    """Testing for favorite color part two."""
    merriam: dict[str, str] = {'apple': 'brown', 'grape': 'purple', 'banana': 'brown', 'strawberry': 'purple'}
    assert favorite_color(merriam) == 'brown'


def test_favorite_color_part_three() -> None:
    """Testing for favorite color part two."""
    merriam: dict[str, str] = {}
    assert favorite_color(merriam) == ''


def test_count() -> None:
    """Testing for the count of values in the string part one."""
    chosen: list[str] = ['zoe', 'obumneke', 'amber', 'maduike', 'zoe']
    assert count(chosen) == {'zoe': 2, 'obumneke': 1, 'amber': 1, 'maduike': 1}


def test_count_part_two() -> None:
    """Testing for the count of values in the string part two."""
    chosen: list[str] = ['1', '2', '3', '4', '2', '4']
    assert count(chosen) == {'1': 1, '2': 2, '3': 1, '4': 2}


def test_count_part_three() -> None:
    """Testing for the count of values in the string part two."""
    chosen: list[str] = []
    assert count(chosen) == {}