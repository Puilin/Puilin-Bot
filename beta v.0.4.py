import asyncio
import discord
from discord.ext import commands
import random
from urllib.request import urlopen, Request
import urllib
import urllib.request
import bs4
from time import sleep

app = commands.Bot(command_prefix='/')

token = "NjkyMDM3MDYxNDE0MzU1MDA0.XnosGA.BL_uBWubT1-HW0SaJwAuAuFNbus"

@app.command(pass_context=True)
async def 뽑기(ctx, num1, num2):
    picked = random.randint(int(num1), int(num2))
    await ctx.send('뽑힌 숫자는 : '+str(picked))

@app.command(name="청소", pass_context=True)
async def _clear(ctx, *, amount=5):
    await ctx.channel.purge(limit=amount)

@app.event
async def on_ready():
    print("등장 : ")
    print(app.user.name)
    print(app.user.id)
    print("==========")
    game = discord.Game("퓨이린 봇 가동")
    await app.change_presence(status=discord.Status.online, activity=game)

#discord.Game : 게임하는중
#discord.Streaming : 방송하는중
#discord.Activity : 봇이 활동하는 중
#Status : online, offline, idle, dnd(DO NOT DISTURB)

@app.event
async def on_message(message):

    
    await app.process_commands(message)
    if message.author.bot:
        return None
    if message.content == '/북':
        await message.channel.send("따닥")
    if message.content == "/안녕":
        await message.channel.send("안녕하세요.")
    if message.content == "/발":
        await message.channel.send("발이라 부르지 마세요.")
    if message.content == "/동숲":
        for i in range(1, 11):
            await message.channel.send("와 동숲 재밌겠다")
            sleep(0.5)
    if message.content == "/나무":
        await message.channel.send("나무를 캡니다.")
        treeHit = 0
        while treeHit < 5:
            treeHit += 1
            await message.channel.send("나무를 %d번 캤습니다" %treeHit)
            sleep(1)
        await message.channel.send("나무가 쓰러집니다")
    if message.content == "/DN":
        await message.channel.send("남만주")
    #if message.content.startswith("/롤2"):
     #   learn = message.content.split(" ")
      #  location = learn[1]
       # enc_location = urllib.parse.quote(location)

#        url = "http://www.op.gg/summoner/userName=" + enc_location
 #       html = urllib.request.urlopen(url)

  #      bsObj = bs4.BeautifulSoup(html, "html.parser")
   #     rank1 = bsObj.find("div", {"class": "TierRankInfo"})
    #    rank2 = rank1.find("div", {"class": "TierRank"})
     #   rank3 = rank2.find("span", {"class": "tierRank"})
      #  print(rank2)
       # if rank2 != 'Unranked':
        #    jumsu1 = rank1.find("div", {"class": "TierInfo"})
         #   jumsu2 = jumsu1.find("span", {"class": "LeaguePoints"})
          #  jumsu3 = jumsu2.text
           # jumsu4 = jumsu3.strip()#점수표시 (11LP등등)
            #print(jumsu4)

#            winlose1 = jumsu1.find("span", {"class": "WinLose"})
 #           winlose2 = winlose1.find("span", {"class": "wins"})
  #          winlose2_1 = winlose1.find("span", {"class": "losses"})
   #         winlose2_2 = winlose1.find("span", {"class": "winratio"})
#
 #           winlose2txt = winlose2.text
  #          winlose2_1txt = winlose2_1.text
   #         winlose2_2txt = winlose2_2.text #승,패,승률 나타냄  200W 150L Win Ratio 55% 등등
#
 #           print(winlose2txt + " " + winlose2_1txt + " " + winlose2_2txt)
#
 #       channel = message.channel
  #      embed = discord.Embed(
   #         title='롤 정보',
    #        description='롤 정보입니다.',
     #       colour=discord.Colour.green()
      #  )
       # if rank2=='Unranked':
        #    embed.add_field(name='당신의 티어', value=rank2, inline=False)
         #   embed.add_field(name='-당신은 언랭-', value="언랭은 더이상의 정보는 제공하지 않습니다.", inline=False)
          #  await channel.send(channel, embed=embed)
        #else:
         #   embed.add_field(name='당신의 티어', value=rank2, inline=False)
          #  embed.add_field(name='당신의 LP(점수)', value=jumsu4, inline=False)
           # embed.add_field(name='당신의 승,패 정보', value=winlose2txt+" "+winlose2_1txt, inline=False)
            #embed.add_field(name='당신의 승률', value=winlose2_2txt, inline=False)
          #  await channel.send(channel, embed=embed)
    if message.content == '/도움말':
        await message.channel.send("""/안녕 : 퓨이린 봇이 인사를 합니다
/발 : 금지된 명령어입니다.
/DN : 금지된 명령어입니다2
/나무 : 봇이 나무를 캐줍니다.
/도움말 : 도움말을 볼 수 있습니다.
/동숲 : 너만 동숲이 없습니다.
/북 : 따닥
/롤 (닉네임) : (닉네임)의 롤 전적을 검색합니다. (op.gg) [언랭 검색 안됨]
/뽑기 (숫자1) (숫자2) : (숫자1)과 (숫자2) 사이의 수를 랜덤으로 고릅니다.
/청소 (숫자) : (숫자)만큼 지난 채팅을 삭제합니다.""")
            
app.run(token)
