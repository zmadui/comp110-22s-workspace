"""EX: 05 Testing for Utils.""" 

__author__ = "730329470"

from utils import only_evens
from utils import sub
from utils import concat


def test_only_evens() -> None:
    """Testing for only evens part one."""
    numbers: list[int] = [1, 3, 4]
    assert only_evens(numbers) == [4]


def test_only_evens_two() -> None:
    """Testing for only evens part two."""
    numbers: list[int] = []
    assert only_evens(numbers) == []


def test_only_evens_three() -> None:
    """Testing for only evens part three."""
    numbers: list[int] = [750, 751, 752, 780]
    assert only_evens(numbers) == [750, 752, 780]


def test_sub_one() -> None:
    """Testing for sub part one."""
    numbers: list[int] = [1, 2, 3, 4, 8, 9]
    assert sub(numbers, 0, 4) == [1, 2, 3, 4]


def test_sub_two() -> None:
    """Testing for sub part two."""
    numbers: list[int] = []
    assert sub(numbers, 0, 1) == []


def test_sub_three() -> None:
    """Testing for sub part three."""
    numbers: list[int] = [1, 3, 4, 5]
    assert sub(numbers, -1, 10) == [1, 3, 4, 5]


def test_concat() -> None:
    """Testing for concat part one."""
    beginning_list: list[int] = [1, 2]
    final_list: list[int] = [10, 11]
    assert concat(beginning_list, final_list) == [1, 2, 10, 11]


def test_concat_two() -> None:
    """Testing for concat part two."""
    beginning_list: list[int] = []
    final_list: list[int] = [1, 2]
    assert concat(beginning_list, final_list) == [1, 2]


def test_concat_three() -> None:
    """Testing for concat part three."""
    beginning_list: list[int] = [-1, 3, 6]
    final_list: list[int] = [8, 9]
    assert concat(beginning_list, final_list) == [-1, 3, 6, 8, 9]