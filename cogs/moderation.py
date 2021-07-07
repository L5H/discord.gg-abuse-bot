import discord
from discord.ext import commands
from colorama import Fore, Style, init
init()

class moderation(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'[{Fore.GREEN}{Style.BRIGHT}+{Fore.RESET}] Loaded Moderation.')

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx,member:discord.Member,*,reason= "None"):
        if member == ctx.author:
            embed = discord.Embed(description="You can't kick yourself dumbass.")
            await ctx.send(embed=embed)
            return
        embed = discord.Embed(title=f"Kicked {member}", description=f"Reason: {reason}")
        embed.set_footer(text=f"Kicked by {ctx.author}")
        await ctx.send(embed=embed)
        await member.send("You were kicked from hentaihaven.dev official discord for: "+reason)
        await member.kick(reason=reason)
    @kick.error
    async def kick_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description="You didn't mention a user to kick.")
            embed.set_footer(text=f"Kick attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(description="You don't have permission to do this.")
            embed.set_footer(text=f"Kick attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.MemberNotFound):
            embed = discord.Embed(description=f"User was not found.")
            embed.set_footer(text=f"Kick attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.CommandInvokeError):
            embed = discord.Embed(description=f"Could not kick the user. (CommandInvokeError)")
            embed.set_footer(text=f"Kick attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx,member:discord.Member,*,reason= "None"):
        if member == ctx.author:
            embed = discord.Embed(description="You can't ban yourself dumbass.")
            await ctx.send(embed=embed)
            return
        embed = discord.Embed(title=f"Banned {member}", description=f"Reason: {reason}")
        embed.set_footer(text=f"Banned by {ctx.author}")
        await ctx.send(embed=embed)
        await member.send("You were banned from hentaihaven.dev official discord for: "+reason)
        await member.ban(reason=reason)
    @ban.error
    async def ban_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description="You didn't mention a user to ban.")
            embed.set_footer(text=f"Ban attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(description="You don't have permission to do this.")
            embed.set_footer(text=f"Ban attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.MemberNotFound):
            embed = discord.Embed(description="User was not found.")
            embed.set_footer(text=f"Ban attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.CommandInvokeError):
            embed = discord.Embed(description="Could not ban the user. (CommandInvokeError)")
            embed.set_footer(text=f"Ban attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return
        
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self,ctx,*,member):
        busers = await ctx.guild.bans()
        name,tag = member.split('#')
        for ok in busers:
            user = ok.user
            if(user.name,user.discriminator)==(name,tag):
                await ctx.guild.unban(user)
                embed = discord.Embed(description=f"{name} has been unbanned.")
                embed.set_footer(text = f"Unbanned by {ctx.author}")
                await ctx.send(embed=embed)
                return
        embed = discord.Embed(description=f"{member} not found.")
        await ctx.send(embed=embed)
    @unban.error
    async def unban_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description="You did not give the username of the user to unban.")
            embed.set_footer(text=f"Unban attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(description="You don't have the permission to do this.")
            embed.set_footer(text=f"Unban attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.CommandInvokeError):
            embed = discord.Embed(description="This member is an admin.")
            embed.set_footer(text=f"Unban attempted by {ctx.author}")
            return

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self,ctx,member:discord.Member,*,reason= "no reason"):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if member == ctx.author:
            embed = discord.Embed(description="you cant mute yourself retard")
            await ctx.send(embed=embed)
            return
        if not role: # if my muted role is somehow deleted by my stupid ass mods
            role = await ctx.guild.create_role(name='Muted', permissions=discord.Permissions())
            await ctx.channel.set_permissions(role, send_messages=False, read_message_history=True, read_messages=True)
            return
        await member.edit(roles=[role])
        embed = discord.Embed(title=f"Muted {member}", description=f"Reason: {reason}")
        embed.set_footer(text=f"Muted by {ctx.author}")
        await ctx.send(embed=embed)
    @mute.error
    async def mute_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description="You did not mention a member to mute.")
            embed.set_footer(text=f"Mute attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(description="You don't have permission to do this.")
            embed.set_footer(text=f"Mute attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.MemberNotFound):
            embed = discord.Embed(description="Member was not found.")
            embed.set_footer(text=f"Mute attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.CommandInvokeError):
            embed = discord.Embed(description="This member is an admin.")
            embed.set_footer(text=f"Mute attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unmute(self,ctx,member:discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(role)
        embed = discord.Embed(description=f"{member.mention} was unmuted.")
        embed.set_footer(text=f"Unmuted by {ctx.author}")
        await ctx.send(embed=embed)
    @unmute.error
    async def unmute_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description="You did not mention a member to unmute.")
            embed.set_footer(text=f"Unmute attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(description="You don't have the permission to do this.")
            embed.set_footer(text=f"Unmute attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.MemberNotFound):
            embed = discord.Embed(description=f"Member was not found.")
            embed.set_footer(text=f"Unmute attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.CommandInvokeError):
            embed = discord.Embed(description="This member is not muted.")
            embed.set_footer(text=f"Unmute attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def slowmode(self,ctx,seconds):
        await ctx.channel.edit(slowmode_delay=seconds)
        embed = discord.Embed(description=f"Set channels slowmode to {seconds} seconds.")
        await ctx.send(embed=embed)
    @slowmode.error
    async def slowmode_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description="You did not specify how many seconds you wanted to set the slowmode to this channel.")
            await ctx.send(embed=embed)
            return
        if isinstance(error, MissingPermissions):
            embed = discord.Embed(description="You don't have permission to do this.")
            await ctx.send(embed=embed)
            return
    
    @commands.command(aliases=['clear'])
    @commands.has_permissions(manage_messages=True)
    async def purge(self,ctx,nig: int):
        await ctx.channel.purge(limit=nig+1)
        embed = discord.Embed(description=f"{nig} message(s) were deleted")
        await ctx.send(embed=embed)
    @purge.error
    async def purge_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description="You did not specify an amount of messages you wanted to delete.")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(description="You don't have the permission to do this.")
            await ctx.send(embed=embed)
            return

    @commands.command(aliases=['chanlock'])
    @commands.has_permissions(manage_channels=True)
    async def channellock(self,ctx,arg):
        if arg == 'true':
            overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
            overwrite.send_messages = False
            await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
            embed = discord.Embed(description="Channel successfully locked.")
            await ctx.send(embed=embed)
        elif arg == 'false':
            overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
            overwrite.send_messages = True
            await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
            embed = discord.Embed(description="Channel successfully unlocked.")
            await ctx.send(embed=embed)
        elif arg == None:
            print("arg None test") #this doesnt debug??????????????
        else:
            embed = discord.Embed(description="Argument can only be 'true' or 'false'.")
            await ctx.send(embed=embed)
            return
    @channellock.error #'function' object has no attribute 'error' ?????????????? (update: i was stupid and forgot to add () to the end of commands.command on channelock command lol)
    async def channellock_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(description="You don't have the permission to do this.")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.MissingRequiredArgument): # elif arg == None: doesnt want to work so this is the error handler for now
            embed = discord.Embed(description="Argument can only be 'true' or 'false'.")
            await ctx.send(embed=embed)
            return

    @commands.command(aliases=['chpr', 'changestatus'])
    @commands.has_permissions(manage_messages=True)
    async def changepresence(self,ctx,*,arg):
        await self.client.change_presence(activity=discord.Game(name=arg))
        embed = discord.Embed(description="Changed status to "+arg)
        await ctx.send(embed=embed)
    @changepresence.error
    async def changepresence_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description="You did not include a status to set.")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(description="You don't have the permission to do this.")
            await ctx.send(embed=embed)
            return

def setup(client):
    client.add_cog(moderation(client))
