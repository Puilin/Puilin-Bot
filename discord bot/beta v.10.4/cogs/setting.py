import discord
from discord.ext import commands
import asyncio

class Setting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="설정", pass_context=True)
    async def toggle(self, ctx):
        embed = discord.Embed(title="퓨이린 봇 설정", description="퓨이린 봇과 관련된 설정을 관리할 수 있습니다.", color=0xCC723D)
        embed.add_field(name="음성 채팅 참여 알림 (🔊)", value="음성 채팅 참여 알림을 끄고 켤 수 있습니다.", inline=False)
        message = await ctx.send(embed=embed)
        await message.add_reaction('🔊')
        def check1(reaction, user):
            return user == ctx.author
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=10.0, check=check1)
            if str(reaction.emoji) == "🔊":
                try:
                    f = open("toggling.txt", 'r')
                    str_list = f.readlines()
                    guild_id = ctx.guild.id
                    original = True
                    idx = -1
                    for i in str_list:
                        lst1 = i.strip('\n').split("=")
                        if lst1[0] == str(guild_id):
                            idx = str_list.index(i)
                            if lst1[1] == "false":
                                original = False
                            f.close()
                            break
                    if original:
                        embed = discord.Embed(title="음성 채팅 참여 알림", description="", color=0xCC723D)
                        embed.add_field(name="현재 상태 : 켜짐", value="끄시겠습니까?", inline=False)
                        message = await ctx.send(embed=embed)
                        await message.add_reaction('✔')
                        await message.add_reaction('❌')
                        def check2(reaction, user):
                            return user == ctx.author
                        try:
                            reaction, user = await self.bot.wait_for('reaction_add', timeout=10.0, check=check2)
                            if str(reaction.emoji) == '✔':
                                f2 = open("toggling.txt", 'w')
                                str_list[idx] = lst1[0] + "=" + "false" + '\n'
                                for j in str_list:
                                    f2.write(j)
                                f2.close()
                                embed = discord.Embed(title="음성 채팅 참여 알림을 껐습니다.", description="", color=0xCC723D)
                                message = await ctx.send(embed=embed)
                            else:
                                return
                        except asyncio.TimeoutError:
                            pass
                    else:
                        embed = discord.Embed(title="음성 채팅 참여 알림", description="", color=0xCC723D)
                        embed.add_field(name="현재 상태 : 꺼짐", value="켜시겠습니까?", inline=False)
                        message = await ctx.send(embed=embed)
                        await message.add_reaction('✔')
                        await message.add_reaction('❌')
                        def check2(reaction, user):
                            return user == ctx.author
                        try:
                            reaction, user = await self.bot.wait_for('reaction_add', timeout=10.0, check=check2)
                            if str(reaction.emoji) == '✔':
                                f2 = open("toggling.txt", 'w')
                                str_list[idx] = lst1[0] + "=" + "true" + "\n"
                                for j in str_list:
                                    f2.write(j)
                                f2.close()
                                embed = discord.Embed(title="음성 채팅 참여 알림을 켰습니다.", description="", color=0xCC723D)
                                message = await ctx.send(embed=embed)
                            else:
                                return
                        except asyncio.TimeoutError:
                            pass
                except FileNotFoundError:
                    guild_list = self.bot.guilds
                    f = open("toggling.txt", 'w')
                    for i in guild_list:
                        f.write(str(i.id) + "=true" + "\n")
                    f.close()
                    Setting.toggle(self, ctx)
            else:
                return
        except asyncio.TimeoutError:
            pass

def setup(bot):
    bot.add_cog(Setting(bot))
