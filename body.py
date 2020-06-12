#Call page, all commands aer reeled in here.
import asyncio
import discord
from discord.ext import commands
import time
import pandas as pd
import brokken
from heroes import Hero

#ID 718221388963381309


#This is discord.py's call. commands.Bot(lambada: prefix)
client = commands.Bot(command_prefix = '.', case_insensitive=True, owner_id=154662042513440768)

#Pandas Read Player Stats
ps = pd.read_csv('playerstatistics.csv')
print(ps)

#Good Morning, Yuzuki
@client.event
async def on_ready():
    print(f'{client.user.name} Is Awake')
    client.loop.create_task(change_status())

#Uptime Clock
async def change_status():
    #The "currently playing" message on Yuzuki
        await client.change_presence(activity=discord.Game(f"This message is pissing me off"))

#Member Join
@client.event
async def on_member_join(member):
    print(f"{member}, what a mistake they made.")
    await member.send("Welcome, this is a closed invite server. Use .start to begin")

#Member Leave
@client.event
async def on_member_remove(member):
    print(f"{member} has left.")

#Ping measurement
@client.command(name = 'ping')
async def ping(dtx):
    await dtx.send(f"Your ping is {round(client.latency * 1000)}ms")

#LINK START: If user has 'player' role, disable them from having permission to use this command again
@client.command(name = 'start')
async def start(ctx):
    role = discord.utils.get(ctx.guild.roles, name='Player')
    if role not in ctx.author.roles:
        await ctx.author.send("Thank you for starting. Lets begin.")
        await ctx.send(f"Link connection has been established. Say hello to your room...")
        await ctx.author.add_roles(role)
        pend(ctx.author.id, ctx.author.display_name)
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
    columns = ['userID','name','HP','STR','DEX','SPD','MPE','HIT']
    heropend = pd.DataFrame(basis, columns=columns)
    print(f'\n\nNEW PLAYER: {hero.name}\n{heropend}')
    global ps
    ps = ps.append(heropend, ignore_index=True)
    ps.to_csv('playerstatistics.csv', index = False)

client.run(brokken.token)