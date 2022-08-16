import discord
from discord.ext import commands
import csv
import pandas as pd
import random

class Conversation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="대화모드", pass_context=True)
    async def conv_init(self, ctx):
        guild = ctx.guild
        channel = discord.utils.get(guild.text_channels, name="대화")
        if channel == None:
            channel = await ctx.guild.create_text_channel('대화')
            embed = discord.Embed(title="퓨이린 봇과의 대화가 시작되었습니다!", description="", color=0xFFD8D8)
            embed.add_field(name="퓨이린 봇에게 말 가르치기", value="/배워 [할말];[대답]")
            embed.set_footer(text="자세한 사항은 홈페이지를 참고바랍니다.\nhttps://puilinbot.herokuapp.com/command/")
            await channel.send(embed=embed)
        else:
            await ctx.send("이미 채널이 존재해요")
    
    @commands.command(name="배워", pass_context=True)
    async def conv_study(self, ctx, *args):
        if ctx.channel.name == '대화':
            f = open('data.csv','a', newline='', encoding='utf-8')
            wr = csv.writer(f)
            str1 = str(' '.join(args))
            lst1 = str1.split(";")
            try:
                wr.writerow([lst1[0], lst1[1], ctx.guild.id])
                f.close()
                await ctx.send("새로운 말을 배웠어요!")
            except IndexError:
                await ctx.send("대답도 입력해주세요! 질문과 대답은 ;로 구분할 수 있어요")
                f.close()
        else:
            await ctx.send("대화 채널에서 사용해주세요")
    
    @commands.Cog.listener()
    async def on_message(self, message):


        if message.author.bot:
            return None
        if message.channel.name == "대화" and not message.content.startswith("/배워"):
            q = message.content
            csv = pd.read_csv('data.csv', names=['Q','A','server_id'], encoding='utf-8')
            find_row = csv.loc[csv['Q'] == q]
            try:
                find_row = find_row.sample(n=1)
                ans = find_row['A'].tolist()
                await message.channel.send(ans[0])
            except ValueError:
                await message.channel.send("모르는 말이에요...")
            


async def setup(bot):
    await bot.add_cog(Conversation(bot))