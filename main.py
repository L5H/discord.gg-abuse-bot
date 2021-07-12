import discord, sys
from discord.ext import commands
from cogs import moderation, events, apicommands, ownercommands, usercommands, errorhandlers

sys.stdout.buffer.write(b'\33]0;hentaihaven.dev bot\a')
sys.stdout.buffer.flush()
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="h.", intents=intents)
cogs = [errorhandlers, events, moderation, ownercommands, usercommands, apicommands]

for ok in range(len(cogs)):
    cogs[ok].setup(client)

client.run("no")
