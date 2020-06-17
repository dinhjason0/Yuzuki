from discord.ext import commands
import discord
from heroes import Hero
import pandas as pd
#LINK START: If user has 'player' role, disable them from having permission to use this command again

class start(commands.Cog):
    def __init__(self, client):
        self.client = client

        @client.command(name='start')
        async def start(ctx):
            role = discord.utils.get(ctx.guild.roles, name='Player')
            if role not in ctx.author.roles:
                await ctx.author.send("Thank you for starting. Lets begin.")
                await ctx.send(
                    f"Link connection has been established. Say hello to your new room {ctx.author.display_name}")
                await ctx.author.add_roles(role)
                self.pend(ctx.author.id, ctx.author.display_name)
            elif role in ctx.author.roles:
                await ctx.author.send("You're already a player!")
            pass

    def pend(id, display_name):
        hero = Hero(id, display_name)
        basis = {
            'userID': [hero.userID],
            'name': [hero.name],
            'HP': [hero.HP],
            'STR': [hero.STR],
            'DEX': [hero.DEX],
            'SPD': [hero.SPD],
            'MPE': [hero.MPE],
            'HIT': [hero.HIT]
        }
        columns = ['userID', 'name', 'HP', 'STR', 'DEX', 'SPD', 'MPE', 'HIT']
        heropend = pd.DataFrame(basis, columns=columns)
        print(f'\n\nNEW PLAYER: {hero.name}\n{heropend}')
        global ps
        ps = ps.append(heropend, ignore_index=True)
        ps.to_csv('playerstatistics.csv', index=False)

def setup(client):
    client.add_cog(start(client))