"""Utility class for numerical operations."""

from __future__ import annotations
from optparse import Values

from typing import Union

__author__ = "730329470"


class Simpy:
    values: list[float]
    def __init__(self, values: list[float]): 
        """Constructing a list of values."""
        self.values = values

    def __str__(self) -> str:
        """Converting the given argument into a string."""
        return f"Simpy({self.values})"

    def fill(self, insertment: float, count: int) -> None:
        """Making a list of number and repeating it the number of requested times."""
        i: int = 0
        n: float = 0
        n = insertment
        l: list[float] = []
        while i < count:
            l.append(n)
            i += 1
        self.values = l

    
    def arange(self, start: float, stop: float, step: float=1.0) -> None:
        """Fill with a range of float values."""
        assert step != 0.0
        n: float = start
        l: list[float] = []
        if step < 0:
            while n > stop:
                l.append(n)
                n += step
        else:
            while n < stop:
                l.append(n)
                n += step
        self.values = l


    def sum(self) -> float:
        """Sum of values in list."""
        total: float = 0.0
        i: int = 0
        while i < len(self.values):
            total += self.values[i]
            i += 1
        return total


    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adding values in Simpy."""
        add: list[float] = []
        if isinstance(rhs, float):
            i: int = 0
            while i < len(self.values):
                add.append(self.values[i] + rhs)
                i += 1
            return Simpy(add)
        elif len(self.values) == len(rhs.values):
            i: int = 0
            while i < len(self.values):
                add.append(self.values[i] + rhs.values[i])
                i += 1
            return Simpy(add)
        else:
            return self


    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Exponentially increasing values in Simpy."""
        exponent: list[float] = []
        if isinstance(rhs, float): #how
            i: int = 0
            while i < len(self.values):
                exponent.append(self.values[i] ** rhs)
                i += 1
            return Simpy(exponent)
        elif len(self.values) == len(rhs.values):
            i: int = 0
            while i < len(self.values):
                exponent.append(self.values[i] ** rhs.values[i])
                i += 1
            return Simpy(exponent)
        else:
            return self


    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Making two equal lists."""
        equal: list[bool] = []
        i: int = 0
        correct: bool = True
        incorrect: bool = False
        if isinstance(rhs, float):
            i: int = 0
            while i < len(self.values):
                if self.values[i] == rhs:
                    equal.append(correct)
                else:
                    equal.append(incorrect)
                i += 1
            return equal
        elif len(self.values) == len(rhs.values):
                i: int = 0
                while i < len(self.values):
                    if self.values[i] == rhs.values[i]:
                        equal.append(correct)
                    else:
                        equal.append(incorrect)
                    i += 1
                return equal
        else:
            return equal

                   
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Determining wheher the value is greater."""
        greater: list[bool] = []
        i: int = 0
        correct: bool = True
        incorrect: bool = False
        if isinstance(rhs, float):
            i: int = 0
            while i < len(self.values):
                if self.values[i] > rhs:
                    greater.append(correct)
                else:
                    greater.append(incorrect)
                i += 1
            return greater
        elif len(self.values) == len(rhs.values):
                i: int = 0
                while i < len(self.values):
                    if self.values[i] > rhs.values[i]:
                        greater.append(correct)
                    else:
                        greater.append(incorrect)
                    i += 1
                return greater
        else:
            return greater


    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Obtaining a certain value."""
        i: int = 0
        final: float = 0.0
        mask: list[float] = []
        if isinstance(rhs, int):
            if rhs < len(self.values):
                final += self.values[rhs]
            return final
        elif len(rhs) == len(self.values):
            while i < len(self.values):
                if rhs[i] == True:
                    mask.append(self.values[i])
                i += 1
            return Simpy(mask)
        return self


    


            



        






        
            
       

            












# TODO: Your constructor and methods will go here.