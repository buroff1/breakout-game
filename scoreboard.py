from turtle import Turtle

# Attempt to read the highest score from a file, or initialize it if not present.
try:
    # Try to read the existing high score from a file.
    score = int(open('highestScore.txt', 'r').read())
except FileNotFoundError:
    # If the file doesn't exist, create it and initialize the high score to 0.
    open('highestScore.txt', 'w').write('0')
    score = 0
except ValueError:
    # Handle cases where the file is corrupted and does not contain an integer.
    score = 0

# Define the default font for the scoreboard.
FONT = ('arial', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self, lives):
        super().__init__()  # Initialize the Turtle superclass.
        self.color('white')  # Set the scoreboard's color.
        self.penup()  # Lift the pen to avoid drawing lines when moving.
        self.hideturtle()  # Make the turtle invisible.
        self.highScore = score  # Set the high score from the file or initialized value.
        self.goto(x=-580, y=260)  # Position the scoreboard on the screen.
        self.lives = lives  # Initialize the lives.
        self.score = 0  # Start the current score at 0.
        self.update_score()  # Display the initial score.

    def update_score(self):
        """Clears the current score display and writes the new score."""
        self.clear()  # Clear the previous score text.
        self.write(f"Score: {self.score} | Highest Score: {self.highScore} | Lives: {self.lives}",
                   align='left', font=FONT)  # Display the current score and lives.

    def increase_score(self):
        """Increases the score by 1 and updates the display; also updates the high score if necessary."""
        self.score += 1  # Increment the current score.
        if self.score > self.highScore:
            self.highScore = self.score  # Update the high score if the current score is greater.
        self.update_score()  # Refresh the scoreboard display.

    def decrease_lives(self):
        """Decreases the number of lives by 1 and updates the scoreboard."""
        self.lives -= 1  # Decrement the lives.
        self.update_score()  # Update the display to reflect the change.

    def reset(self):
        """Resets the current score to 0 at the end of the game and saves the high score."""
        self.score = 0  # Reset the current score to 0.
        self.update_score()  # Update the display.
        open('highestScore.txt', 'w').write(str(self.highScore))  # Save the new high score to the file.
