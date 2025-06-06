import os
import sys
import time

# RGB devil-themed color cycling (returns ANSI escape code string)
def rgb_devils_colors(delay=0.05, cycles=3):
    # Devil theme: red to dark red shades cycling
    base_r, base_g, base_b = 255, 0, 0
    for cycle in range(cycles):
        for i in range(0, 255, 15):
            r = 255
            g = 0
            b = 0 + i // 3
            yield f"\033[38;2;{r};{g};{b}m"
            time.sleep(delay)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.04):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()