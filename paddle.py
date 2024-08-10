from turtle import Turtle

# Define a constant for the movement distance of the paddle.
MOVE_DIST = 70


class Paddle(Turtle):
    def __init__(self):
        super().__init__()  # Call the initializer of the superclass, Turtle.
        self.color('steel blue')  # Set the color of the paddle.
        self.shape('square')  # Set the shape of the turtle object to a square.
        self.penup()  # Lift the turtle’s pen up to prevent it from drawing lines when it moves.
        self.shapesize(stretch_wid=1, stretch_len=10)  # Stretch the turtle to create a paddle shape.
        self.goto(x=0, y=-280)  # Position the paddle at specified coordinates on the screen.

    def move_left(self):
        """
        Move the paddle left by a set distance.
        This method moves the paddle backward by the distance defined in MOVE_DIST.
        """
        self.backward(MOVE_DIST)  # Move the paddle backward by MOVE_DIST units.

    def move_right(self):
        """
        Move the paddle right by a set distance.
        This method moves the paddle forward by the distance defined in MOVE_DIST.
        """
        self.forward(MOVE_DIST)  # Move the paddle forward by MOVE_DIST units.
