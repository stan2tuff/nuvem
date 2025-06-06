import os
import sys
import time

# Clear screen cross-platform
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Simple RGB cycle in terminal for a text
def rgb_print(text, delay=0.1):
    colors = ['\033[91m', '\033[93m', '\033[92m', '\033[96m', '\033[94m', '\033[95m']
    for c in colors:
        print(c + text + '\033[0m', end='\r')
        time.sleep(delay)
    print('\033[0m', end='')

# Rocket animation
def rocket_animation():
    rocket_frames = [
        "    🚀    ",
        "   🚀     ",
        "  🚀      ",
        " 🚀       ",
        "🚀        ",
    ]
    for _ in range(5):
        for frame in rocket_frames:
            clear()
            print(frame)
            time.sleep(0.1)
    clear()

# Print with rgb cycling for menu header
def print_rgb_header(text):
    colors = ['\033[91m', '\033[93m', '\033[92m', '\033[96m', '\033[94m', '\033[95m']
    for c in colors:
        print(c + text + '\033[0m')
        time.sleep(0.004)