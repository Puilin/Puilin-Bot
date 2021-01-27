import asyncio
import discord
from discord.ext import commands
import random
import time
import warnings
from datetime import datetime
from pytz import timezone

global daily
daily = []
global timestamp
timestamp = []


class MainCog(commands.Cog):


    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def 뽑기(self, ctx, num1, num2):
        picked = random.randint(int(num1), int(num2))
        await ctx.send('뽑힌 숫자는 : '+str(picked))

    @commands.command(name="골라", pass_context=True)
    async def pick(self, ctx):
        embed = discord.Embed(title="뭘 뽑을지는 봇의 마음", description="", color=0x3DB7CC)
        embed.add_field(name="고를 대상을 입력해주세요", value="(예시) 코카콜라 펩시", inline=False)
        await ctx.send(embed=embed)
        def check_p1(message):
            return message.author == ctx.author
        try:
            message = await self.bot.wait_for("message", timeout=20, check=check_p1)
            list1 = message.content.split(" ")
            embed = discord.Embed(title="뭘 뽑을지는 봇의 마음", description="", color=0x3DB7CC)
            embed.add_field(name="골라야 하는 경우의 수를 입력해주세요", value="(예시) 1", inline=False)
            await ctx.send(embed=embed)
            def check_p2(message):
                return message.content.isdigit() and 1 <= int(message.content) <= len(list1)
            try:
                message = await self.bot.wait_for("message", timeout=20, check=check_p2)
                count = int(message.content)
                bots_choice = random.sample(list1,count)
                await ctx.send("%s" %bots_choice)
            except asyncio.TimeoutError:
                await ctx.send("입력 시간 초과")
        except asyncio.TimeoutError:
            await ctx.send("입력 시간 초과")
            

    @commands.command(name="청소", pass_context=True)
    async def _clear(self, ctx, *, amount=5):
        await ctx.channel.purge(limit=amount)


    @commands.Cog.listener()
    async def on_message(self, message):


        if message.author.bot:
            return None
        if message.content == "/안녕":
            await message.channel.send("안녕하세요.")
        if message.content == "/발":
            await message.channel.send("발이라 부르지 마세요.")
        if message.content == "/나무":
            await message.channel.send("나무를 캡니다.")
            treeHit = 0
            while treeHit < 5:
                treeHit += 1
                await message.channel.send("나무를 %d번 캤습니다" %treeHit)
                time.sleep(1)
            await message.channel.send("나무가 쓰러집니다")
        if message.content == "/패치노트":
            await message.channel.send("https://github.com/Puilin/My-own-code/blob/master/%ED%8C%A8%EC%B9%98%EB%85%B8%ED%8A%B8.md")
        if message.content == "/DN":
            await message.channel.send("남만주")
        if message.content in ['/도움말', '/명령어']:
            embed = discord.Embed(title="명령어 목록", description="", color=0xFFA7A7)
            embed.add_field(name = ":gear: 기본 기능", value = "-" * 50, inline=False)
            embed.add_field(name = "/도움말 or /명령어", value = "명령어 목록을 볼 수 있습니다.", inline=False)
            embed.add_field(name = "/패치노트", value = "패치노트를 확인합니다.", inline=False)
            embed.add_field(name = "/안녕", value = "퓨이린 봇이 인사를 합니다.", inline=False)
            embed.add_field(name = "/청소 (숫자)", value = "(숫자)만큼 지난 채팅을 삭제합니다.", inline=False)
            embed.add_field(name = "/출첵 or /출석체크", value = "출석체크 현황을 확인합니다.", inline=False)
            embed.add_field(name = "/나무", value = "봇이 나무를 캐줍니다.", inline=False)
            embed.add_field(name = "/발", value = "금지된 명령어입니다.", inline=False)
            embed.add_field(name = "/DN", value = "금지된 명령어입니다2", inline=False)
            embed.add_field(name = ":fork_and_knife: 편의 기능", value = "-" * 50, inline=False)
            embed.add_field(name = "/뽑기 (숫자1) (숫자2)", value = "(숫자1)과 (숫자2) 사이의 수를 랜덤으로 고릅니다.", inline=False)
            embed.add_field(name = "/골라", value = "추첨 시스템을 불러옵니다", inline=False)
            embed.add_field(name = "/코로나", value = "코로나19 관련 정보를 제공합니다.", inline=False)
            embed.add_field(name = ":video_game: 게임 관련", value = "-" * 50, inline=False)
            embed.add_field(name = "/롤전적 (닉네임)", value = "(닉네임)의 롤 전적을 검색합니다.", inline=False)
            embed.add_field(name = "/메이플", value = "메이플 편의기능을 제공합니다.", inline=False)
            embed.add_field(name = "/랜덤게임", value = "봇이 제공하는 게임 중 하나를 랜덤으로 불러옵니다.", inline=False)
            embed.add_field(name = "/배라", value = "배스킨라빈스 31 게임을 시작합니다. (채널 관리 & 역할 관리 권한 필요)", inline=False)
            await message.channel.send(embed=embed)
        if message.content in ["/출첵", "/출석체크"]:
            embed = discord.Embed(title="출석체크 현황", description="", color=0xD1B2FF)
            get_list = []
            for i in daily:
                if i in message.guild.members:
                    get_list.append(i.name)
            embed.add_field(name = "출석인원", value = "%d명" %len(get_list), inline=False)
            embed.add_field(name = "출석자 목록", value = "%s" %get_list, inline=False)
            await message.channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if before.channel is None and after.channel is not None:
            if after.channel.name == '일반': # 채널을 이렇게 설정할 수 있다 (없어도 됨)
                fmt = "%Y-%m-%d %H:%M:%S %Z%z"
                KST = datetime.now(timezone('Asia/Seoul'))
                now = KST.strftime(fmt)
                timestamp.append(now[8:10])
                embed = discord.Embed(title = "음성 채널 참여", description = "<#" + str(after.channel.id)+"> 채널에 "+str(member.name)+' 님이 참여하셨습니다.', color = 0x00ff00)
                embed.add_field(name = "시간", value = str(now), inline=False)
                await member.guild.system_channel.send(embed=embed)
                try:
                    if int(timestamp[-1]) - int(timestamp[-2]) != 0: # 날짜가 바뀌면 명단 초기화
                        daily.clear()
                except IndexError:
                    pass
                if not member in daily: #출석체크 명단에 있는지 체크 없으면 출첵
                    daily.append(member)
                    await member.guild.system_channel.send(str(member.name) + " 님 "\
                        + str(now[:10]) + " :white_check_mark: 출석체크 완료")


def setup(bot):
    bot.add_cog(MainCog(bot))
