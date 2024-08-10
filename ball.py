from turtle import Turtle

# Constant for the distance the ball moves in each step.
MOVE_DIST = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the superclass (Turtle).
        self.shape('circle')  # Set the shape of the turtle object to a circle.
        self.color('white')  # Set the color of the turtle object to white.
        self.penup()  # Lift the pen so that it doesn’t draw lines when it moves.
        self.x_move_dist = MOVE_DIST  # Horizontal movement distance per move call.
        self.y_move_dist = MOVE_DIST  # Vertical movement distance per move call.
        self.reset()  # Position the ball to its starting position on creation.

    def move(self):
        """Move the ball in the screen by updating its position based on predefined distances."""
        new_y = self.ycor() + self.y_move_dist  # Compute new y-coordinate.
        new_x = self.xcor() + self.x_move_dist  # Compute new x-coordinate.
        self.goto(new_x, new_y)  # Move the ball to the new coordinates.

    def bounce(self, x_bounce, y_bounce):
        """
        Reverse the ball's direction based on collision detection flags.

        Args:
            x_bounce (bool): If True, reverse horizontal direction.
            y_bounce (bool): If True, reverse vertical direction.
        """
        if x_bounce:
            self.x_move_dist *= -1  # Reverse horizontal movement direction.

        if y_bounce:
            self.y_move_dist *= -1  # Reverse vertical movement direction.

    def reset(self):
        """Reset the ball's position to the starting point and set initial vertical movement."""
        self.goto(x=0, y=-240)  # Move the ball to the starting position.
        self.y_move_dist = MOVE_DIST  # Set initial vertical movement speed to a constant.
