import discord, asyncio, random, asyncio, datetime
from discord.ext import commands
from colorama import Fore, Style, init
init()

class usercommands(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.snipe = {}

    @commands.Cog.listener()
    async def on_connect(self):
        print(f'[{Fore.GREEN}{Style.BRIGHT}+{Fore.RESET}] Loaded User Commands.')
    
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        self.snipe[message.channel.id] = message

    @commands.command()
    async def snipe(self, ctx):
        snipe = self.snipe[ctx.channel.id]
        try:
            embed = discord.Embed(description=snipe.content, color=0x2f3136)
            embed.set_author(name=snipe.author, icon_url=snipe.author.avatar_url)
            embed.timestamp = snipe.created_at
            await ctx.send(embed=embed)
        except:
            await ctx.send(embed=discord.Embed(description="There is nothing to snipe.", color=0x2f3136))

    @commands.command()
    async def stealcookie(self,ctx, member:discord.Member):
        cookies = ['_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_62657D96A5E6A2390541FB63C076300EE640117D6BF641F536C998A790E49A3E5319BDC737A6C70519EF809EA7D11CA11D3ADC37A4006D4C747FA061FAD0EB976FCAA5A7C74024CFB7774C7F64721211F4C14739196E06391A343C7559343A81CAA9D62AB224A8B7A0DF61627391F95858307C44980371C9B6D9C48F6222370348F61E6B730A6F22175460793F79D915BC6BE06E02F92347C24B6468833B81C6ABACAA3586C3DFBA7436BAFE6A8AD5C8CACD0D7C6EC805773A888445C9B4C0D0CDEEF772886D465B33CFC2DE2CB35313D558AB8B44ADC5FBFE9DE178040F0BF30D7C30AE87AA3AA617E8A9CF348756D8EADDDD9A4FD1EE2C46EEEDA0C633CBED682536B7BA3B3F14AF6E4C2A58BB712507EA91F605C2CA5CCF91B75DE6072E941C98346085EF37E48770503139F759628C6DE648','_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_6B96E6855F8E44CE0759A6B2468A9EF0E3E42DB833B5B3E77146947CFEB420C116D86C75A6DB67ADB39DBD0D31FDB805160E9A074022FCA7898D6FFE61B0DF6609F169956413B8E0CE0A12A638C5579ED67B861BDF0763BA263DBC410ED657C760785D7F282B2772E066123959C9EB5A9C336D7207553AE8E908C09CEA01302611CBE1F4981CBF9714C71998121C4154FE4BB9CD9FA2770C8882AA76694F497A40A3EFB8AFC67DE5D3C61E0921F5F66E0FBA91D0264F6456DDC811043245736FB015AEB880C5D45665DEA54A403CF110123683FDE267B8B1B797F2ABBF82D764ED182676B45AB5147C187007EF80F924C63127661EB55FB530FC0BBB6831350B17464D7B0AC65E0E60C8CC1C09CCAB33E3FC44B0E0A9BE186D25B74E5BD3B3F3FBF2755A3D4A53E4CF8749B5D8104F30E0260073''_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_B34CA36CED3A50AA2F66A854396E5F87D9BA128CD98CC6DBD4B4DF6B0BA5B0CC6D8E94FFF3C4BE222F5B7D444370859617671DD88F4172DCB2F5AC6493ABB9075768B53F05C54E424EC28BFFC0DD57F9953CA8AED14A4BA12CB86CDD62953E0E769B266C1F5C569C3FC968A036FB7C9722FAD69ADACDE18EB122385662BC76A0BB5DBE61A189011CC9748A4877B28FFFDA80DF58759C4F95FF75101C29FAA32CB14F6D1349752FCE5DE769D8BAA3E8DFFD5838C9E7B19C8EB5FDF76F465E55AA8C3065F1A51CAE14BDAC78B3CCE1C6D531FB0E24775FF8491C38A3D9BCDD6534A283E3FBDA559A1DFA5A704A79EB6E4FCD6FEB65F876A50B84505E75E8A1497379D21570DC4C103387F3EA90EA8AA177057692E7','_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_37C1D9865B019C90EB60FFFEE0B59D65300511530EC5202E3D873E3A0CC0AEE5543632199B11FBFCBA2CAA96AB514474DD6FDC44B4D30AD4F88C8EC41928176C18FC211841AD0828031B68DDB78375829D84A625E5B78E9654D157DF3C73A4C46669786A8585B3D6D2BEFA2492601E27F208DD008168C8078B1F2F30A6E0E5CCA12CBE8DE076CB1D20416F07346CB1A697DD917E0338263350D9EA8CBEA490A19E86CE3CF0BA360AFEB7E96C48418BEBC5021A151348E153746148139D52A0D80EC079D627E7D632AB3587C2C92634308F8A1179C00D323344CD26D546C67471DC907F1AF186879905C713B9B113C0EFFB3DD7A28CE80D692FD8B0DD88BCFF62C1C66A091BDC26DF929370A8890EAEE06207D06A87AFFED626961EBA3396073EEF34132C18E41FD158090D29393089A38E5F5FF9','_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_FA3C52FA4B7F685981D684F04F5F22B28AE69E2157B72FD7F212FD4BAA320E752E2202A62775FE6CE385CB0560962F472677E3E71846E387673E027E7C6557796ECE3E271C4A0C425110A39A672388BCCAEEC59DBF214BA85C8C60697F3CE0FBD44D1A24CB7EACC8EBF7ADD8913C85C2889B694A2036D3419645AC02F5C26C2F5D34690AB31BEBE2C4418D704EA3B1693C59D865294B88647C81FB47B64DE3FAF81DB1A920B5148CFF85B928CC8C10C615DE3E1A11EF80EA3857713F2D2FBA80193552BE2B8E29057D7AAFBF61C6B19E83E586735586DBF7418804CAF708DA3C659A703E67BEAE26B6EEDF3440F851BD43D7807915A10AE44C4CA28E325E7D578AF44F35F1CA1C1E86361E3878A8E6728995292593EEB9F27A98600F8CB5C2472E106CA11CA3FFD20B7C2707B94088A31D7190C']
        embed = discord.Embed(description=f"Stealing {member}'s cookie..",color=0x2f3136)
        await ctx.send(embed=embed)
        await asyncio.sleep(2)
        embed = discord.Embed(description="Cookie has been stolen.. Waiting for authorization..",color=0x2f3136)
        await ctx.send(embed=embed)
        await asyncio.sleep(2)
        embed2 = discord.Embed(title=f"Success. {member}'s .ROBLOSECURITY Cookie is below.", description=f"```{random.choice(cookies)}```",color=0x2f3136)
        await ctx.send(embed=embed2)
    @stealcookie.error
    async def stealcookie_error(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            embed = discord.Embed(description="You did not mention a user.\n\n`bash stealcookie {user}`",color=0x2f3136)
            await ctx.send(embed=embed)
            return

    @commands.command()
    async def stealtoken(self,ctx,member:discord.Member):
        tokens = ['NDc5MzMzMzc5Njc0OTk2NzQ2.DlYF_w.QpvT7z0m4ThKoezf5zbe2fIPWV8','NDc5MzYwMTgzNTYzMTkwMjcz.DlYGmQ.3MlAyGKs5-7_e7CPMflmUe87r_E','NDc5MzYwNDc1OTY1MDMwNDMx.DlYG-w.yXWMKlalIt87Mz673elIFprWbnY','NDc5MzYwNzUyMTA1MjkxNzc3.DlYHWbash hOqxEiLGhnFyqd4Jas-BxP-MLJs','NDc5MzYxMTA3MTA3MTE5MTA1.DlYHoA.t5LtubIhbUWoi0wv4hY5c-Eqg1w','NDc5MzYxNDAyMTQ2OTE0MzA0.DlYH5A.Bm12AOLHbY2hEINnj4nEtGEdsh8','NDc5MzYxNzAwMDQzNDIzNzg1.DlYIPQ.xkjX_ai7tCq4shEVNPQfqTKWreQ']
        embed = discord.Embed(description=f"Stealing {member}'s Discord token..",color=0x2f3136)
        await ctx.send(embed=embed)
        await asyncio.sleep(2)
        embed = discord.Embed(description="Token has been stolen.. Checking through Discord's API.",color=0x2f3136)
        await ctx.send(embed=embed)
        await asyncio.sleep(2)
        embed2 = discord.Embed(title=f"Success. {member}'s Discord token is below.", description=f"```{random.choice(tokens)}```",color=0x2f3136)
        await ctx.send(embed=embed2)
    @stealtoken.error
    async def stealtoken_error(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            embed = discord.Embed(description="You did not mention a user.\n\n`bash stealtoken {user}`",color=0x2f3136)
            await ctx.send(embed=embed)
            return

    @commands.command()
    async def plzsendcodelikethis(self,ctx):
        embed = discord.Embed(description="plz send ur code like this it looks autistic without it",color=0x2f3136)
        embed.set_image(url="https://cdn.hentaihaven.dev/onionsiteishot/fbisfatcock/skidnigger/Discord_x50mpifBtW.png")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(usercommands(client))