from ursina import *
import subprocess  # Used to run another Python file (game.py)

app = Ursina()

# Function to start the game by running the game.py script
def start_game():
    print("Starting the game...")
    # Run the game.py script using subprocess
    subprocess.Popen(['python3', 'main.py'])  # Ensure you're running the correct game script

# Create the Start Game button
start_button = Button(
    text="Start TOP GUN FlightSim",  # Button text
    color=color.green,              # Button color
    scale = (0.02,0.02),
    position = (0, 0),             # Button position on the screen
    font_size = 0.01,
    on_click=start_game             # Call start_game function on click
)

button_background = Entity(
    model='quad',                 # 2D plane to act as the button background
    color=color.green,        # Background color (you can choose any color)
    scale=(0.02, 0.02),            # Size of the background (slightly bigger than the button)
    position=(0, 0.1),            # Position it where the button will be
    z=-1                          # Make sure it's behind the button
)


app.run()  # Start the Ursina application and show the button
