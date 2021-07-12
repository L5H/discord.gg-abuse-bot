import discord, os
from discord.ext import commands
from cogs import moderation, events, apicommands, ownercommands, usercommands, errorhandlers

os.system("title hentaihaven.dev bot")
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="h.", intents=intents, case_insensitive=False)
cogs = [errorhandlers, events, moderation, ownercommands, usercommands, apicommands]

for ok in range(len(cogs)):
    cogs[ok].setup(client)

client.run("no")
