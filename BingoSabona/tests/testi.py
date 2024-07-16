import subprocess
import os
import sys
import time

# Function to run the server
def run_server():
    print("Starting server...")
    subprocess.Popen([sys.executable, "server12.py"], cwd=os.getcwd())

# Function to run the game
def run_game():
    print("Starting game...")
    subprocess.Popen([sys.executable, "Interface_game.py"], cwd=os.getcwd())

# Main function
if __name__ == "__main__":
    try:
        # Start the server
        run_server()
        # Wait for some time tccco ensure the server starts before running the game
        time.sleep(1)
        # Start the game
        run_game()
    except Exception as e:
        print("Error:", e)
