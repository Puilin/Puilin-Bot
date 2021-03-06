import asyncio
import discord
from discord.ext import commands


class Maple(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="메이플", pass_context=True)
    async def maple(self, ctx):
        embed = discord.Embed(title="메이플 편의기능", description="", color=0xFAE0D4)
        embed.add_field(name="추옵  (\u2694)" ,value="무기의 추가옵션을 봅니다.", inline=False)
        embed.add_field(name="코강  (💎)" ,value="전직업 코어강화 정리", inline=False)
        embed.add_field(name="심볼  (❄)" ,value="심볼 강화 비용 계산", inline=False)
        message = await ctx.send(embed=embed)

        for i in ["\u2694", "💎", "❄"]:
            await message.add_reaction(i)

        def check_m1(reaction, user):
            return user == ctx.author
        try:
            reaction, user = await self.bot.wait_for("reaction_add", timeout=10, check=check_m1)
            if str(reaction.emoji) == "\u2694":
                embed = discord.Embed(title="추옵", description="", color=0xFAE0D4)
                embed.add_field(name="파프니르  (🕐)" ,value="150제", inline=False)
                embed.add_field(name="앱솔랩스  (🕑)" ,value="160제", inline=False)
                embed.add_field(name="아케인셰이드  (🕒)" ,value="200제", inline=False)
                message = await ctx.send(embed=embed)

                await message.add_reaction('🕐')
                await message.add_reaction('🕑')
                await message.add_reaction('🕒')
                
                def check_m2(reaction, user):
                    return user == ctx.author
                try:
                    reaction, user = await self.bot.wait_for("reaction_add", timeout=10, check=check_m2)
                    if str(reaction.emoji) == '🕐':
                        embed = discord.Embed()
                        embed.set_image(url='https://blogfiles.pstatic.net/MjAyMTAxMjRfMTEg/MDAxNjExNDY5MzQzMTkx.C3QlTLCdH3f5KP_VuT4ShyuUceYj25pnYn1-K9B7EhUg.rfTfooOTVD69l_GN-M7GjeFcwyKVWbpwkyBfm_0y4Tsg.PNG.suryblue/1.PNG?type=w1')
                        embed.set_footer(text='출처 : https://godgle.tistory.com')
                        await ctx.send(embed=embed)
                    elif str(reaction.emoji) == '🕑':
                        embed = discord.Embed()
                        embed.set_image(url='https://blogfiles.pstatic.net/MjAyMTAxMjRfMTEg/MDAxNjExNDY5MzQzNTMw.BHsk2vNgQFScFnb14d6ptphjrlhTQbOE-UzJsvCr4N4g.FAKheOcWlKjiGSjME6t1c4vI5oyamYilfojWsooJMuMg.PNG.suryblue/2.PNG?type=w1')
                        embed.set_footer(text='출처 : https://godgle.tistory.com/')
                        await ctx.send(embed=embed)
                    elif str(reaction.emoji) == '🕒':
                        embed = discord.Embed()
                        embed.set_image(url='https://blogfiles.pstatic.net/MjAyMTAxMjRfOTIg/MDAxNjExNDY5MzQzNzU3.ESKfnUxxOK24xNg8HtT-nMOXHMjsJOg42RGLOaHAjL8g.OqPRpFhmSHpTzk9i3mvo512JlIr6MMoC0oO4Gf_EMxgg.PNG.suryblue/3.PNG?type=w1')
                        embed.set_footer(text='출처 : https://godgle.tistory.com/')
                        await ctx.send(embed=embed)
                except asyncio.TimeoutError:
                    await ctx.send("입력 시간 초과")
            elif str(reaction.emoji) == '💎':
                await ctx.send("http://www.inven.co.kr/board/maple/2304/22970")
            elif str(reaction.emoji) == '❄':
                embed = discord.Embed(title="심볼", description="", color=0xFAE0D4)
                embed.add_field(name="소멸의 여로  (🕐)" ,value="lv.200", inline=False)
                embed.add_field(name="츄츄~에스페라  (🕑)" ,value="lv.210~235", inline=False)
                message = await ctx.send(embed=embed)

                for i in ['🕐', '🕑']:
                    await message.add_reaction(i)
                
                def check_m3(reaction, user):
                    return user == ctx.author
                try:
                    reaction, user = await self.bot.wait_for("reaction_add", timeout=10, check=check_m3)
                    if str(reaction.emoji) == '🕐':
                        def check_m4(message):
                            return message.author == ctx.author and message.content.isdigit() and 1<=int(message.content)<=20
                        try:
                            await ctx.send("현재 심볼 레벨을 입력해 주세요 (1~20)")
                            message = await self.bot.wait_for("message", timeout=20, check=check_m4)
                            if int(message.content) == 20:
                                await ctx.send("최대 레벨입니다.")
                                return None
                            meso = 2370000 + int(message.content) * 7130000
                            growth = int(message.content)**2 + 11
                            await ctx.send("필요 성장치 : %d\n강화 비용 : %d 메소" %(growth,meso))
                        except asyncio.TimeoutError:
                            await ctx.send("입력 시간 초과")
                    elif str(reaction.emoji) == '🕑':
                        def check_m5(message):
                            return message.author == ctx.author and message.content.isdigit() and 1<=int(message.content)<=20
                        try:
                            await ctx.send("현재 심볼 레벨을 입력해 주세요 (1~20)")
                            message = await self.bot.wait_for("message", timeout=20, check=check_m5)
                            if int(message.content) == 20:
                                await ctx.send("최대 레벨입니다.")
                                return None
                            meso = 12440000 + int(message.content) * 6600000
                            growth = int(message.content)**2 + 11
                            await ctx.send("필요 성장치 : %d\n강화 비용 : %d 메소" %(growth,meso))
                        except asyncio.TimeoutError:
                            await ctx.send("입력 시간 초과")
                except asyncio.TimeoutError:
                    await ctx.send("입력 시간 초과")
                            
                        
                
        except asyncio.TimeoutError:
            await ctx.send("입력 시간 초과")

def setup(bot):
    bot.add_cog(Maple(bot))
