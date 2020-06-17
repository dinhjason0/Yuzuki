#Call page, all commands aer reeled in here.
import os
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

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        client.load_extension(f'cogs.{filename[:-3]}')

#Pandas Read Player Stats
ps = pd.read_csv('playerstatistics.csv')
print(ps)

client.run(brokken.token)