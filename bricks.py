from turtle import Turtle
import random

# List of available colors for the bricks.
COLOR_LIST = [
    'light blue', 'royal blue', 'light steel blue', 'steel blue',
    'light cyan', 'light sky blue', 'violet', 'salmon', 'tomato',
    'sandy brown', 'purple', 'deep pink', 'medium sea green', 'khaki'
]

# List of weights used for random selection of brick 'quantity' values.
weights = [1, 2, 1, 1, 3, 2, 1, 4, 1, 3, 1, 1, 1, 4, 1, 3, 2, 2, 1, 2, 1, 2, 1, 2, 1]


class Brick(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()  # Initialize the superclass (Turtle).
        self.penup()  # Disable drawing when moving.
        self.shape('square')  # Set the turtle's shape to a square.
        self.shapesize(stretch_wid=1.5, stretch_len=3)  # Stretch the square into a rectangle.
        self.color(random.choice(COLOR_LIST))  # Set a random color from the color list.
        self.goto(x=x_cor, y=y_cor)  # Position the brick at the specified coordinates.

        self.quantity = random.choice(weights)  # Assign a random 'quantity' from weights list.

        # Calculate and store the brick's edge coordinates for use in collision detection.
        self.left_wall = self.xcor() - 30  # Left boundary of the brick.
        self.right_wall = self.xcor() + 30  # Right boundary of the brick.
        self.upper_wall = self.ycor() + 15  # Top boundary of the brick.
        self.bottom_wall = self.ycor() - 15  # Bottom boundary of the brick.


class Bricks:
    def __init__(self):
        self.y_start = 0  # Starting y-coordinate for brick placement.
        self.y_end = 240  # Ending y-coordinate for brick placement.
        self.bricks = []  # List to store all brick instances.
        self.create_all_lanes()  # Initialize all lanes of bricks.

    def create_lane(self, y_cor):
        """
        Create a lane of bricks at a given y-coordinate.
        Bricks are positioned from x = -570 to x = 570, spaced 63 units apart.
        """
        for i in range(-570, 570, 63):
            brick = Brick(i, y_cor)  # Create a new brick at specified coordinates.
            self.bricks.append(brick)  # Append the new brick to the bricks list.

    def create_all_lanes(self):
        """
        Create multiple lanes of bricks using a vertical offset of 32 units between each lane,
        from y_start to y_end.
        """
        for i in range(self.y_start, self.y_end, 32):
            self.create_lane(i)  # Call create_lane for each vertical offset.
