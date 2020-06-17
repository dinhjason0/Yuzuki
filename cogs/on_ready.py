from discord.ext import commands
import discord
#Good Morning, Yuzuki

class on_ready(commands.Cog):
    def __init__(self, client):
        self.client = client

        @client.event
        async def on_ready():
            print(f'{client.user.name} Is Awake')

            client.loop.create_task(change_status())

        # Uptime Clock
        async def change_status():
            # The "currently playing" message on Yuzuki
            await client.change_presence(activity=discord.Game(f"This message is pissing me off"))

def setup(client):
    client.add_cog(on_ready(client))