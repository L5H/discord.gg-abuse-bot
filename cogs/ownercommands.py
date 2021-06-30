import discord, aiohttp, requests
from discord.ext import commands
from colorama import Fore, Style, init
init()

class ownercommands(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'[{Fore.GREEN}{Style.BRIGHT}+{Fore.RESET}] Loaded Owner Commands.')
    
    @commands.command()
    @commands.has_role("Lead Developer (owner)")
    async def shutdown(self,ctx):
        embed = discord.Embed(description="Shutting down.")
        await ctx.send(embed=embed)
        print(f'[{Fore.RED}{Style.BRIGHT}x{Fore.RESET}] Shutdown.')
        exit()

    @commands.command(aliases=['hentaiscraper'])
    @commands.has_role("Lead Developer (owner)")
    async def hscrape(self,ctx):
        allowed_files = ["jpg", "jpeg", "png", "gif"] # from https://github.com/Codec04/hentai-web-scraper <3
        subreddits = ["hentai", "Nekomimi", "Sukebei"]
        for subreddit in subreddits:
            json_data = requests.get(f"https://www.reddit.com/r/{subreddit}/top.json?limit=69&t=month", headers={"User-agent": ""}).json()
            try:
                for image in range(0, 69):
                    image_url = json_data["data"]["children"][image]["data"]["url"]
                    for allowed_file in allowed_files:
                        if image_url.split(".")[-1] == allowed_file:
                            embed = discord.Embed(description="Hentai scraper")
                            embed.set_image(url=image_url)
                            await ctx.send(embed=embed)
            except IndexError:
                continue

def setup(client):
    client.add_cog(ownercommands(client))