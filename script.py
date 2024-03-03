import tkinter as tk
from threading import Thread
import pyautogui
import time


def click_buttons(loop_times):
    global running
    button_positions = [(297, 979), (363, 985), (1088, 297), (435, 986), (824, 440), (850, 778), (845, 954), (940, 599)]
    delays = [1, 2, 2, 30, 4, 2, 2, 2]

    def sleep_with_break(delay, move_cursor=False):
        original_position = pyautogui.position()  # Save original cursor position
        if move_cursor:
            # Move cursor to the "Stop" button's position only if specified
            pyautogui.moveTo(125, 940)

        for _ in range(int(delay * 10)):  # Break the delay into smaller pieces
            if not running:
                break
            time.sleep(0.1)  # Sleep for a tenth of a second at a time

        if move_cursor:
            # Move the cursor back to its original position
            pyautogui.moveTo(original_position)

    for _ in range(loop_times):
        if not running:
            break
        for position, delay in zip(button_positions, delays):
            if not running:
                break
            # Check if the delay is 30 seconds and move cursor if true
            move_cursor = delay == 30
            sleep_with_break(delay, move_cursor=move_cursor)
            if not running:
                break
            pyautogui.click(position)
            print(f"Clicked button at {position} after waiting {delay} seconds.")



def start_clicking():
    global running
    running = True
    try:
        loop_times = int(loop_entry.get()) 
    except ValueError:
        print("Please enter a valid integer for the loop count.")
        running = False
        return
    t = Thread(target=click_buttons, args=(loop_times,))
    t.start()

# Stop the button clicking process
def stop_clicking():
    global running
    running = False

# GUI setup
app = tk.Tk()
app.title("Button Clicker")
app.attributes("-topmost", True)  # Make the window always on top

# Assuming the new width is 200 pixels and the height is 200 pixels
# and positioning it at (20, 750)
app.geometry("200x200+20+750")

running = False  # Global flag to control execution

# Entry for loop count
loop_label = tk.Label(app, text="Enter loop count:")
loop_label.pack(pady=(20,0))
loop_entry = tk.Entry(app)
loop_entry.pack(pady=10)
loop_entry.insert(0, "100")  # Default value

# Start button
start_button = tk.Button(app, text="Start", command=start_clicking)
start_button.pack(pady=10)

# Stop button
stop_button = tk.Button(app, text="Stop", command=stop_clicking)
stop_button.pack(pady=20)

app.mainloop()
