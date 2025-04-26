import pyautogui
import time
import random
import winsound
import os
import tkinter as tk

tex = "WHY R U STOPPED??? "

def shake_cursor():
    print("Event: Shakin' cursor")
    end_time = time.time() + 10  # Shaking for 10 seconds
    while time.time() < end_time:
        x, y = pyautogui.position()
        offset_x = random.randint(-25, 25)
        offset_y = random.randint(-25, 25)
        pyautogui.moveTo(x + offset_x, y + offset_y, duration=0.01)
        time.sleep(0.01)

def play_error_sound():
    winsound.MessageBeep()
    print("Event: Error sound")

def type_random_text():
    print("Event: Typing random text")
    messages = ["Oops!", "What's happening?", "Glitch in the matrix!", "Why so serious?", "Is anyone there?"]
    message = random.choice(messages)
    for char in message:
        pyautogui.typewrite(char, interval=0.1)
    pyautogui.press('enter')

def random_mouse_clicks():
    print("Event: Random mouse clicks")
    screen_width, screen_height = pyautogui.size()
    for _ in range(5):
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        pyautogui.click(x, y)
        time.sleep(0.5)

def random_window_minimize():
    print("Event: Randomly minimizing windows")
    for _ in range(3):
        pyautogui.hotkey("alt", "space")  # Open the window menu
        time.sleep(0.5)
        pyautogui.press("n")  # Minimize
        time.sleep(1)

def open_and_close_calculator():
    print("Event: Opening and closing Calculator")
    pyautogui.hotkey("win", "r")
    time.sleep(0.5)
    pyautogui.typewrite("calc")
    pyautogui.press("enter")
    time.sleep(2)  # Keeps Calculator open for a short while
    pyautogui.hotkey("alt", "f4")  # Closes Calculator

def add_desktop_icon():
    print("Event: Creating dummy text files on the desktop")
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    for i in range(3):
        file_name = f"{desktop_path}\\{i}_fun.txt"
        with open(file_name, "w") as file:
            file.write("Hello from foolin2day!")
        print(f"Created {file_name}")
        time.sleep(1)

def open_random_emoticon():
    print("Event: Showing random emoticon popup")
    emoticons = ["¯\\_(ツ)_/¯", "(ಠ_ಠ)", "(╯°□°）╯︵ ┻━┻", "(づ｡◕‿‿◕｡)づ", "(ಥ﹏ಥ)"]
    pyautogui.alert(text=random.choice(emoticons), title="Emoticon Alert", button="umm...")

def block_taskbar():
    print("Rare Event: Blocking taskbar")
    root = tk.Tk()
    root.overrideredirect(1)
    root.geometry(f"{pyautogui.size().width}x50+0+{pyautogui.size().height - 50}")
    root.configure(bg='black')
    root.attributes("-topmost", True)
    root.after(5000, root.destroy)
    root.mainloop()

def random_event():
    events = [
        shake_cursor,
        play_error_sound,
        type_random_text,
        random_mouse_clicks,
        random_window_minimize,
        open_and_close_calculator,
        add_desktop_icon,
        block_taskbar,
        open_random_emoticon,
    ]
    event = random.choice(events)
    event()

def cleanup():
    print("Cleaning up created files...")
    desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    for i in range(3):
        file_name = f"{desktop_path}\\{i}_fun.txt"
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"Removed {file_name}")

def main_loop():
    try:
        while True:
            wait_time = random.randint(30, 90)  # Interval
            for remaining in range(wait_time, 0, -1):
                print(f"Next event starting in {remaining}s! ", end='\r')
                time.sleep(1)
            print(" " * 50, end='\r')  # Clear line
            random_event()  # Trigger a random event
    except KeyboardInterrupt:
        print("\nScript stopped manually.")
        cleanup()
        print(tex * 100)
        time.sleep(0.1)

main_loop()
