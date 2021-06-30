import discord, ctypes
from discord.ext import commands
from cogs import moderation, events, apicommands, ownercommands, usercommands, errorhandlers

ctypes.windll.kernel32.SetConsoleTitleW('hentaihaven.dev bot')
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="h.", intents=intents)
cogs = [errorhandlers, events, moderation, ownercommands, usercommands, apicommands]

for ok in range(len(cogs)):
    cogs[ok].setup(client)

client.run("no")