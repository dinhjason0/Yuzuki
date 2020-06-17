from discord.ext import commands
#Ping Measurement

class ping(commands.Cog):
    def __init__(self, client):
        self.client = client

        # Ping measurement
        @client.command(name='ping')
        async def ping(dtx):
            await dtx.send(f"Your ping is {round(client.latency * 1000)}ms")


def setup(client):
    client.add_cog(ping(client))