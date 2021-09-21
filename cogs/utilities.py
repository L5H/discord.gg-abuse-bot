import discord, requests
from discord.ext import commands
from colorama import Fore, Style, init
init()

class utilities(commands.Cog):
    def __init__(self,client):
        self.client = client
        self.token = "no"

    @commands.Cog.listener()
    async def on_connect(self):
        print(f'[{Fore.GREEN}{Style.BRIGHT}+{Fore.RESET}] Loaded Utilites.')

    @commands.command()
    async def help(self,ctx,*,option:str=None):
        if not option:
            embed = discord.Embed(color=0x2f3136)
            embed.add_field(name="User Commands",value="Shows commands all users can use.\n**Usage:** `bash help user`",inline=False)
            embed.add_field(name="Moderation Commands",value="Show commands only moderators/admins can use.\n**Usage:** `bash help mod`",inline=False)
            embed.add_field(name="Voice Commands",value="Shows voice channel commands. __**Currently in development.**__\n**Usage:** `bash help voice`",inline=False)
            embed.add_field(name="Utilities",value="Shows utilities.\n**Usage:** `bash help util`",inline=False)
            embed.add_field(name="Color",value="Shows color role commands.\n**Usage:** `bash help color`",inline=False)
            embed.set_footer(text="Prefix: bash \nDeveloper: cia#0002\nGithub: https://github.com/tokenlogger/discord.gg-abuse-bot/")
            embed.set_thumbnail(url=requests.get("https://api.hentaihaven.dev/katapi").json()['url'])
            await ctx.send(embed=embed)
        elif option == "user":
            embed = discord.Embed(title="User Commands",color=0x2f3136)
            embed.add_field(name="`bash kat`",value="Sends a picture of a random cat from **https://api.hentaihaven.dev/katapi**",inline=False)
            embed.add_field(name="`bash fact`",value="Sends a random fact from **https://api.hentaihaven.dev/factapi**",inline=False)
            embed.add_field(name="`bash hentai`",value="Sends hentai from **https://api.hentaihaven.dev/factapi**",inline=False)
            embed.add_field(name="`bash snipe`",value="Sends the most recently deleted message. (all deleted/edited messages are logged anyways)",inline=False)
            embed.add_field(name="`bash stealcookie`",value="Steals a users cookie.\n**Usage:** `bash stealcookie {user}`\n\n",inline=False)
            embed.add_field(name="`bash stealtoken`",value="Steals a users token.\n**Usage:** `bash stealtoken {user}`",inline=False)
            embed.set_footer(text="Prefix: bash \nDeveloper: cia#0002\nGithub: https://github.com/tokenlogger/discord.gg-abuse-bot/")
            embed.set_thumbnail(url=requests.get("https://api.hentaihaven.dev/katapi").json()['url'])
            await ctx.send(embed=embed)
        elif option == "mod":
            embed = discord.Embed(title="Moderation Commands",color=0x2f3136)
            embed.add_field(name="`bash kick`",value="Kicks a user.\n**Usage:** `bash kick {user} {reason}`",inline=False)
            embed.add_field(name="`bash ban`",value="Bans a user.\n**Usage:** `bash ban {user} {reason}`",inline=False)
            embed.add_field(name="`bash banbyname`",value="Mass bans by a name given. **ONLY USE IF BEING RAIDED**\n**Usage:** `bash banbyname {name} {reason}`",inline=False)
            embed.add_field(name="`bash unban`",value="Unbans a user.\n**Usage:** `bash unban {user+tag}`",inline=False)
            embed.add_field(name="`bash mute`",value="Mutes a user.\n**Usage:** `bash mute {user} {reason}`",inline=False)
            embed.add_field(name="`bash unmute`",value="Unmutes a user.\n**Usage:** `bash unmute {user}`",inline=False)
            embed.set_footer(text="Prefix: bash \nDeveloper: cia#0002\nGithub: https://github.com/tokenlogger/discord.gg-abuse-bot/")
            embed.set_thumbnail(url=requests.get("https://api.hentaihaven.dev/katapi").json()['url'])
            await ctx.send(embed=embed)
        elif option == "voice":
            embed = discord.Embed(title="Voice Commands",color=0x2f3136)
            embed.add_field(name="`bash join`",value="Joins the users voice channel.",inline=False)
            embed.add_field(name="`bash leave`",value="Leaves the users voice channel.",inline=False)
            embed.set_footer(text="Prefix: bash \nDeveloper: cia#0002\nGithub: https://github.com/tokenlogger/discord.gg-abuse-bot/")
            embed.set_thumbnail(url=requests.get("https://api.hentaihaven.dev/katapi").json()['url'])
            await ctx.send(embed=embed)
        elif option == "util":
            embed = discord.Embed(title="Utilites",color=0x2f3136)
            embed.add_field(name="`bash avatar`",value="Shows a users avatar.\n**Usage:** `bash avatar {user}`",inline=False)
            embed.add_field(name="`bash banner`",value="Shows a users banner.\n**Usage:** `bash banner {user}`",inline=False)
            embed.add_field(name="`bash slowmode`",value="Adds slowmode to the channel.\n**Usage:** `bash slowmode {seconds}`",inline=False)
            embed.add_field(name="`bash nickname`",value="Adds a nickname to a user.\n**Usage:** `bash nickname {user} {nickname}`",inline=False)
            embed.add_field(name="`bash purge`",value="Deletes an amount of messages in a channel.\n**Usage:** `bash purge {amount}`",inline=False)
            embed.add_field(name="`bash channellock`",value="Locks the channel.\n**Usage:** `bash channellock {true/false}`",inline=False)
            embed.add_field(name="`bash changepresence`",value="Changes the bots presence.\n**Usage:** `bash changepresence {presence}`",inline=False)
            embed.set_footer(text="Prefix: bash \nDeveloper: cia#0002\nGithub: https://github.com/tokenlogger/discord.gg-abuse-bot/")
            embed.set_thumbnail(url=requests.get("https://api.hentaihaven.dev/katapi").json()['url'])
            await ctx.send(embed=embed)
        elif option == "color":
            embed = discord.Embed(title="Color",color=0x2f3136)
            embed.add_field(name="`bash color`",value="Adds a selected color role from <#888956219253985280>.\n**Usage:** `bash color {id}`",inline=False)
            embed.add_field(name="`bash removecolor`",value="Removes a selected color role from <#888956219253985280>.\n**Usage:** `bash removecolor {id}`",inline=False)
            embed.set_footer(text="Prefix: bash \nDeveloper: cia#0002\nGithub: https://github.com/tokenlogger/discord.gg-abuse-bot/")
            embed.set_thumbnail(url=requests.get("https://api.hentaihaven.dev/katapi").json()['url'])
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(color=0x2f3136)
            embed.add_field(name="User Commands",value="Shows commands all users can use.\n**Usage:** `bash help user`",inline=False)
            embed.add_field(name="Moderation Commands",value="Show commands only moderators/admins can use.\n**Usage:** `bash help mod`",inline=False)
            embed.add_field(name="Voice Commands",value="Shows voice channel commands. __**Currently in development.**__\n**Usage:** `bash help voice`",inline=False)
            embed.add_field(name="Utilities",value="Shows utilities.\n**Usage:** `bash help util`",inline=False)
            embed.add_field(name="Color",value="Shows color role commands.\n**Usage:** `bash help color`",inline=False)
            embed.set_footer(text="Prefix: bash \nDeveloper: cia#0002\nGithub: https://github.com/tokenlogger/discord.gg-abuse-bot/")
            embed.set_thumbnail(url=requests.get("https://api.hentaihaven.dev/katapi").json()['url'])
            await ctx.send(embed=embed)

    @commands.command(aliases=['av','ava','pfp'])
    async def avatar(self,ctx,member:discord.Member):
        embed = discord.Embed(description=f"{member}'s avatar.",color=0x2f3136)
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)
    @avatar.error
    async def avatar_error(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            embed = discord.Embed(description="You did not mention a user.\n\n`bash avatar {user}`",color=0x2f3136)
            await ctx.send(embed=embed)
            return

    @commands.command()
    async def banner(self, ctx, user: discord.User=None):
        if user == None:
            r = requests.get(f"https://discord.com/api/v9/users/{ctx.author.id}", headers={"Authorization": "Bot " + self.token}).json()
            if r["banner"] == None:
                embed = discord.Embed(description=f"You don't have a banner.", color=0x2f3136)
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(description=f"Here's your banner.\n\n[png](https://cdn.discordapp.com/banners/{ctx.author.id}/{r['banner']}.png)\n[jpg](https://cdn.discordapp.com/banners/{ctx.author.id}/{r['banner']}.jpg)\n[gif](https://cdn.discordapp.com/banners/{ctx.author.id}/{r['banner']}.gif)\n",color=0x2f3136)
                embed.set_image(url=f"https://cdn.discordapp.com/banners/{ctx.author.id}/{r['banner']}.gif?size=4096")
                await ctx.send(embed=embed)
        else:
            r = requests.get(f"https://discord.com/api/v9/users/{user.id}", headers={"Authorization": "Bot " + self.token}).json()
            if r["banner"] == None:
                embed = discord.Embed(description=f"{user} doesn't have a banner.", color=0x2f3136)
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(description=f"{user}'s banner.\n\n[png](https://cdn.discordapp.com/banners/{user.id}/{r['banner']}.png)\n[jpg](https://cdn.discordapp.com/banners/{user.id}/{r['banner']}.jpg)\n[gif](https://cdn.discordapp.com/banners/{user.id}/{r['banner']}.gif)\n", color=0x2f3136)
                embed.set_image(url=f"https://cdn.discordapp.com/banners/{user.id}/{r['banner']}?size=4096")
                await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def slowmode(self,ctx,seconds):
        await ctx.channel.edit(slowmode_delay=seconds)
        embed = discord.Embed(description=f"Set channels slowmode to {seconds} seconds.",color=0x2f3136)
        await ctx.send(embed=embed)
    @slowmode.error
    async def slowmode_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(description="You did not specify how many seconds you wanted to set the slowmode to this channel.\n\n`bash slowmode {seconds}`",color=0x2f3136)
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(description="You don't have permission to do this.",color=0x2f3136)
            await ctx.send(embed=embed)
            return

    @commands.command(aliases=['nick','nn'])
    @commands.has_permissions(manage_nicknames=True)
    async def nickname(self,ctx,member:discord.Member,*,arg):
        embed = discord.Embed(description=f"Changed {member.mention}'s nickname to {arg}",color=0x2f3136)
        embed.set_footer(text=f"Nickname changed by {ctx.author}")
        await ctx.send(embed=embed)
        await member.edit(nick=arg)
    @nickname.error
    async def nickname_error(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            embed = discord.Embed(description="You did not specify the correct arguments.\n\n`bash nickname {user} {nickname}`",color=0x2f3136)
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
            embed = discord.Embed(description="You did not specify an amount of messages you wanted to delete.\n\n`bash purge {amount}`",color=0x2f3136)
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
        else:
            embed = discord.Embed(description="Argument can only be 'true' or 'false'.",color=0x2f3136)
            await ctx.send(embed=embed)
            return
    @channellock.error
    async def channellock_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(description="You don't have the permission to do this.",color=0x2f3136)
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.MissingRequiredArgument):
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
            embed = discord.Embed(description="You did not include a status to set.\n\n`bash changepresence {name}`",color=0x2f3136)
            await ctx.send(embed=embed)
            return
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(description="You don't have the permission to do this.",color=0x2f3136)
            await ctx.send(embed=embed)
            return
            
def setup(client):
    client.add_cog(utilities(client))
