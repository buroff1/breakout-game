import time
from turtle import Turtle
import random

# Define constants for fonts and alignment used in the UI
FONT = ("Courier", 52, "normal")  # Large font for main titles
FONT2 = ("Courier", 32, "normal")  # Smaller font for other texts
ALIGNMENT = 'center'  # Common alignment for text
COLOR = "white"  # Default color for text
# List of colors used to randomize UI elements
COLOR_LIST = [
    'light blue', 'royal blue', 'light steel blue', 'steel blue',
    'light cyan', 'light sky blue', 'violet', 'salmon', 'tomato',
    'sandy brown', 'purple', 'deep pink', 'medium sea green', 'khaki'
]


class UI(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the superclass Turtle
        self.hideturtle()  # Make the turtle invisible as it's used only for text display
        self.penup()  # Prevent drawing lines when moving
        self.color(random.choice(COLOR_LIST))  # Randomly choose a color from the list
        self.header()  # Display the header on initialization

    def header(self):
        """Display the main game title and instructions."""
        self.clear()  # Clear any existing text
        self.goto(x=0, y=-150)  # Position for the game title
        self.write('Breakout', align=ALIGNMENT, font=FONT)  # Write the game title
        self.goto(x=0, y=-180)  # Position for the game instructions
        self.write('Press Space to PAUSE or RESUME the Game',
                   align=ALIGNMENT, font=('Calibri', 14, 'normal'))  # Instruction text

    def change_color(self):
        """Change the color of the UI text to a random color and refresh the header."""
        self.clear()  # Clear existing text
        self.color(random.choice(COLOR_LIST))  # Select a new random color
        self.header()  # Redisplay the header with the new color

    def paused_status(self):
        """Display the paused status with a blinking effect."""
        self.clear()  # Clear existing text
        self.change_color()  # Change the color for the paused status
        time.sleep(0.5)  # Pause for a moment to create a blinking effect

    def game_over(self, win):
        """Display a game over message depending on whether the player won or lost."""
        self.clear()  # Clear any existing text
        if win:
            self.write('You Won', align='center', font=FONT)  # Winning message
        else:
            self.write("Game Over", align='center', font=FONT)  # Losing message
