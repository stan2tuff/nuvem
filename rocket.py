import time
import sys

rocket_frames = [
    "   /\  ",
    "  /  \ ",
    " /++++\\",
    "|      |",
    "| NUVEM|",
    "|------|",
    "  |  |  ",
    "  |  |  ",
]

def rocket_launch_animation():
    for i in range(10):
        print("\n" * (10 - i))
        for line in rocket_frames:
            print(line)
        time.sleep(0.15)
        if i != 9:
            # Clear the lines to simulate animation frame
            sys.stdout.write("\033[F" * (len(rocket_frames) + 10))