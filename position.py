import pyautogui
import keyboard
import time

positions = []  # List to store positions

print("Press the 'Enter' key to record the mouse position. Press 'ESC' to quit.")

def record_position(event):
    x, y = pyautogui.position()
    position = (x, y)
    positions.append(position)
    print(f"Position recorded: {position}")

keyboard.on_press_key("enter", record_position)

try:
    # Run until 'ESC' is pressed.
    keyboard.wait('esc')
except KeyboardInterrupt:
    pass
finally:
    print("\nRecorded positions:")
    print(positions)
    print("Done.")
