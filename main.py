# Import necessary modules and classes for the game
import turtle as tr
from paddle import Paddle  # Custom Paddle class
from ball import Ball  # Custom Ball class
from scoreboard import Scoreboard  # Custom Scoreboard class
from ui import UI  # Custom UI class for the game interface
from bricks import Bricks  # Custom Bricks class
import time  # Time module for handling game timing

# Setup the main screen using the turtle module
screen = tr.Screen()  # Create a screen object
screen.setup(width=1200, height=600)  # Set up the screen dimensions
screen.bgcolor('black')  # Set the background color to black
screen.title('Breakout')  # Set the window title to 'Breakout'
screen.tracer(0)  # Turn off automatic animation to manually control updates

# Make the window non-resizable
screen.cv._rootwindow.resizable(False, False)  # Disable both horizontal and vertical resizing

# Initialize user interface elements
ui = UI()  # Create an instance of the UI class
ui.header()  # Display the header or title of the gam

# Initialize the scoreboard with 5 lives
score = Scoreboard(lives=5)  # Create a scoreboard object with 5 initial lives

# Initialize the paddle
paddle = Paddle()  # Create an instance of the Paddle class

# Initialize the bricks
bricks = Bricks()  # Create an instance of the Bricks class

# Create the ball object
ball = Ball()  # Create an instance of the Ball class

# Game control flags
game_paused = False  # Flag to track if the game is paused
playing_game = True  # Flag to track if the game is still running


def pause_game():
    """Toggle the pause state of the game."""
    global game_paused  # Use the global game_paused variable
    game_paused = not game_paused  # Toggle the pause state


# Keyboard bindings
screen.listen()  # Listen for keyboard inputs
screen.onkey(key='Left', fun=paddle.move_left)  # Move paddle left on 'Left' key press
screen.onkey(key='Right', fun=paddle.move_right)  # Move paddle right on 'Right' key press
screen.onkey(key='space', fun=pause_game)  # Pause or unpause the game on 'space' key press


def check_collision_with_walls():
    """Check and handle collisions between the ball and the game window borders."""
    global ball, score, playing_game, ui

    # Collision with left and right walls
    if ball.xcor() < -580 or ball.xcor() > 570:  # If the ball hits the side walls
        ball.bounce(x_bounce=True, y_bounce=False)  # Bounce the ball horizontally

    # Collision with the top wall
    if ball.ycor() > 270:  # If the ball hits the top wall
        ball.bounce(x_bounce=False, y_bounce=True)  # Bounce the ball vertically

    # Collision with the bottom wall (loss condition)
    if ball.ycor() < -280:  # If the ball falls below the bottom of the screen
        ball.reset()  # Reset the ball to the initial position
        score.decrease_lives()  # Decrease the player's lives by one
        if score.lives == 0:  # Check if there are no more lives
            score.reset()  # Reset the score
            playing_game = False  # End the game loop
            ui.game_over(win=False)  # Display the game over message
        ui.change_color()  # Change the color of the UI elements


def check_collision_with_paddle():
    """Check and handle collisions between the ball and the paddle."""
    global ball, paddle

    # Calculate relative positions
    paddle_x = paddle.xcor()  # Get the paddle's x-coordinate
    ball_x = ball.xcor()  # Get the ball's x-coordinate

    # Collision detection logic
    if ball.distance(paddle) < 110 and ball.ycor() < -250:  # If the ball is near the paddle
        if (paddle_x > 0 and ball_x > paddle_x) or (paddle_x < 0 and ball_x < paddle_x):  # Check collision sides
            ball.bounce(x_bounce=True, y_bounce=True)  # Bounce ball diagonally
        else:
            ball.bounce(x_bounce=False, y_bounce=True)  # Bounce ball vertically


def check_collision_with_bricks():
    """Check and handle collisions between the ball and the bricks."""
    global ball, score, bricks

    for brick in bricks.bricks:  # Iterate through each brick
        if ball.distance(brick) < 40:  # If the ball collides with a brick
            score.increase_score()  # Increase the player's score
            brick.quantity -= 1  # Decrease the brick's hit points
            if brick.quantity == 0:  # If the brick is destroyed
                brick.clear()  # Clear the brick from the screen
                brick.goto(3000, 3000)  # Move the brick off-screen
                bricks.bricks.remove(brick)  # Remove the brick from the list

            # Collision side detection
            if ball.xcor() < brick.left_wall or ball.xcor() > brick.right_wall:  # Check horizontal collision
                ball.bounce(x_bounce=True, y_bounce=False)  # Bounce ball horizontally
            elif ball.ycor() < brick.bottom_wall or ball.ycor() > brick.upper_wall:  # Check vertical collision
                ball.bounce(x_bounce=False, y_bounce=True)  # Bounce ball vertically


# Game loop
while playing_game:  # Main game loop runs while the game is active
    if not game_paused:  # Only update the game if it's not paused
        screen.update()  # Refresh the screen
        time.sleep(0.01)  # Short delay to control the game speed
        ball.move()  # Move the ball

        # Collision detection
        check_collision_with_walls()  # Check for wall collisions
        check_collision_with_paddle()  # Check for paddle collisions
        check_collision_with_bricks()  # Check for brick collisions

        # Victory condition
        if len(bricks.bricks) == 0:  # If all bricks are destroyed
            ui.game_over(win=True)  # Display the win message
            break  # Exit the game loop
    else:
        ui.paused_status()  # Display paused status when the game is paused

tr.mainloop()  # Start the turtle main loop to keep the window open
