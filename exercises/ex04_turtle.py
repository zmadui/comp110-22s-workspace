"""EX04: A Beautiful House with the circular door!"""

__author__ = "730329470"

from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """This is where my scene commences."""
    steven: Turtle = Turtle()
    base(steven, 200, 90, 170)
    window(steven, 65, 100)
    window(steven, 165, 100)
    chimney(steven, 160, 180)
    roof(steven, 200, 120, 200)
    door(steven, 125, 60)
    doorhandle(steven, 125, 45)
    done()


def base(steven: Turtle, x: float, y: float, z: float) -> None: 
    """Drawing the base of the house."""
    i: int = 0 
    while (i < 2):
        steven.forward(x)
        steven.left(y)
        steven.forward(z)
        steven.left(y)
        i += 1
      
    
def roof(steven: Turtle, x: float, y: float, z: float) -> None:
    """Drawing the roof of the house."""
    i: int = 0
    steven.penup()
    steven.goto(0, 170)
    steven.pendown()
    steven.pencolor("purple")
    while (i < 2):
        steven.begin_fill()
        steven.fillcolor("purple")
        steven.forward(x)
        steven.left(y)
        steven.forward(z)
        steven.left(y)
        steven.end_fill()
        i += 1

        
def window(steven: Turtle, x: float, y: float) -> None:
    """Drawing windows for the house."""
    i: int = 0
    steven.penup()
    steven.goto(x, y)
    steven.pendown()
    steven.pencolor(99, 204, 250)
    steven.begin_fill()
    steven.fillcolor(99, 204, 250)
    while (i < 2):
        steven.left(90)
        steven.forward(60)
        steven.left(90)
        steven.forward(30)
        i += 1
    steven.end_fill()
    

def chimney(steven: Turtle, x: float, y: float) -> None:
    """Drawing a chimney on the house."""
    i: int = 0
    steven.penup()
    steven.pencolor("grey")
    steven.goto(180, 230)
    steven.goto(x, y)
    steven.pendown()
    steven.begin_fill()
    while (i < 2):
        steven.fillcolor("grey")
        steven.forward(30)
        steven.left(90)
        steven.forward(60)
        steven.left(90)
        i += 1
    steven.end_fill()


def door(steven: Turtle, x: float, y: float) -> None:
    """Drawing a circular door."""
    steven.penup()
    steven.pencolor("pink")
    steven.goto(x, y)
    steven.pendown()
    steven.begin_fill()
    steven.fillcolor("pink")
    steven.circle(30)
    steven.end_fill()


def doorhandle(steven: Turtle, x: float, y: float) -> None:
    """Drawing the handle of the door."""
    steven.penup()
    steven.pencolor("purple")
    steven.goto(x, y)
    steven.pendown()
    steven.begin_fill()
    steven.fillcolor("purple")
    steven.circle(5)
    steven.end_fill()


if __name__ == "__main__": 
    main() 