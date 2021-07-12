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
    async def kick(self,ctx,member:discord.Member,*,reason="None"):
        if member == ctx.author:
            embed = discord.Embed(description="You can't kick yourself dumbass.",color=0x2f3136)
            await ctx.send(embed=embed)
            return
        embed = discord.Embed(title=f"Kicked {member}", description=f"Reason: `{reason}`",color=0x2f3136)
        embed.set_footer(text=f"Kicked by {ctx.author}")
        await ctx.send(embed=embed)
        embed = discord.Embed(description=f"You were kicked from discord.gg/cloudflare for: `{reason}`",color=0x2f3136)
        await member.send(embed=embed)
        await member.kick(reason=reason)
    @kick.error
    async def kick_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description="You didn't mention a user to kick.\n\n`h.kick {user} {reason}`",color=0x2f3136)
            embed.set_footer(text=f"Kick attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(description="You don't have permission to do this.",color=0x2f3136)
            embed.set_footer(text=f"Kick attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.MemberNotFound):
            embed = discord.Embed(description=f"User was not found.",color=0x2f3136)
            embed.set_footer(text=f"Kick attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.CommandInvokeError):
            embed = discord.Embed(description=f"Could not kick the user. (CommandInvokeError)",color=0x2f3136)
            embed.set_footer(text=f"Kick attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx,member:discord.Member,*,reason="None"):
        if member == ctx.author:
            embed = discord.Embed(description="You can't ban yourself dumbass.",color=0x2f3136)
            await ctx.send(embed=embed)
            return
        embed = discord.Embed(title=f"Banned {member}", description=f"Reason: {reason}",color=0x2f3136)
        embed.set_footer(text=f"Banned by {ctx.author}")
        await ctx.send(embed=embed)
        embed = discord.Embed(description=f"You were banned from discord.gg/cloudflare for: `{reason}`",color=0x2f3136)
        await member.send(embed=embed)
        await member.ban(reason=reason)
    @ban.error
    async def ban_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description="You didn't mention a user to ban.\n\n`h.ban {user} {reason}`",color=0x2f3136)
            embed.set_footer(text=f"Ban attempted by {ctx.author}")
            await ctx.send(embed=embed)
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(description="You don't have permission to do this.",color=0x2f3136)
            embed.set_footer(text=f"Ban attempted by {ctx.author}")
            await ctx.send(embed=embed)
        if isinstance(error, commands.MemberNotFound):
            embed = discord.Embed(description="User was not found.",color=0x2f3136)
            embed.set_footer(text=f"Ban attempted by {ctx.author}")
            await ctx.send(embed=embed)
        if isinstance(error, commands.CommandInvokeError):
            embed = discord.Embed(description="Could not ban the user. (CommandInvokeError)",color=0x2f3136)
            embed.set_footer(text=f"Ban attempted by {ctx.author}")
            await ctx.send(embed=embed)
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self,ctx,*,member):
        busers = await ctx.guild.bans()
        name,tag = member.split('#')
        for ok in busers:
            user = ok.user
            if(user.name,user.discriminator)==(name,tag):
                await ctx.guild.unban(user)
                embed = discord.Embed(description=f"{name} has been unbanned.",color=0x2f3136)
                embed.set_footer(text = f"Unbanned by {ctx.author}")
                await ctx.send(embed=embed)
                return
        embed = discord.Embed(description=f"{member} not found.",color=0x2f3136)
        await ctx.send(embed=embed)
    @unban.error
    async def unban_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description="You did not give the username of the user to unban.\n\n`h.unban {usernamewithtag}`",color=0x2f3136)
            embed.set_footer(text=f"Unban attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(description="You don't have the permission to do this.",color=0x2f3136)
            embed.set_footer(text=f"Unban attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.CommandInvokeError):
            embed = discord.Embed(description="This member is an admin.",color=0x2f3136)
            embed.set_footer(text=f"Unban attempted by {ctx.author}")
            return

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self,ctx,member:discord.Member,*,reason="None"):
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if member == ctx.author:
            embed = discord.Embed(description="you cant mute yourself retard",color=0x2f3136)
            await ctx.send(embed=embed)
            return
        if not role: # if my muted role is somehow deleted by my stupid ass mods
            role = await ctx.guild.create_role(name='Muted', permissions=discord.Permissions())
            await ctx.channel.set_permissions(role, send_messages=False, read_message_history=True, read_messages=True)
            return
        await member.edit(roles=[role])
        embed = discord.Embed(title=f"Muted {member}", description=f"Reason: `{reason}`",color=0x2f3136)
        embed.set_footer(text=f"Muted by {ctx.author}")
        await ctx.send(embed=embed)
        embed = discord.Embed(description=f"You were muted in discord.gg/cloudflare for: `{reason}`",color=0x2f3136)
        await member.send(embed=embed)
    @mute.error
    async def mute_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description="You did not mention a member to mute.\n\n`h.mute {member} {reason}`",color=0x2f3136)
            embed.set_footer(text=f"Mute attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(description="You don't have permission to do this.",color=0x2f3136)
            embed.set_footer(text=f"Mute attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.MemberNotFound):
            embed = discord.Embed(description="Member was not found.",color=0x2f3136)
            embed.set_footer(text=f"Mute attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.CommandInvokeError):
            embed = discord.Embed(description="This member is an admin.",color=0x2f3136)
            embed.set_footer(text=f"Mute attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unmute(self,ctx,member:discord.Member):
        role = discord.utils.get(ctx.guild.roles,name="Muted")
        await member.remove_roles(role)
        embed = discord.Embed(description=f"{member.mention} was unmuted.",color=0x2f3136)
        embed.set_footer(text=f"Unmuted by {ctx.author}")
        await ctx.send(embed=embed)
    @unmute.error
    async def unmute_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description="You did not mention a member to unmute.\n\n`h.unmute {user}`",color=0x2f3136)
            embed.set_footer(text=f"Unmute attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(description="You don't have the permission to do this.",color=0x2f3136)
            embed.set_footer(text=f"Unmute attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.MemberNotFound):
            embed = discord.Embed(description=f"Member was not found.",color=0x2f3136)
            embed.set_footer(text=f"Unmute attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.CommandInvokeError):
            embed = discord.Embed(description="This member is not muted.",color=0x2f3136)
            embed.set_footer(text=f"Unmute attempted by {ctx.author}")
            await ctx.send(embed=embed)
            return
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def slowmode(self,ctx,seconds):
        await ctx.channel.edit(slowmode_delay=seconds)
        embed = discord.Embed(description=f"Set channels slowmode to {seconds} seconds.",color=0x2f3136)
        await ctx.send(embed=embed)
    @slowmode.error
    async def slowmode_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description="You did not specify how many seconds you wanted to set the slowmode to this channel.\n\n`h.slowmode {seconds}`",color=0x2f3136)
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(description="You don't have permission to do this.",color=0x2f3136)
            await ctx.send(embed=embed)
            return

    @commands.command(alias=['nick','nn'])
    @commands.has_permissions(manage_nicknames=True)
    async def nickname(self,ctx,member:discord.Member,*,arg):
        embed = discord.Embed(description=f"Changed {member.mention}'s nickname to {arg}",color=0x2f3136)
        embed.set_footer(text=f"Nickname changed by {ctx.author}")
        await ctx.send(embed=embed)
        await member.edit(nick=arg)
    @nickname.error
    async def nickname_error(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            embed = discord.Embed(description="You did not specify the correct arguments.\n\n`h.nickname {user} {nickname}`",color=0x2f3136)
            await ctx.send(embed=embed)
            return
        if isinstance(error,commands.MissingPermissions):
            embed = discord.Embed(description="You don't have the permission to do this.",color=0x2f3136)
            await ctx.send(embed=embed)
            return

    @commands.command(aliases=['clear'])
    @commands.has_permissions(manage_messages=True)
    async def purge(self,ctx,nig: int):
        await ctx.channel.purge(limit=nig+1)
        embed = discord.Embed(description=f"{nig} message(s) were deleted",color=0x2f3136)
        embed.set_footer(text=f"Purge used by {ctx.author}")
        await ctx.send(embed=embed)
    @purge.error
    async def purge_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description="You did not specify an amount of messages you wanted to delete.\n\n`h.purge {amount}`",color=0x2f3136)
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(description="You don't have the permission to do this.",color=0x2f3136)
            await ctx.send(embed=embed)
            return

    @commands.command(aliases=['chanlock'])
    @commands.has_permissions(manage_channels=True)
    async def channellock(self,ctx,arg):
        if arg == 'true':
            overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
            overwrite.send_messages = False
            await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
            embed = discord.Embed(description="Channel successfully locked.",color=0x2f3136)
            await ctx.send(embed=embed)
        elif arg == 'false':
            overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
            overwrite.send_messages = True
            await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
            embed = discord.Embed(description="Channel successfully unlocked.",color=0x2f3136)
            await ctx.send(embed=embed)
        elif arg == None:
            print("arg None test") #this doesnt debug??????????????
        else:
            embed = discord.Embed(description="Argument can only be 'true' or 'false'.",color=0x2f3136)
            await ctx.send(embed=embed)
            return
    @channellock.error #'function' object has no attribute 'error' ?????????????? (update: i was stupid and forgot to add () to the end of commands.command on channelock command lol)
    async def channellock_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(description="You don't have the permission to do this.",color=0x2f3136)
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.MissingRequiredArgument): # elif arg == None: doesnt want to work so this is the error handler for now
            embed = discord.Embed(description="Argument can only be `true` or `false`.",color=0x2f3136)
            await ctx.send(embed=embed)
            return

    @commands.command(aliases=['chpr', 'changestatus'])
    @commands.has_permissions(manage_messages=True)
    async def changepresence(self,ctx,*,arg):
        await self.client.change_presence(activity=discord.Game(name=arg))
        embed = discord.Embed(description="Changed status to "+arg,color=0x2f3136)
        await ctx.send(embed=embed)
    @changepresence.error
    async def changepresence_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description="You did not include a status to set.\n\n`h.changepresence {name}`",color=0x2f3136)
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(description="You don't have the permission to do this.",color=0x2f3136)
            await ctx.send(embed=embed)
            return

def setup(client):
    client.add_cog(moderation(client))
