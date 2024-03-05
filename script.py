import tkinter as tk
from threading import Thread
import pyautogui
import time

def click_buttons(loop_times, custom_delay):
    global running
    button_positions = [(297, 979), (363, 985), (1088, 297), (435, 986), (824, 440), (850, 778), (845, 954), (940, 599)]
    delays = [1, 2, 2, custom_delay, 4, 2, 2, 2]  

    def sleep_with_break(delay, move_cursor=False):
        if move_cursor:
            original_position = pyautogui.position()
        
        for _ in range(int(delay * 10)):
            if not running:
                break
            time.sleep(0.1)
            if move_cursor and _ == 0:
                pyautogui.moveTo(125, 940)

        if move_cursor:
            pyautogui.moveTo(original_position)

    for _ in range(loop_times):
        if not running:
            break
        for position, delay in zip(button_positions, delays):
            if not running:
                break
            move_cursor = delay == custom_delay  
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
        custom_delay = float(custom_delay_entry.get())  
    except ValueError:
        print("Please enter valid integers for the loop count and delay.")
        running = False
        return
    t = Thread(target=click_buttons, args=(loop_times, custom_delay))
    t.start()

def stop_clicking():
    global running
    running = False

# GUI setup
app = tk.Tk()
app.title("Button Clicker")
app.attributes("-topmost", True)
app.geometry("200x300+20+650") 

running = False

# Entry for loop count
loop_label = tk.Label(app, text="Enter loop count:")
loop_label.pack(pady=(20,0))
loop_entry = tk.Entry(app)
loop_entry.pack(pady=10)
loop_entry.insert(0, "100")

# Entry for custom delay
custom_delay_label = tk.Label(app, text="Enter custom delay (s):")
custom_delay_label.pack(pady=(5,0))
custom_delay_entry = tk.Entry(app)
custom_delay_entry.pack(pady=10)
custom_delay_entry.insert(0, "30")  

# Start button with increased size
start_button = tk.Button(app, text="Start", command=start_clicking, height=2, width=15, font=('Helvetica', '12'))
start_button.pack(pady=10)

# Stop button with increased size
stop_button = tk.Button(app, text="Stop", command=stop_clicking, height=4, width=15, font=('Helvetica', '12'))
stop_button.pack(pady=10)

app.mainloop()
