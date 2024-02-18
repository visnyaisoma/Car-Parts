from pynput.keyboard import Key, Listener

# Load car parts from the text file
with open("carparts.txt", "r") as file:
    car_parts = [line.strip().lower() for line in file]

# Initialize variables
pressed_keys = [] 
continuous = False

# Function to handle key press events
def on_press(key):
    global continuous
    
    # Check if the key pressed is not the escape key and key presses are not continuous
    if key != Key.esc and not continuous:
        print("{0} pressed".format(key))
        
        # Append the pressed key to the list of pressed keys
        pressed_keys.append(key)
        continuous = True


# Function to handle key release events
def on_release(key):
    global continuous
    print("{0} release".format(key))
    continuous = False
    if key == Key.esc:
        process_pressed_keys()
        return False

# Function to process the sequence of pressed keys and recognize car parts
def process_pressed_keys():
    global pressed_keys
    input_word = ''.join(str(key.char).lower() for key in pressed_keys if hasattr(key, 'char'))
    
    # Initialize variable to store the longest matched car part
    longest_match = "" 
    
    for part in car_parts:
        if part.replace(" ", "") in input_word and len(part) > len(longest_match):
            longest_match = part
    
    # Print the result based on the longest matched car part
    if longest_match:
        print("Longest recognized part:", longest_match)
    elif not pressed_keys:
        print("Empty! Please type something!")
    else:
        print("No matching part found! Try another one!")    
    
    # Clear the list of pressed keys
    pressed_keys.clear()

# Set up keyboard listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()