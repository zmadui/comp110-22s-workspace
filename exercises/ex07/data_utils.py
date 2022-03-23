"""Dictionary related utility functions."""

__author__ = "730329470"
# Define your functions below
from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
        
    return result


def head(column_table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Make a dictionary of all the columns in a row"""
    webster: dict[str, list[str]] = {}
    for column in column_table:
        i: int = 0
        first_column_value: list[str] = []
        if N > len(column_table[column]):
            return column_table
        while i < N:
            first_value: str = column_table[column][i]
            first_column_value.append(first_value)
            i += 1
        webster[column] = first_column_value
    return webster


def select(column_table: dict[str, list[str]], column_name: list[str]) -> dict[str, list[str]]:
    """Create a subset of the columns"""
    result: dict[str, list[str]] = {}
    for column in column_name:
        result[column] = column_table[column]
    return result


def concat(table_one: dict[str, list[str]], table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Create a table that combines two tables"""
    result: dict[str, list[str]] = {}
    for column in table_one:
        result[column] = table_one[column]
    for column in table_two:
        if column in result:
            result[column] += table_two[column]
        else:
            result[column] = table_two[column ]
    return result


def count( frequency: list[str]) -> dict[str, int]:
    """Counting how often a value appears"""
    webster: dict[str, int] = {}
    for number in frequency:
        if number in webster:
            webster[number] += 1
        else:
            webster[number] = 1
    return webster


