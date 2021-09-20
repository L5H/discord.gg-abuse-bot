import discord, server
from discord.ext import commands
from cogs import moderation, events, apicommands, ownercommands, usercommands, errorhandlers, utilities, voice, colors

server.server()
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=['bash '], intents=intents, case_insensitive=True, activity=discord.Streaming(type=discord.ActivityType.watching, name="discord.gg/abuse", url="https://sex-trafficking.cf/"))
cogs = [errorhandlers, events, moderation, utilities, voice, ownercommands, usercommands, apicommands, colors]
client.remove_command('help')

for ok in range(len(cogs)):
    cogs[ok].setup(client)

client.run("no")