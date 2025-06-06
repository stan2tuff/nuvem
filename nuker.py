import requests
import time

class Nuker:
    def __init__(self, token, guild_id):
        self.token = token
        self.guild_id = guild_id
        self.headers = {
            "Authorization": f"Bot {self.token}",
            "Content-Type": "application/json"
        }
        self.api_base = "https://discord.com/api/v10"

    def get_channels(self):
        url = f"{self.api_base}/guilds/{self.guild_id}/channels"
        r = requests.get(url, headers=self.headers)
        if r.status_code == 200:
            return r.json()
        return []

    def get_roles(self):
        url = f"{self.api_base}/guilds/{self.guild_id}/roles"
        r = requests.get(url, headers=self.headers)
        if r.status_code == 200:
            return r.json()
        return []

    def get_members(self):
        url = f"{self.api_base}/guilds/{self.guild_id}/members?limit=1000"
        r = requests.get(url, headers=self.headers)
        if r.status_code == 200:
            return r.json()
        return []

    def delete_channel(self, channel_id):
        url = f"{self.api_base}/channels/{channel_id}"
        r = requests.delete(url, headers=self.headers)
        return r.status_code == 204

    def create_channel(self, name):
        url = f"{self.api_base}/guilds/{self.guild_id}/channels"
        data = {"name": name, "type": 0}
        r = requests.post(url, json=data, headers=self.headers)
        return r.status_code == 201

    def delete_role(self, role_id):
        url = f"{self.api_base}/guilds/{self.guild_id}/roles/{role_id}"
        r = requests.delete(url, headers=self.headers)
        return r.status_code == 204

    def rename_role(self, role_id, new_name):
        url = f"{self.api_base}/guilds/{self.guild_id}/roles/{role_id}"
        data = {"name": new_name}
        r = requests.patch(url, json=data, headers=self.headers)
        return r.status_code == 200

    def kick_member(self, user_id):
        url = f"{self.api_base}/guilds/{self.guild_id}/members/{user_id}"
        r = requests.delete(url, headers=self.headers)
        return r.status_code == 204

    def ban_member(self, user_id, days=7):
        url = f"{self.api_base}/guilds/{self.guild_id}/bans/{user_id}"
        data = {"delete_message_days": days}
        r = requests.put(url, json=data, headers=self.headers)
        return r.status_code == 204