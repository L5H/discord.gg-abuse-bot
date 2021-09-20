import discord
from discord.ext import commands

class colors(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.color_roles = {
            "0": 888974745649938442,
            "1": 888974746396524545,
            "2": 888974747000508437,
            "3": 888974747600318505,
            "4": 888974748732755968,
            "5": 888974749550657608,
            "6": 888974750544719953,
            "7": 888974751450681344,
            "8": 888974752453132319,
            "9": 888974753078054973,
            "10": 888974754088878131,
            "11": 888974755221340181,
            "12": 888974756278329404,
            "13": 888974759910588467,
            "14": 888974760489398303,
            "15": 888974761139535913,
            "16": 888974762330705921
        }
    
    @commands.command()
    async def color(self, ctx, colorid=None):
        if colorid == None:
            await ctx.send(embed=discord.Embed(description="Please enter a number, look in<#888956219253985280> for color numbers.\n\nExample: `bash color 1`", color=0x2f3136))
        elif colorid not in self.color_roles:
            await ctx.send(embed=discord.Embed(description="Please enter a valid number, look in <#888956219253985280> for color numbers.", color=0x2f3136))
        else:
            await ctx.author.add_roles(ctx.guild.get_role(self.color_roles.get(colorid)))
            await ctx.send(embed=discord.Embed(description=f"Successfully gave you <@&{self.color_roles.get(colorid)}>.", color=0x2f3136))

    @commands.command(aliases=["removec"])
    async def removecolor(self, ctx, colorid=None):
        role = ctx.guild.get_role(self.color_roles.get(colorid))
        if colorid == None:
            await ctx.send(embed=discord.Embed(description="Please enter a number, look in<#888956219253985280> for color numbers.\n\nExample: `bash color 1`", color=0x2f3136))
        elif role not in ctx.author.roles:
            await ctx.send(embed=discord.Embed(description="You do not have that role.", color=0x2f3136))
        elif colorid not in self.color_roles:
            await ctx.send(embed=discord.Embed(description="Please enter a valid number, look in <#888956219253985280> for color numbers.", color=0x2f3136))
        else:
            await ctx.author.remove_roles(role)
            await ctx.send(embed=discord.Embed(description=f"Successfully removed role <@&{self.color_roles.get(colorid)}>.", color=0x2f3136))

def setup(client):
    client.add_cog(colors(client))