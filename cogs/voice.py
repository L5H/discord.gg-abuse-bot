import discord
from discord.ext import commands
from colorama import Fore, Style, init
init()

class voice(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_connect(self):
        print(f'[{Fore.GREEN}{Style.BRIGHT}+{Fore.RESET}] Loaded Voice.')

    @commands.command() # basic join and leave commands for now
    async def join(self,ctx):
        await ctx.author.voice.channel.connect()
    
    @commands.command()
    async def leave(self,ctx):
        await ctx.guild.voice_client.disconnect()

def setup(client):
    client.add_cog(voice(client))