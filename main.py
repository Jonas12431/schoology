import tkinter as tk
import random
import time

# Track attempts to click "No"
attempts = 0
start_time = 0

def move_button(event):
    """Move the 'No' button when the cursor gets close to it"""
    global attempts
    attempts += 1
    
    # Get window dimensions
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    
    # Safety check - if window isn't fully initialized yet
    if window_width < 100 or window_height < 100:
        window_width = 400
        window_height = 300
    
    # Button dimensions
    button_width = no_button.winfo_width()
    button_height = no_button.winfo_height()
    
    # Ensure minimum button size
    if button_width < 30:
        button_width = 80
    if button_height < 10:
        button_height = 30
    
    # Safe margin to keep button fully visible
    margin = 20
    
    # Calculate maximum coordinates to ensure button stays visible
    max_x = max(50, window_width - button_width - margin)
    max_y = max(50, window_height - button_height - margin)
    
    # Generate new random coordinates
    new_x = random.randint(margin, max_x)
    new_y = random.randint(margin, max_y)
    
    # Place the button at the new coordinates, relative to the window
    no_button.place(x=new_x, y=new_y)
    
    # Update attempt counter and message
    if attempts <= 10:
        messages = [
            "Nice try!",
            "Too slow!",
            "Not even close!",
            "Missed again!",
            "You can't catch me!",
            "Haha, missed me!",
            "Keep trying!",
            "Almost got it... NOT!",
            "You're getting frustrated, aren't you?",
            "Just click 'Yes' already!"
        ]
        attempt_label.config(text=f"{messages[attempts-1]}\nAttempts: {attempts}")
    else:
        attempt_label.config(text=f"Wow, you're persistent!\nAttempts: {attempts}")
    
    # Change window background color randomly for added fun
    if attempts % 3 == 0:
        colors = ["#FFD1DC", "#CAE1FF", "#E0FFD1", "#FFE8D1", "#E5D1FF"]
        root.config(bg=random.choice(colors))
        main_frame.config(bg=random.choice(colors))

def on_yes_click():
    """Close the window when 'Yes' is clicked"""
    global attempts, start_time
    
    # Calculate time spent
    end_time = time.time()
    duration = end_time - start_time
    
    # Create a new window with stats
    stats_window = tk.Toplevel(root)
    stats_window.title("Prank Results")
    stats_window.geometry("300x200")
    stats_window.resizable(False, False)
    
    # Add statistics
    tk.Label(stats_window, text="CONGRATULATIONS!", font=("Arial", 16, "bold")).pack(pady=10)
    tk.Label(stats_window, text="You've officially admitted you're dumb!", font=("Arial", 12)).pack(pady=5)
    tk.Label(stats_window, text=f"Attempts to deny: {attempts}", font=("Arial", 12)).pack(pady=5)
    tk.Label(stats_window, text=f"Time spent: {duration:.2f} seconds", font=("Arial", 12)).pack(pady=5)
    
    # Close button
    tk.Button(stats_window, text="Accept My Fate", font=("Arial", 12), command=lambda: [stats_window.destroy(), root.destroy()]).pack(pady=20)
    
    # Make sure the main window stays open until they close the stats window
    root.withdraw()

# Create the main window
root = tk.Tk()
root.title("Important Question")
root.geometry("500x400")
root.resizable(False, False)

# Set initial background color
root.config(bg="#F0F0F0")

# Record start time
start_time = time.time()

# Create a main frame to hold everything
main_frame = tk.Frame(root, bg="#F0F0F0")
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Create the question label with a border and shadow effect
question_frame = tk.Frame(main_frame, bg="#FFFFFF", bd=2, relief=tk.RAISED)
question_frame.pack(pady=20, padx=20, ipadx=10, ipady=10)

question_label = tk.Label(
    question_frame, 
    text="Are you Dumb?", 
    font=("Arial", 24, "bold"),
    bg="#FFFFFF"
)
question_label.pack(pady=10, padx=20)

# Create a frame for the buttons
button_frame = tk.Frame(main_frame, bg="#F0F0F0")
button_frame.pack(fill="both", expand=True, pady=20)

# Create the 'Yes' button with a nice style
yes_button = tk.Button(
    button_frame, 
    text="Yes", 
    font=("Arial", 16, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=20,
    pady=10,
    relief=tk.RAISED,
    command=on_yes_click
)
yes_button.place(x=100, y=50)

# Create the 'No' button with a nice style
no_button = tk.Button(
    root, 
    text="No", 
    font=("Arial", 16, "bold"),
    bg="#F44336",
    fg="white",
    padx=20,
    pady=10,
    relief=tk.RAISED
)
no_button.place(x=300, y=150)

# Create attempt counter and message label
attempt_label = tk.Label(
    main_frame,
    text="Try clicking 'No'... if you can!",
    font=("Arial", 12, "italic"),
    bg="#F0F0F0"
)
attempt_label.pack(side=tk.BOTTOM, pady=20)

# Bind the motion event to the 'No' button
no_button.bind("<Enter>", move_button)

# Run the application
root.mainloop() 
