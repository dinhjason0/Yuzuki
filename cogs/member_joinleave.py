from discord.ext import commands
#Member Join

class member_joinleave(commands.Cog):
    def __init__(self, client):
        self.client = client

        # Member Join
        @client.event
        async def on_member_join(member):
            print(f"{member}, what a mistake they made.")
            await member.send("Welcome, this is a closed invite server. Use .start to begin")

        # Member Leave
        @client.event
        async def on_member_remove(member):
            print(f"{member} has left.")

def setup(client):
    client.add_cog(member_joinleave(client))