#Call page, all commands aer reeled in here.
import os
from discord.ext import commands
import brokken

#ID 718221388963381309

#This is discord.py's call. commands.Bot(lambada: prefix)
client = commands.Bot(command_prefix = '.', case_insensitive=True, owner_id=154662042513440768)

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(brokken.token)