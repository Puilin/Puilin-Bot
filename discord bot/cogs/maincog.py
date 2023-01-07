import asyncio
from sqlite3 import Time
import discord
from discord.ext import commands
import random
from datetime import datetime
from pytz import timezone
from discord import app_commands
import os
import pymongo

timestamp = []
            
client = pymongo.MongoClient("your string here")
db_point = client.point
db_daily = client.daily

class MainCog(commands.Cog):


    def __init__(self, bot):
        self.bot = bot
    
    def check_toggles(self, guild):
        f = open('toggling.txt', 'r')
        str_list = f.readlines()
        for i in str_list:
            line = i.strip('\n').split('=')
            if line[0] == str(guild.id):
                if line[1] == 'true':
                    return True
                else:
                    return False
        return False
    
    @commands.command(pass_context=True)
    async def 뽑기(self, ctx, num1, num2):
        picked = random.randint(int(num1), int(num2))
        await ctx.send('뽑힌 숫자는 : '+str(picked))

    @app_commands.command(name="피망", description="퓨이린 봇에게 피망을 줍니다. 매일 한 개씩 주도록 합시다.")
    async def pimang(self, interaction :discord.Interaction):
        response = [
            "으악...",
            "저한테 왜이러세요.. 8ㅁ8",
            "초록괴물이다!!!",
            "시러어어어",
            "너무해ㅐ.."
        ]
        await interaction.response.send_message("%s" %random.sample(response, 1)[0])
    
    @app_commands.command(name="골라", description="뭘 고를지 망설여지시나요? 봇이 뽑아드립니다!")
    async def pick(self, inter :discord.Interaction):
        ctx = await commands.Context.from_interaction(inter)
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

    @app_commands.command(name="골라_", description="경우의 수가 2가지인 경우. /골라의 약식 명령어")
    @app_commands.describe(대상1="봇이 고를 대상1", 대상2="봇이 고를 대상2")
    async def pick_simple(self, interaction :discord.Interaction, 대상1 :str, 대상2 :str):
        list1 = []
        list1.append(대상1)
        list1.append(대상2)
        bots_choice = random.sample(list1,1)
        await interaction.response.send_message("{}, {} 중에서 저는 {}를 고르겠어요!".format(대상1, 대상2, bots_choice))

    @app_commands.command(name="청소", description="채널의 메시지를 삭제합니다.")
    @app_commands.checks.bot_has_permissions(manage_messages=True)
    async def _clear(self, interaction: discord.Interaction, amount:int):
        ctx = await commands.Context.from_interaction(interaction)
        try:
            await ctx.channel.purge(limit=amount)
            await interaction.response.send_message(content="청소가 완료되었습니다.", ephemeral=True)
        except discord.app_commands.MissingPermissions:
            await ctx.send("메시지 관리 권한이 없습니다.")
    
    @app_commands.command(name="포인트", description="현재 가지고 있는 포인트를 조회합니다.")
    async def show_point(self, interaction: discord.Interaction):
        server_id = interaction.user.guild.id
        entry = db_point[str(server_id)].find_one({'id':str(interaction.user.id)})
        embed = discord.Embed(title="포인트 조회", description="", color=0xCAA232)
        if entry is None:
            embed.add_field(name=f"{interaction.user.name}", value="0 Pt")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        embed.add_field(name=f"{interaction.user.name}", value=f"{entry['points']} Pt", inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    
    @app_commands.command(name="팀매칭1", description="선택한 멤버들로 여러 팀을 구성합니다. (10명 이하인 경우)")
    async def matching(self, interaction: discord.Interaction, member1: discord.Member, member2: discord.Member = None,\
        member3: discord.Member = None, member4: discord.Member = None, member5: discord.Member = None,\
            member6: discord.Member = None, member7: discord.Member = None, member8: discord.Member = None,\
                member9: discord.Member = None, member10: discord.Member = None):
        ctx = await commands.Context.from_interaction(interaction)
        await ctx.send("구성할 팀의 개수를 입력하세요.")
        def check(message):
            return message.content.isdigit()
        members = [member1, member2, member3, member4, member5, member6, member7, member8, member9, member10]
        for member in members.copy():
            if member == None:
                members.remove(member)
        try:
            while True:
                message = await self.bot.wait_for('message', timeout=10, check=check)
                team_count = int(message.content)
                if team_count > len(members):
                    await ctx.send("멤버의 수보다 팀의 개수가 많습니다. 다시 입력해주세요")
                    continue
                elif team_count <= 0:
                    await ctx.send("1 이상의 수를 입력해주세요.")
                    continue
                else:
                    break
            alloc = [0 for _ in range(team_count)]
            for i in range(len(members)):
                alloc[i % team_count] += 1
            matched = []
            for j in alloc:
                chosen = random.sample(members, j)
                matched.append(chosen)
                members = list(set(members) - set(chosen))
            embed = discord.Embed(title="팀 매칭 결과", color=0xCCCCFF)
            index = 1
            for team in matched:
                output = []
                printing = ""
                for member in team:
                    output.append(member.name)
                    printing += member.name + "\n"
                embed.add_field(name="team " + str(index), value=printing)
                index += 1
            await ctx.send(embed=embed)
        except asyncio.TimeoutError:
            ctx.send("입력 시간 초과로 팀매칭 시스템을 종료합니다.")

    @app_commands.command(name="팀매칭2", description="감정표현에 참여한 멤버들로 여러 팀을 구성합니다. (인원 제한 없음)")
    async def matching2(self, interaction: discord.Interaction):
        ctx = await commands.Context.from_interaction(interaction)
        embed = discord.Embed(title="팀 매칭 시스템", description="팀 짤 사람 10초 안에 모여라!", color=0xCCCCFF)
        message = await ctx.send(embed=embed)
        await message.add_reaction('👍')
        def check1(reaction, user):
            return str(reaction.emoji) == '👍'
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=10.0, check=check1)
            for sec in range(10, -1, -1):
                embed = discord.Embed(title="팀 매칭 시스템", description="팀 짤 사람 {}초 안에 모여라!".format(sec), color=0xCCCCFF)
                await asyncio.sleep(1.0)
                await message.edit(embed=embed)
            members = []
            async for i in reaction.users():
                if (not i.bot):
                    members.append(i.name)
            def check2(message):
                return message.content.isdigit()
            await ctx.send("구성할 팀의 개수를 입력하세요.")
            try:
                while True:
                    message = await self.bot.wait_for('message', timeout=10, check=check2)
                    team_count = int(message.content)
                    if team_count > len(members):
                        await ctx.send("멤버의 수보다 팀의 개수가 많습니다. 다시 입력해주세요")
                        continue
                    elif team_count <= 0:
                        await ctx.send("1 이상의 수를 입력해주세요")
                        continue
                    else:
                        break
                alloc = [0 for _ in range(team_count)]
                for i in range(len(members)):
                    alloc[i % team_count] += 1
                matched = []
                for j in alloc:
                    chosen = random.sample(members, j)
                    matched.append(chosen)
                    members = list(set(members) - set(chosen))
                embed = discord.Embed(title="팀 매칭 결과", color=0xCCCCFF)
                index = 1
                for team in matched:
                    output = []
                    printing = ""
                    for member in team:
                        output.append(member)
                        printing += member + "\n"
                    embed.add_field(name="team " + str(index), value=printing)
                    index += 1
                await ctx.send(embed=embed)
            except asyncio.TimeoutError:
                await ctx.send("입력 시간 초과로 팀매칭 시스템을 종료합니다.")
        except asyncio.TimeoutError:
            await message.clear_reactions()
            await ctx.send("아무도 팀을 짜고 싶지 않나봐요..")


    @commands.Cog.listener()
    async def on_message(self, message):


        if message.author.bot:
            return None
        if message.content == "/패치노트":
            await message.channel.send("https://github.com/Puilin/My-own-code/blob/master/%ED%8C%A8%EC%B9%98%EB%85%B8%ED%8A%B8.md")
        if message.content == "/DN":
            await message.channel.send("남만주")
        if message.content in ['/도움말', '/명령어']:
            embed = discord.Embed(title="명령어 목록", description="", color=0xFFA7A7)
            embed.add_field(name = ":gear: 기본 기능", value = "-" * 50, inline=False)
            embed.add_field(name = "/도움말 or /명령어", value = "명령어 목록을 볼 수 있습니다.", inline=False)
            embed.add_field(name = "/패치노트", value = "패치노트를 확인합니다.", inline=False)
            embed.add_field(name = "/청소 (숫자)", value = "(숫자)만큼 지난 채팅을 삭제합니다.", inline=False)
            embed.add_field(name = "/출첵 or /출석체크", value = "출석체크 현황을 확인합니다.", inline=False)
            embed.add_field(name = "/피망", value = "퓨이린 봇에게 피망을 줄 수 있습니다. 매일 하나씩 주도록 합시다.", inline=False)
            embed.add_field(name = "/발", value = "금지된 명령어입니다.", inline=False)
            embed.add_field(name = "/DN", value = "금지된 명령어입니다2", inline=False)
            embed.add_field(name = ":fork_and_knife: 편의 기능", value = "-" * 50, inline=False)
            embed.add_field(name = "/뽑기 (숫자1) (숫자2)", value = "(숫자1)과 (숫자2) 사이의 수를 랜덤으로 고릅니다.", inline=False)
            embed.add_field(name = "/골라", value = "추첨 시스템을 불러옵니다", inline=False)
            embed.add_field(name = "/코로나", value = "코로나19 관련 정보를 제공합니다.", inline=False)
            embed.add_field(name = "/날씨", value = "날씨 정보를 제공합니다.", inline=False)
            embed.add_field(name = ":video_game: 게임 관련", value = "-" * 50, inline=False)
            embed.add_field(name = "/롤전적 (닉네임)", value = "(닉네임)의 롤 전적을 검색합니다.", inline=False)
            embed.add_field(name = "/메이플", value = "메이플 편의기능을 제공합니다.", inline=False)
            embed.add_field(name = "/랜덤게임", value = "봇이 제공하는 게임 중 하나를 랜덤으로 불러옵니다.", inline=False)
            embed.add_field(name = "/배라", value = "배스킨라빈스 31 게임을 시작합니다. (채널 관리 & 역할 관리 권한 필요)", inline=False)
            embed.add_field(name = ":hammer_pick: 강화(인챈트)", value = "-" * 50, inline=False)
            embed.add_field(name = "/강화 (멤버이름)", value = "해당 멤버를 인챈트합니다.", inline=False)
            embed.add_field(name = "/강화현황 (멤버이름)", value = "해당 멤버의 인챈트 단계를 확인합니다.", inline=False)
            embed.add_field(name = "/강화랭킹", value = "강화 랭킹을 조회합니다.", inline=False)
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
        # if MainCog.check_toggles(self, member.guild):
            if before.channel is None and after.channel is not None and not member.bot:
                # if after.channel.name == '일반': # 채널을 이렇게 설정할 수 있다 (없어도 됨)
                server_id = member.guild.id
                fmt = "%Y-%m-%d %H:%M:%S %Z%z"
                KST = datetime.now(timezone('Asia/Seoul'))
                now = KST.strftime(fmt)
                timestamp.append(now[8:10])
                embed = discord.Embed(title = "음성 채널 참여", description = "<#" + str(after.channel.id)+"> 채널에 "+str(member.name)+' 님이 참여하셨습니다.', color = 0x00ff00)
                embed.add_field(name = "시간", value = str(now), inline=False)
                await member.guild.system_channel.send(embed=embed)
                try:
                    if int(timestamp[-1]) - int(timestamp[-2]) != 0: # 날짜가 바뀌면 명단 초기화
                        db_daily[str(server_id)].drop()
                except IndexError:
                    pass
                entry = db_daily[str(server_id)].find_one({'id': str(member.id)})
                if entry is None:
                    db_daily[str(server_id)].insert_one({
                        'id': str(member.id),
                        'name' : member.name,
                        'date' : datetime.utcnow()
                    })
                    await member.guild.system_channel.send(str(member.name) + " 님 "\
                        + str(now[:10]) + " :white_check_mark: 출석체크 완료 (+100 Pt)")
                    entry = db_point[str(server_id)].find_one({'id':str(member.id)})
                    if entry is None:
                        db_point[str(server_id)].insert_one({
                            'id': str(member.id),
                            'name': member.name,
                            'points': 0
                        })
                    db_point[str(server_id)].update_one({'id': str(member.id)}, {'$inc': {'points':100}})


async def setup(bot):
    maincog = MainCog(bot)
    await bot.add_cog(maincog)
    try:
        bot.tree.add_command(maincog.pick)
        bot.tree.add_command(maincog.pick_simple)
        bot.tree.add_command(maincog._clear)
        bot.tree.add_command(maincog.pimang)
        bot.tree.add_command(maincog.matching)
        bot.tree.add_command(maincog.matching2)
        bot.tree.add_command(maincog.show_point)
    except app_commands.CommandAlreadyRegistered:
        pass