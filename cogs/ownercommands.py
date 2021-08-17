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
    @commands.has_role("discord.gg/g.")
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
    @commands.has_role("discord.gg/g.")
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

    @commands.command()
    @commands.has_role("discord.gg/g.")
    async def request(self,ctx,url,output):
        if output == 'json' or output == 'JSON':
            responce = requests.get(url).json()
            embed = discord.Embed(title=f"HTTP GET results for {url} using JSON.",description=f"```json\n{responce}\n```",color=0x2f3136)
            await ctx.send(embed=embed)
        elif output == 'text' or output == 'TEXT':
            responce = requests.get(url).text
            embed = discord.Embed(title=f"HTTP GET results for {url} using text.",description=f"```\n{responce}\n```",color=0x2f3136)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description="Invalid parameters.",color=0x2f3136)
            embed.add_field(name="JSON",value="```g.request {url} json```\nThis returns JSON output from the url.",inline=False)
            embed.add_field(name="TEXT",value="```g.request {url} text```\nThis returns text output from the url.",inline=False)
            embed.set_footer(text="Keep in mind this is only HTTP GET requests, POST request command has not been made.")
            await ctx.send(embed=embed)
    @request.error
    async def request_error(self,ctx,error):
        if isinstance(error,commands.MissingRole):
            embed = discord.Embed(description="You don't have the permission to do this.",color=0x2f3136)
            await ctx.send(embed=embed)
            return
        
    @commands.command(aliases=['hentaiscraper'])
    @commands.has_role("discord.gg/g.")
    async def hscrape(self,ctx):
        allowed_files = ["jpg", "jpeg", "png", "gif"] # from https://g.hub.com/Codec04/hentai-web-scraper <3
        subreddits = ["hentai", "Nekomimi", "Sukebei"]
        for subreddit in subreddits:
            json_data = requests.get(f"https://www.reddit.com/r/{subreddit}/top.json?limit=69&t=month", headers={"User-agent": ""}).json()
            try:
                for image in range(0, 69):
                    image_url = json_data["data"]["children"][image]["data"]["url"]
                    for allowed_file in allowed_files:
                        if image_url.split(".")[-1] == allowed_file:
                            embed = discord.Embed(description="Hentai Scraper",color=0x2f3136)
                            embed.set_image(url=image_url)
                            await ctx.send(embed=embed)
            except IndexError:
                continue
    @hscrape.error
    async def hscrape_error(self,ctx,error):
        if isinstance(error,commands.MissingRole):
            embed = discord.Embed(description="You don't have the permission to do this.",color=0x2f3136)
            await ctx.send(embed=embed)
            return

def setup(client):
    client.add_cog(ownercommands(client))