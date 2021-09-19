import discord, requests, os
from discord.ext import commands
from colorama import Fore, Style, init
init()

class ownercommands(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_connect(self):
        print(f'[{Fore.GREEN}{Style.BRIGHT}+{Fore.RESET}] Loaded Owner Commands.')
    
    @commands.command()
    @commands.has_role("superior")
    async def shutdown(self,ctx):
        embed = discord.Embed(description="Shutting down.",color=0x2f3136)
        await ctx.send(embed=embed)
        print(f'[{Fore.RED}{Style.BRIGHT}x{Fore.RESET}] Shutdown.')
        exit()
    @shutdown.error
    async def shutdown_error(self,ctx,error):
        if isinstance(error,commands.MissingRole):
            embed = discord.Embed(description="You don't have the permission to do this.",color=0x2f3136)
            await ctx.send(embed=embed)
            return

    @commands.command(aliases=['clearterm'])
    @commands.has_role("superior")
    async def clearterminal(self,ctx):
        embed = discord.Embed(description="Cleared the terminal.",color=0x2f3136)
        await ctx.send(embed=embed)
        os.system('cls||clear')
        print(f'[{Fore.YELLOW}{Style.BRIGHT}!{Fore.RESET}] Cleared terminal.')
    @clearterminal.error
    async def clearterminal_error(self,ctx,error):
        if isinstance(error,commands.MissingRole):
            embed = discord.Embed(description="You don't have the permission to do this.",color=0x2f3136)
            await ctx.send(embed=embed)
            return

def setup(client):
    client.add_cog(ownercommands(client))