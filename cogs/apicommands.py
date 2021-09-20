import discord, aiohttp, time, os
from discord.ext import commands
from colorama import Fore, Style, init
init()

class apicommands(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_connect(self):
        print(f'[{Fore.GREEN}{Style.BRIGHT}+{Fore.RESET}] Loaded API Commands.')
        time.sleep(3)
        os.system('cls||clear')

    @commands.command()
    async def hentai(self,ctx):
        embed = discord.Embed(description="Removed due to the images being removed from the CDN. Sorry.",color=0x2f3136)
        await ctx.send(embed=embed)
        '''async with aiohttp.ClientSession() as s:
            async with s.get('https://api.hentaihaven.dev/nsfwapi') as r:
                hentai = await r.json()
                embed = discord.Embed(description="Hentai provided by https://api.hentaihaven.dev/nsfwapi",color=0x2f3136)
                embed.set_image(url=hentai['url'])
                await ctx.send(embed=embed)'''

    @commands.command()
    async def fact(self,ctx):
        async with aiohttp.ClientSession() as s:
            async with s.get("https://api.hentaihaven.dev/factapi") as r:
                fact = await r.json()
                embed = discord.Embed(title="Fact provided by [api.hentaihaven.dev](https://api.hentaihaven.dev/factapi)",description=fact['fact'],color=0x2f3136)
                await ctx.send(embed=embed)

    @commands.command(aliases=['cat'])
    async def kat(self,ctx):
        async with aiohttp.ClientSession() as s:
            async with s.get("https://api.hentaihaven.dev/katapi") as r:
                kat = await r.json()
                embed = discord.Embed(description="Kat PFP provided by [api.hentaihaven.dev](https://api.hentaihaven.dev/katapi)",color=0x2f3136)
                embed.set_image(url=kat['url'])
                embed.set_footer(text="If the image is low res, copy the image link in the embed and get it from there.\nDiscord lowers res of images in embeds.")
                await ctx.send(embed=embed)

def setup(client):
    client.add_cog(apicommands(client))