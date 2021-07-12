import discord
from discord.ext import commands
from colorama import Fore, Style, init
init()

class events(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'[{Fore.GREEN}{Style.BRIGHT}+{Fore.RESET}] Loaded Events.')

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.id == 854036403158908939: #bots uid
            pass
        else:
            print(f'[{Fore.GREEN}{Style.BRIGHT}+{Fore.RESET}] {message.author}: {message.content}')
        links = ['discord.gg','.gg','gg/']
        for i in links:
            try:
                if message.author.id == 854036403158908939: # bots uid
                    pass
                elif i in message.content.lower():
                    await message.delete()
                    await message.channel.send(embed=discord.Embed(description="no self promoting lol",color=0x2f3136))
                else:
                    pass
            except discord.errors.NotFound: # for some reason this gives out errors?
                pass
        
    @commands.Cog.listener()
    async def on_member_join(self,member):
        print(f'[{Fore.GREEN}{Style.BRIGHT}JOIN{Fore.RESET}] Username: {member}')
        embed = discord.Embed(description=f"welcome, hope u enjoy it here",color=0x2f3136)
        embed.set_author(name=member, icon_url=member.avatar_url)
        channel = self.client.get_channel(854636583064305698)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        print(f'[{Fore.RED}{Style.BRIGHT}LEAVE{Fore.RESET}] Username: {member}')
        embed=discord.Embed(description=f"bye lol you wont be missed",color=0x2f3136)
        embed.set_author(name=member, icon_url=member.avatar_url)
        embed.set_footer(text=f"UID: {member.mention}")
        channel = self.client.get_channel(856212824182620175)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self,message):
        try:
            print(f'[{Fore.RED}{Style.BRIGHT}-{Fore.RESET}] {message.author}: {message.content}')
            embed = discord.Embed(description=message.content,color=0x2f3136)
            embed.set_author(name=message.author, icon_url=message.author.avatar_url)
            embed.set_footer(text=f"Deleted in: #{message.channel.name}")
            channel = self.client.get_channel(856212153147981844)
            await channel.send(embed=embed)
        except discord.errors.HTTPException: # if this is even possible?????
            print(f'[{Fore.RED}{Style.BRIGHT}!{Fore.RESET}] Deleted message is too long.')
            embed = discord.Embed(description="Deleted message is too long.",color=0x2f3136)
            embed.set_author(name=message.author, icon_url=message.author.avatar_url)
            embed.set_footer(text=f"Deleted in: #{message.channel.name}")
            channel = self.client.get_channel(856212153147981844)
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self,messagebefore,messageafter):
        try:
            print(f'[{Fore.YELLOW}{Style.BRIGHT}={Fore.RESET}] {messagebefore.author}\n[{Fore.YELLOW}{Style.BRIGHT}={Fore.RESET}] Content Before Edit: {messagebefore.content}\n[{Fore.YELLOW}{Style.BRIGHT}={Fore.RESET}] Content After Edit: {messageafter.content}')
            embed = discord.Embed(color=0x2f3136)
            embed.add_field(name="Before:", value=messagebefore.content, inline=False)
            embed.add_field(name="After:", value=messageafter.content, inline=False)
            embed.set_author(name=messagebefore.author, icon_url=messagebefore.author.avatar_url)
            embed.set_footer(text=f"Edited in: #{messagebefore.channel.name}")
            channel = self.client.get_channel(856212153147981844)
            await channel.send(embed=embed)
        except discord.errors.HTTPException:
            print(f'[{Fore.RED}{Style.BRIGHT}!{Fore.RESET}] Edited message is too long.')
            embed = discord.Embed(description="Edited message is too long.",color=0x2f3136)
            embed.set_author(name=messagebefore.author, icon_url=messagebefore.author.avatar_url)
            embed.set_footer(text=f"Edited in: #{messagebefore.channel.name}")
            channel = self.client.get_channel(856212153147981844)
            await channel.send(embed=embed)
        links = ['discord.gg','.gg','gg/']
        for i in links:
            try:
                if messageafter.author.id == 854036403158908939: # bots uid
                    pass
                elif i in messageafter.content.lower():
                    await messageafter.delete()
                    await messageafter.channel.send(embed=discord.Embed(description="no self promoting lol",color=0x2f3136))
                else:
                    pass
            except discord.errors.NotFound: # for some reason this gives out errors?
                pass

def setup(client):
    client.add_cog(events(client))
