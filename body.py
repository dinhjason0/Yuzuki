#Call page, all commands aer reeled in here.
import asyncio
import discord
from discord.ext import commands
import time
import brokken

#ID 718221388963381309

#This is discord.py's call. commands.Bot(lambada: prefix)
client = commands.Bot(command_prefix = '.', case_insensitive=True)

#Good Morning, Yuzuki
@client.event
async def on_ready():
    print(f'{client.user.name} Is Awake')
    await client.loop.create_task(change_status())


#Uptime Clock
async def change_status():
    #The "currently playing" message on Yuzuki
    i = 0
    while True:
        await client.change_presence(activity = discord.Game(f"The bot has been live for {++i} seconds"))
        await asyncio.sleep(1)
#Change_presence(activity), check documentation.

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

#LINK START
#If user has 'player' role, disable them from having permission to use this command again
@client.command(name = 'start')
async def start(ctx, guild: discord.Guild = None):
    guild = ctx.guild if not guild else guild
    role = ('Player')
    if role not in ctx.author.roles:
        await ctx.author.send("Thank you for starting. Lets begin.")
        await ctx.send(f"Link connection has been established. Say hello to your room...")

client.run(brokken.token)