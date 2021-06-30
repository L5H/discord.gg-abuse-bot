import discord
from discord.ext import commands
from colorama import Fore, Style, init
init()

class errorhandlers(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'[{Fore.GREEN}{Style.BRIGHT}+{Fore.RESET}] Loaded Error Handlers.')

    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        if isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(description="Command doesn't exist.")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(errorhandlers(client))