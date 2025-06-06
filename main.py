import time
import sys
from nuker import Nuker
from utils import clear, slow_print, rgb_devils_colors

VERSION = "0.004"
NAME = "NUVEM"

def print_header():
    clear()
    # RGB devil colors cycling
    colors = rgb_devils_colors(delay=0.03, cycles=1)
    try:
        for _ in range(3):
            color = next(colors)
            print(color + f"=== {NAME} DEVIL MENU v{VERSION} ===\033[0m")
            time.sleep(0.3)
            clear()
    except StopIteration:
        pass
    print(f"\033[31m=== {NAME} DEVIL MENU v{VERSION} ===\033[0m\n")

def select_server_menu(servers):
    while True:
        clear()
        print_header()
        if not servers:
            print("No servers found for this bot token.")
            return None
        print("Select a server to nuke:\n")
        for idx, server in enumerate(servers, start=1):
            print(f"{idx}. {server['name']} (ID: {server['id']})")
        print("0. Exit")
        choice = input("\nEnter choice: ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                return None
            elif 1 <= choice <= len(servers):
                return servers[choice - 1]['id']
        print("Invalid choice, try again.")
        time.sleep(1)

def main():
    clear()
    print_header()
    token = input("Enter your Bot Token: ").strip()
    nuker = Nuker(token)

    servers = nuker.get_servers()
    guild_id = select_server_menu(servers)
    if guild_id is None:
        print("Exiting...")
        return

    clear()
    slow_print("Preparing to nuke selected server...", delay=0.03)
    nuker.nuke(guild_id)
    print("\nAll done! Thanks for using NUVEM.")

if __name__ == "__main__":
    main()