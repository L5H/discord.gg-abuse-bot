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
    
    @commands.command()
    @commands.has_role("Lead Developer (owner)") # this is set to only me because the bot is currently self hosted, so my home connection doesnt get leaked lol ex. https://api.ipify.org/ using output text
    async def requests(self,ctx,url,output):
        #elif method == 'GET' or method == 'get': (was testing something here yes ik its elif and not if there was if before)
        if output == 'json' or output == 'JSON':
            responce = requests.get(url).json()
            embed = discord.Embed(title=f"HTTP GET results for {url} using JSON.",description=f"```json\n{responce}\n```")
            await ctx.send(embed=embed)
        elif output == 'text' or output == 'TEXT':
            responce = requests.get(url).text
            embed = discord.Embed(title=f"HTTP GET results for {url} using text.",description=f"```\n{responce}\n```")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description="Invalid parameters.")
            embed.add_field(name="JSON",value="```h.requests {url} json```\nThis returns JSON output from the url.",inline=False)
            embed.add_field(name="TEXT",value="```h.requests {url} text```\nThis returns text output from the url.",inline=False)
            embed.set_footer(text="Keep in mind this is only HTTP GET requests, POST request command has not been made.")
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(ownercommands(client))
