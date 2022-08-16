from discord.ext import commands
import asyncio
import random
import discord
import re

class Br31(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="배라", pass_context=True)
    async def br(self, ctx):
        embed = discord.Embed(title="배스킨라빈스 31", description=":exclamation: 채널 관리 & 역할 관리 권한 필요 :exclamation: ", color=0xFAED7D)
        embed.add_field(name="시작하려면 /시작", value="끝내려면 /종료")
        await ctx.send(embed=embed)
        def check1(res):
            return res.content == '/시작' or res.content == '/종료'
        try:
            res = await self.bot.wait_for('message', timeout=10.0, check=check1)
            if res.content == "/시작":
                embed = discord.Embed(title="배스킨라빈스 31", description="", color=0xFAED7D)
                embed.add_field(name="여기여기 모여라", value="참여하실 분은 10초 안에 아래 감정표현을 눌러주세요")
                message = await ctx.send(embed=embed)
                await message.add_reaction('👍')
                def check2(reaction, user):
                    return user == ctx.author and str(reaction.emoji) == '👍'
                try:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=10.0, check=check2)
                    await asyncio.sleep(10)
                    user_list = []
                    async for i in reaction.users():
                        if (not i.bot):
                            user_list.append(i.name)
                    if len(user_list) < 1:
                        await ctx.send("참여인원이 부족하여 게임을 종료합니다.")
                        return None
                    await ctx.send("참여인원 : %s" %user_list)
                    try:
                        channel = await ctx.guild.create_text_channel('배스킨라빈스')
                        try:
                            async for i in reaction.users():
                                await channel.set_permissions(i, read_messages=True, send_messages=True)
                            embed = discord.Embed(title='입력 규칙 설명', description='입력은 1 2 3과 같이 띄어쓰기로 구분합니다.', color=0xFAED7D)
                            await channel.send(embed=embed)
                            await channel.send("순서를 정합니다.")
                            user_list.append("퓨이린 봇")
                            random.shuffle(user_list)
                            my_str = ""
                            for i in user_list:
                                if i == user_list[-1]:
                                    my_str += i
                                else:
                                    my_str = my_str + i + " -> "
                            await channel.send("%s" %my_str)
                            turn = 0
                            history = 0
                            while True:
                                if user_list[turn % len(user_list)] == '퓨이린 봇':
                                    if history == 28:
                                        how_many = random.randint(1, 2)
                                        ans = ""
                                        if how_many == 1:
                                            ans += str(history + 1)
                                            history += 1; turn += 1
                                            await channel.send(ans)
                                        elif how_many == 2:
                                            ans += str(history + 1) + " " + str(history + 2)
                                            history += 2; turn += 1
                                            await channel.send(ans)
                                    elif history == 29:
                                        await channel.send("30")
                                        history += 1; turn += 1
                                    elif history == 30:
                                        await channel.send("봇이 패배했습니다")
                                        await asyncio.sleep(5)
                                        await channel.delete()
                                        return None
                                    else:
                                        how_many = random.randint(1, 3)
                                        ans = ""
                                        if how_many == 1:
                                            ans += str(history + 1)
                                            history += 1; turn += 1
                                            await channel.send(ans)
                                        elif how_many == 2:
                                            ans += str(history + 1) + " " + str(history + 2)
                                            history += 2; turn += 1
                                            await channel.send(ans)
                                        else:
                                            ans += str(history + 1) + " " + str(history + 2) + " " + str(history + 3)
                                            history += 3; turn += 1
                                            await channel.send(ans)
                                else:
                                    def check3(message):
                                        return message.author.name == user_list[turn % len(user_list)]
                                    try:
                                        if (history == 30):
                                            await channel.send("%s 님의 패배입니다...." %user_list[turn % len(user_list)])
                                            await asyncio.sleep(5)
                                            await channel.delete()
                                            return None
                                        message = await self.bot.wait_for('message', timeout=20.0, check=check3)
                                        human_ans = re.split(' ', message.content)
                                        if (len(human_ans) > 3 or human_ans[0] != str(history + 1)):
                                            await channel.send("잘못된 입력입니다.")
                                            continue
                                        history += len(human_ans)
                                        turn += 1
                                    except asyncio.TimeoutError:
                                        await channel.send("입력 시간 초과로 %s 님의 패배입니다..." %user_list[turn % len(user_list)])
                                        await asyncio.sleep(5)
                                        await channel.delete()
                                        return None
                        except discord.Forbidden:
                            await ctx.send("역할 관리 권한이 없습니다. 게임을 종료합니다.")
                            await channel.delete()
                            return None
                    except discord.Forbidden:
                        await ctx.send("채널 개설 권한이 없습니다. 게임을 종료합니다.")
                except asyncio.TimeoutError:
                    pass
            else:
                await message.channel.send("게임이 종료되었습니다.")
        except asyncio.TimeoutError:
            pass


async def setup(bot):
    await bot.add_cog(Br31(bot))