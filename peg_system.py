import tkinter as tk
from PIL import Image, ImageTk, ImageOps 
import random
import tkinter.ttk as ttk


# Define the 00-99 peg system 
peg_system = {
    0: "Zeus", 1: "Seed/Soda", 2: "Sun", 3: "Sumo", 4: "Cerro",
    5: "Silo", 6: "Sage", 7: "Sack", 8: "Safe/Sofa", 9: "Soap",
    10: "Dice", 11: "Tit", 12: "Tin", 13: "Tomb", 14: "Tire",
    15: "Tail/Tile", 16: "Dish", 17: "Duck/Dog/Tag", 18: "Dove", 19: "Tub",
    20: "Nose", 21: "Net", 22: "Nun", 23: "Nemo/Gnome", 24: "Nero",
    25: "Nail", 26: "Nacho", 27: "Necklace", 28: "Knife", 29: "Knob",
    30: "Mouse", 31: "Mat", 32: "Moon", 33: "Mummy", 34: "Mare",
    35: "Mill", 36: "Match", 37: "Mug", 38: "Movie", 39: "Map/Mop",
    40: "Rose/Rice/Arroz", 41: "Rod", 42: "Rain", 43: "Ram", 44: "Rower",
    45: "Rail", 46: "Roach", 47: "Rock", 48: "Roof", 49: "Rope",
    50: "Lizard", 51: "Light", 52: "Lion", 53: "Lamb", 54: "Lure",
    55: "Lily", 56: "Leech", 57: "Log", 58: "Leaf", 59: "Lip",
    60: "Chess", 61: "Jet", 62: "Chain", 63: "Jam", 64: "Chair",
    65: "Gel/Jail", 66: "Judge", 67: "Chalk", 68: "Chef", 69: "Ship",
    70: "Case", 71: "Cat/Kite", 72: "Can", 73: "Gum", 74: "Car",
    75: "Coal", 76: "Cage", 77: "Cake", 78: "Cave", 79: "Cup",
    80: "Vase", 81: "Foot", 82: "Phone", 83: "Fame/Foam", 84: "Fire",
    85: "Fly/File", 86: "Fish", 87: "Fork", 88: "Fifa", 89: "Vape",
    90: "Bus", 91: "Bat", 92: "Bone", 93: "Bomb", 94: "Bear",
    95: "Bell", 96: "Peach", 97: "Book", 98: "Beef", 99: "Pope"
}



# Function to load images
def load_images():
    images = {}
    for number in range(100):
        # handling numbers without image with try/except
        try:
            img = Image.open(f"images/{number:02d}.webp")
            img = img.resize((350, 350))  
            img_with_border = ImageOps.expand(img, border=5, fill='black') 
            images[number] = ImageTk.PhotoImage(img_with_border)
        except FileNotFoundError:
            images[number] = None  
    return images


def toggle_visibility():
    toggle_state.set(not toggle_state.get())
    update_display(current_number)

# Function to update the display with number/name pair
def update_display(number):
    name = peg_system.get(number, "Unknown")
    
    if toggle_state.get():
        display_var.set(f"{number:02d}\n{name}")
        if images[number]:
            image_label.config(image=images[number])
        else:
            image_label.config(image='')
    else:
        display_var.set(f"{number:02d}")
        image_label.config(image='')

        
def display_selected():
    # Get the selected word from the combobox
    selected_item = dropdown.get()
    selected_word = selected_item.split()[1]
    global current_number
    # Find the corresponding number in the peg system
    for number, word in peg_system.items():
        current_number = number
        if word.lower() == selected_word.lower():
            update_display(number)
            break


# Function to display the next number in the sequence
def next_number():
    global current_number
    current_number = (current_number + 1) % 100
    update_display(current_number)

# Function to display the previous number in the sequence
def previous_number():
    global current_number
    current_number = (current_number - 1) % 100
    update_display(current_number)

# Function to display a random number
def random_number():
    global current_number
    current_number = random.randint(0, 99)
    update_display(current_number)


# Initialize Tkinter window
root = tk.Tk()
root.title("00-99 Peg System")
root.geometry("600x600")

# Initialize the toggle state variable
toggle_state = tk.BooleanVar(value=True)  # Start with images and names visible


# Bind the left and right arrow keys to the previous and next functions
root.bind("<Left>", lambda event: previous_number())
root.bind("<Right>", lambda event: next_number())
# Bind the space bar to the toggle function
root.bind("<Shift_L>", lambda event: toggle_visibility())
root.bind("<Control_L>", lambda event: random_number())



# Load the images
images = load_images()

# Variable to hold the current number
current_number = 0

# Create a variable to hold the displayed text
display_var = tk.StringVar()
display_label = tk.Label(root, textvariable=display_var, font=("Arial", 24))
display_label.pack(pady=20)

# Create an image label to display the corresponding image
image_label = tk.Label(root)
image_label.pack(pady=5)


dropdown = ttk.Combobox(root, values=list(peg_system.items()), state="readonly")
dropdown.place(x=10, y=10)

dropdown.bind("<<ComboboxSelected>>", lambda event: display_selected())

toggle_button = tk.Button(root, text="Toggle Images and Names", command=toggle_visibility)
toggle_button.pack(pady=10)


# Create the navigation bar with two buttons
nav_frame = tk.Frame(root)
nav_frame.pack(pady=10)


# Create the "Previous", "Next" and "Random" buttons
nav_buttons_frame = tk.Frame(root)
nav_buttons_frame.pack(side=tk.BOTTOM, pady=10)

previous_button = tk.Button(nav_buttons_frame, text="Previous", command=previous_number)
previous_button.pack(side=tk.LEFT, padx=20)

next_button = tk.Button(nav_buttons_frame, text="Next", command=next_number)
next_button.pack(side=tk.LEFT, padx=20)

random_button = tk.Button(nav_buttons_frame, text="Random", command=random_number)
random_button.pack(side=tk.LEFT, padx=20)

# Set the initial display
update_display(current_number)

# Start with images and names visible



# Start the Tkinter event loop
root.mainloop()
