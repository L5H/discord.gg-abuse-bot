import discord
from discord.ext import commands
from cogs import moderation, events, apicommands, ownercommands, usercommands, errorhandlers, utilities, voice

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=['g.'], intents=intents, case_insensitive=True)
cogs = [errorhandlers, events, moderation, utilities, voice, ownercommands, usercommands, apicommands]
client.remove_command('help')

for ok in range(len(cogs)):
    cogs[ok].setup(client)

client.run("ODU0MDM2NDAzMTU4OTA4OTM5.YMeFYQ.-M1cBVZsnbkE79I7pHForGqNYwk")