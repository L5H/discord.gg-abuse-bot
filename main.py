import discord, os, time
from discord.ext import commands
from cogs import moderation, events, apicommands, ownercommands, usercommands, errorhandlers, utilities

os.system("title hentaihaven.dev bot")
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=["h.","H."], intents=intents, case_insensitive=True)
cogs = [errorhandlers, events, moderation, utilities, ownercommands, usercommands, apicommands]
client.remove_command('help')

a = 0
lol = ["/","|","\̲","√"]
while True:
    print("Initializing.. "+lol[a%len(lol)],end='\r')
    a += 1
    time.sleep(.1)
    if a == 20:
        for ok in range(len(cogs)):
            cogs[ok].setup(client)
        client.run("no")
