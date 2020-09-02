import asyncio
import discord
from discord.ext import commands
import random
from urllib.request import urlopen, Request, URLError, HTTPError
import urllib
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import quote
import time
import warnings
import re
import os
from datetime import datetime
from pytz import timezone
from cardgame import *

app = commands.Bot(command_prefix='/')

token = "Your token here"

tierScore = {
    'default' : 0,
    'iron' : 1,
    'bronze' : 2,
    'silver' : 3,
    'gold' : 4,
    'platinum' : 5,
    'diamond' : 6,
    'master' : 7,
    'grandmaster' : 8,
    'challenger' : 9
}

def tierCompare(solorank,flexrank):
    if tierScore[solorank] > tierScore[flexrank]:
        return 0
    elif tierScore[solorank] < tierScore[flexrank]:
        return 1
    else:
        return 2
warnings.filterwarnings(action='ignore')
opggsummonersearch = 'https://www.op.gg/summoner/userName='

def deleteTags(htmls):
    for a in range(len(htmls)):
        htmls[a] = re.sub('<.+?>','',str(htmls[a]),0).strip()
    return htmls


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
    game = discord.Game("퓨이린 봇 개발모드")
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
    if message.content == "/랜덤게임":
        game_list = ["가위바위보", "끝말잇기", "블랙잭"]
        sample = random.sample(game_list, 1)
        await message.channel.send("뽑힌 게임은 %s입니다." %sample)
        if sample[0] == "가위바위보":
            embed = discord.Embed(title="가위바위보!", description="", color=0x5CD1E5)
            embed.add_field(name="퓨이린의 랜덤게임" ,value="시작하려면 /시작\n끝내려면 /종료", inline=False)
            await message.channel.send(embed=embed)
            def check(res):
                return res.content == '/시작' or res.content == '/종료'
            try:
                res = await app.wait_for('message', timeout=10.0, check=check)
                if res.content == '/시작':
                    await message.channel.send("가위, 바위, 보 중에 고르세요! 제한시간은 10초입니다!")
                    def check2(res2):
                        return res2.content == '가위' or res2.content == '바위' or res2.content == '보'
                    try:
                        res2 = await app.wait_for('message', timeout=10.0, check=check2)
                        bots_list = ['가위', '바위', '보']
                        bots_choice = random.sample(bots_list,1)
                        if res2.content == '가위':
                            if bots_choice[0] == '가위':
                                await message.channel.send("비겼습니다. 봇의 선택 : %s" %(bots_choice[0]))
                            elif bots_choice[0] == '바위':
                                await message.channel.send("졌습니다... 봇의 선택 : %s" %(bots_choice[0]))
                            else:
                                await message.channel.send("이겼습니다! 봇의 선택 : %s" %(bots_choice[0]))
                        elif res2.content == '바위':
                            if bots_choice[0] == '가위':
                                await message.channel.send("이겼습니다! 봇의 선택 : %s" %(bots_choice[0]))
                            elif bots_choice[0] == '바위':
                                await message.channel.send("비겼습니다. 봇의 선택 : %s" %(bots_choice[0]))
                            else:
                                await message.channel.send("졌습니다... 봇의 선택 : %s" %(bots_choice[0]))
                        else:
                            if bots_choice[0] == '가위':
                                await message.channel.send("졌습니다... 봇의 선택 : %s" %(bots_choice[0]))
                            elif bots_choice[0] == '바위':
                                await message.channel.send("이겼습니다! 봇의 선택 : %s" %(bots_choice[0]))
                            else:
                                await message.channel.send("비겼습니다. 봇의 선택 : %s" %(bots_choice[0]))
                    except asyncio.TimeoutError:
                        await message.channel.send("10초가 지났습니다. 당신의 패배입니다.")
                else:
                    await message.channel.send("게임이 종료되었습니다.")
            except asyncio.TimeoutError:
                await message.channel.send("게임이 취소되었습니다. 장비를 정지합니다.")
        elif sample[0] == "끝말잇기":
            embed = discord.Embed(title="끝말잇기!", description="", color=0xf69fa8)
            embed.add_field(name="퓨이린의 랜덤게임" ,value="시작하려면 /시작\n끝내려면 /종료", inline=False)
            await message.channel.send(embed=embed)
            def check(res):
                return res.content == '/시작' or res.content == '/종료'
            try:
                res = await app.wait_for('message', timeout=10.0, check=check)
                if res.content == '/시작':
                    await message.channel.send("봇이 먼저 시작합니다! 제한 시간은 5초입니다!")
                    history = []
                    # blacklist = ['즘', '틱', '늄', '슘', '퓸', '늬', '뺌', '섯', '숍', '륨']
                    
                    list1 = []
                    list2 = []
                    count1 = 0
                    count2 = 0
                    t = open('dict.txt', 'r+', encoding="UTF-8")
                    tlist = t.readlines()
                    for i in tlist:
                        i = i.rstrip('\n')
                        i = i.strip()
                        list1.append(i)
                        count1 = len(list1)
                    list2 = [x for x in list1 if x]
                    bots_word = list2
                    await message.channel.send("%s" %random.sample(bots_word, 1))
                    while True:
                        try:
                            try:
                                query = await app.wait_for("message", timeout=5.0)
                                start = query.content[-1]
                                ans_list = []
                                if query.content in list2 and not (query.content in history):
                                    history.append(query.content)
                                    for word in list2:
                                        if word.startswith(start) and not (word in history):
                                            ans_list.append(word)
                                        else:
                                            continue
                                    bots_ans = random.sample(ans_list, 1)
                                    history.append(bots_ans[0])
                                    await message.channel.send(bots_ans)
                                else:
                                    if not (query.content in list2):
                                        await message.channel.send("사전에 없는 단어입니다.")
                                    else:
                                        await message.channel.send("이미 사용된 단어입니다.")
                            except ValueError:
                                await message.channel.send("봇이 단어를 찾지 못했습니다. 당신의 승리!")
                                break
                        except asyncio.TimeoutError:
                            await message.channel.send("타임아웃! 봇의 승리")
                            break
                else:
                    await message.channel.send("게임이 종료되었습니다.")
            except asyncio.TimeoutError:
                await message.channel.send("게임이 취소되었습니다. 장비를 정지합니다.")
        elif sample[0] == "블랙잭":
            embed = discord.Embed(title="블랙잭!", description="", color=0xFF5E00)
            embed.add_field(name="퓨이린의 랜덤게임" ,value="시작하려면 /시작\n끝내려면 /종료", inline=False)
            await message.channel.send(embed=embed)
            def check(res):
                return res.content == '/시작' or res.content == '/종료'
            try:
                res = await app.wait_for('message', timeout=10.0, check=check)
                if res.content == '/시작':
                    deck = fresh_deck()
                    while True:
                        dealer = []
                        player = []
                        for _ in range(2):
                            card, deck = hit(deck)
                            player.append(card)
                            card, deck = hit(deck)
                            dealer.append(card)
                        embed = discord.Embed(title="딜러의 카드", description="", color=0xFF5E00)
                        embed.add_field(name="한 장은 미공개입니다", value="%s, %s" %(dealer[1][0], dealer[1][1]),\
                            inline=False)
                        await message.channel.send(embed=embed)
                        embed = discord.Embed(title="당신의 카드", description="", color=0xFF5E00)
                        embed.add_field(name="------" , value="%s, %s \n %s, %s" %(player[0][0], player[0][1],\
                            player[1][0], player[1][1]), inline=False)
                        await message.channel.send(embed=embed)
                        score_player = count_score(player)
                        score_dealer = count_score(dealer)
                        if score_player == 21:
                            await message.channel.send('블랙잭! 당신의 승리!')
                            await message.channel.send('한 판 더? (y/n)')
                            def check5(res):
                                return res.content == 'y' or res.content == 'n'
                            try:
                                res = await app.wait_for('message', timeout=10.0, check=check5)
                                if res.content == 'y':
                                    continue
                                else:
                                    break
                            except asyncio.TimeoutError:
                                await message.channel.send('응답하지 않아 게임을 종료합니다.')
                        await message.channel.send('카드를 더 받으시겠습니까? (y/n)')
                        def more_card(res):
                            return res.content == 'y' or res.content == 'n'
                        try:
                            res = await app.wait_for('message', timeout=10.0, check=more_card)
                            while score_player < 21 and res.content == 'y':
                                card, deck = hit(deck)
                                player.append(card)
                                score_player = count_score(player)
                            if score_player > 21:
                                embed = discord.Embed(title="당신의 카드", description="", color=0xFF5E00)
                                for card in player:
                                    embed.add_field(name="-" , value="%s, %s" %(card[0], card[1]), inline=False)
                                await message.channel.send(embed=embed)
                                await message.channel.send("버스트! 딜러의 승리!")
                                await message.channel.send('한 판 더? (y/n)')
                                def check5(res):
                                    return res.content == 'y' or res.content == 'n'
                                try:
                                    res = await app.wait_for('message', timeout=10.0, check=check5)
                                    if res.content == 'y':
                                        continue
                                    else:
                                        break
                                except asyncio.TimeoutError:
                                    await message.channel.send('응답하지 않아 게임을 종료합니다.')
                                    break
                            while score_dealer <= 16:
                                card, deck = hit(deck)
                                dealer.append(card)
                                score_dealer = count_score(dealer)
                            if score_dealer > 21:
                                embed = discord.Embed(title="딜러의 카드", description="", color=0xFF5E00)
                                for card in dealer:
                                    embed.add_field(name="-" , value="%s, %s" %(card[0], card[1]), inline=False)
                                await message.channel.send(embed=embed)
                                embed = discord.Embed(title="당신의 카드", description="", color=0xFF5E00)
                                for card in player:
                                    embed.add_field(name="-" , value="%s, %s" %(card[0], card[1]), inline=False)
                                await message.channel.send(embed=embed)
                                await message.channel.send("버스트! 당신의 승리!")
                                await message.channel.send('한 판 더? (y/n)')
                                def check5(res):
                                    return res.content == 'y' or res.content == 'n'
                                try:
                                    res = await app.wait_for('message', timeout=10.0, check=check5)
                                    if res.content == 'y':
                                        continue
                                    else:
                                        break
                                except asyncio.TimeoutError:
                                    await message.channel.send('응답하지 않아 게임을 종료합니다.')
                                    break
                            elif score_dealer == score_player:
                                embed = discord.Embed(title="딜러의 카드", description="", color=0xFF5E00)
                                for card in dealer:
                                    embed.add_field(name="-" , value="%s, %s" %(card[0], card[1]), inline=False)
                                await message.channel.send(embed=embed)
                                embed = discord.Embed(title="당신의 카드", description="", color=0xFF5E00)
                                for card in player:
                                    embed.add_field(name="-" , value="%s, %s" %(card[0], card[1]), inline=False)
                                await message.channel.send(embed=embed)
                                await message.channel.send('비겼습니다')
                                await message.channel.send('한 판 더? (y/n)')
                                def check5(res):
                                    return res.content == 'y' or res.content == 'n'
                                try:
                                    res = await app.wait_for('message', timeout=10.0, check=check5)
                                    if res.content == 'y':
                                        continue
                                    else:
                                        break
                                except asyncio.TimeoutError:
                                    await message.channel.send('응답하지 않아 게임을 종료합니다.')
                                    break
                            else:
                                if score_player > score_dealer:
                                    embed = discord.Embed(title="딜러의 카드", description="", color=0xFF5E00)
                                    for card in dealer:
                                        embed.add_field(name="-" , value="%s, %s" %(card[0], card[1]), inline=False)
                                    await message.channel.send(embed=embed)
                                    embed = discord.Embed(title="당신의 카드", description="", color=0xFF5E00)
                                    for card in player:
                                        embed.add_field(name="-" , value="%s, %s" %(card[0], card[1]), inline=False)
                                    await message.channel.send(embed=embed)
                                    await message.channel.send('당신의 승리!')
                                    await message.channel.send('한 판 더? (y/n)')
                                    def check5(res):
                                        return res.content == 'y' or res.content == 'n'
                                    try:
                                        res = await app.wait_for('message', timeout=10.0, check=check5)
                                        if res.content == 'y':
                                            continue
                                        else:
                                            break
                                    except asyncio.TimeoutError:
                                        await message.channel.send('응답하지 않아 게임을 종료합니다.')
                                        break
                                else:
                                    embed = discord.Embed(title="딜러의 카드", description="", color=0xFF5E00)
                                    for card in dealer:
                                        embed.add_field(name="-" , value="%s, %s" %(card[0], card[1]), inline=False)
                                    await message.channel.send(embed=embed)
                                    embed = discord.Embed(title="당신의 카드", description="", color=0xFF5E00)
                                    for card in player:
                                        embed.add_field(name="-" , value="%s, %s" %(card[0], card[1]), inline=False)
                                    await message.channel.send(embed=embed)
                                    await message.channel.send('딜러의 승리!')
                                    await message.channel.send('한 판 더? (y/n)')
                                    def check5(res):
                                        return res.content == 'y' or res.content == 'n'
                                    try:
                                        res = await app.wait_for('message', timeout=10.0, check=check5)
                                        if res.content == 'y':
                                            continue
                                        else:
                                            break
                                    except asyncio.TimeoutError:
                                        await message.channel.send('응답하지 않아 게임을 종료합니다.')
                                        break
                        except:
                            await message.channel.send('응답하지 않아 게임을 종료합니다.')
                            break
            except asyncio.TimeoutError:
                await message.channel.send("게임이 취소되었습니다. 장비를 정지합니다.")
        else:
            pass
    if message.content == "/패치노트":
        await message.channel.send("https://github.com/Puilin/My-own-code/blob/master/%ED%8C%A8%EC%B9%98%EB%85%B8%ED%8A%B8.md")
    if message.content == "/DN":
        await message.channel.send("남만주")
    if message.content in ['/도움말', '/명령어']:
        embed = discord.Embed(title="명령어 목록", description="", color=0xFFA7A7)
        embed.add_field(name = "/안녕", value = "퓨이린 봇이 인사를 합니다.", inline=False)
        embed.add_field(name = "/발", value = "금지된 명령어입니다.", inline=False)
        embed.add_field(name = "/DN", value = "금지된 명령어입니다2", inline=False)
        embed.add_field(name = "/나무", value = "봇이 나무를 캐줍니다.", inline=False)
        embed.add_field(name = "/도움말 or /명령어", value = "명령어 목록을 볼 수 있습니다.", inline=False)
        embed.add_field(name = "/롤전적 (닉네임)", value = "(닉네임)의 롤 전적을 검색합니다.", inline=False)
        embed.add_field(name = "/패치노트", value = "패치노트를 확인합니다.", inline=False)
        embed.add_field(name = "/뽑기 (숫자1) (숫자2)", value = "(숫자1)과 (숫자2) 사이의 수를 랜덤으로 고릅니다.", inline=False)
        embed.add_field(name = "/청소 (숫자)", value = "(숫자)만큼 지난 채팅을 삭제합니다.", inline=False)
        embed.add_field(name = "/출첵 or /출석체크", value = "출석체크 현황을 확인합니다.", inline=False)
        await message.channel.send(embed=embed)
    if message.content in ["/출첵", "/출석체크"]:
        embed = discord.Embed(title="출석체크 현황", description="", color=0xD1B2FF)
        embed.add_field(name = "출석인원", value = "%d명" %len(daily), inline=False)
        embed.add_field(name = "출석자 목록", value = "%s" %daily, inline=False)
        await message.channel.send(embed=embed)


## op.gg crawling code, covid19 stat code are written by Hoplin

    if message.content.startswith("/코로나"):
        # 보건복지부 코로나 바이러스 정보사이트"
        covidSite = "http://ncov.mohw.go.kr/index.jsp"
        covidNotice = "http://ncov.mohw.go.kr"
        html = urlopen(covidSite)
        bs = BeautifulSoup(html, 'html.parser')
        latestupdateTime = bs.find('span', {'class': "livedate"}).text.split(',')[0][1:].split('.')
        statisticalNumbers = bs.findAll('span', {'class': 'num'})
        beforedayNumbers = bs.findAll('span', {'class': 'before'})

        #주요 브리핑 및 뉴스링크
        briefTasks = []
        mainbrief = bs.findAll('a',{'href' : re.compile('\/tcmBoardView\.do\?contSeq=[0-9]*')})
        for brf in mainbrief:
            container = []
            container.append(brf.text)
            container.append(covidNotice + brf['href'])
            briefTasks.append(container)
        print(briefTasks)

        # 통계수치
        statNum = []
        # 전일대비 수치
        beforeNum = []
        for num in range(7):
            statNum.append(statisticalNumbers[num].text)
        for num in range(4):
            beforeNum.append(beforedayNumbers[num].text.split('(')[-1].split(')')[0])

        totalPeopletoInt = statNum[0].split(')')[-1].split(',')
        tpInt = ''.join(totalPeopletoInt)
        lethatRate = round((int(statNum[3]) / int(tpInt)) * 100, 2)
        embed = discord.Embed(title="대한민국 코로나19 현황", description="",color=0x5CD1E5)
        embed.add_field(name="출처 : 보건복지부", value="http://ncov.mohw.go.kr/index.jsp", inline=False)
        embed.add_field(name="최근 업데이트 시각",value="해당 자료는 " + latestupdateTime[0] + "월 " + latestupdateTime[1] + "일 "+latestupdateTime[2] +" 자료입니다.", inline=False)
        embed.add_field(name="확진환자(누적)", value=statNum[0].split(')')[-1]+"("+beforeNum[0]+")",inline=True)
        embed.add_field(name="완치환자(격리해제)", value=statNum[1] + "(" + beforeNum[1] + ")", inline=True)
        embed.add_field(name="치료중(격리 중)", value=statNum[2] + "(" + beforeNum[2] + ")", inline=True)
        embed.add_field(name="사망", value=statNum[3] + "(" + beforeNum[3] + ")", inline=True)
        embed.add_field(name="누적확진률", value=statNum[6], inline=True)
        embed.add_field(name="치사율", value=str(lethatRate) + " %",inline=True)
        embed.add_field(name="- 최신 브리핑 1 : " + briefTasks[0][0],value="Link : " + briefTasks[0][1],inline=False)
        embed.add_field(name="- 최신 브리핑 2 : " + briefTasks[1][0], value="Link : " + briefTasks[1][1], inline=False)
        embed.set_thumbnail(url="https://wikis.krsocsci.org/images/7/79/%EB%8C%80%ED%95%9C%EC%99%95%EA%B5%AD_%ED%83%9C%EA%B7%B9%EA%B8%B0.jpg")
        await message.channel.send(embed=embed)

    if message.content.startswith("/롤전적"):
        try:
            if len(message.content.split(" ")) == 1:
                embed = discord.Embed(title="소환사 이름이 입력되지 않았습니다!", description="", color=0x5CD1E5)
                embed.add_field(name="Summoner name not entered",
                                value="To use command /롤전적 : /롤전적 (Summoner Nickname)", inline=False)
                await message.channel.send("Error : Incorrect command usage ", embed=embed)
            else:
                playerNickname = ''.join((message.content).split(' ')[1:])
                # Open URL
                checkURLBool = urlopen(opggsummonersearch + quote(playerNickname))
                bs = BeautifulSoup(checkURLBool, 'html.parser')

                # 자유랭크 언랭은 뒤에 '?image=q_auto&v=1'표현이없다

                # Patch Note 20200503에서
                # Medal = bs.find('div', {'class': 'ContentWrap tabItems'}) 이렇게 바꾸었었습니다.
                # PC의 설정된 환경 혹은 OS플랫폼에 따라서 ContentWrap tabItems의 띄어쓰기가 인식이

                Medal = bs.find('div', {'class': 'SideContent'})
                RankMedal = Medal.findAll('img', {'src': re.compile('\/\/[a-z]*\-[A-Za-z]*\.[A-Za-z]*\.[A-Za-z]*\/[A-Za-z]*\/[A-Za-z]*\/[a-z0-9_]*\.png')})
                # Variable RankMedal's index 0 : Solo Rank
                # Variable RankMedal's index 1 : Flexible 5v5 rank

                # for mostUsedChampion
                mostUsedChampion = bs.find('div', {'class': 'ChampionName'})
                mostUsedChampionKDA = bs.find('span', {'class': 'KDA'})

                # 솔랭, 자랭 둘다 배치가 안되어있는경우 -> 사용된 챔피언 자체가 없다. 즉 모스트 챔피언 메뉴를 넣을 필요가 없다.

                # Scrape Summoner's Rank information
                # [Solorank,Solorank Tier]
                solorank_Types_and_Tier_Info = deleteTags(bs.findAll('div', {'class': {'RankType', 'TierRank'}}))
                # [Solorank LeaguePoint, Solorank W, Solorank L, Solorank Winratio]
                solorank_Point_and_winratio = deleteTags(
                    bs.findAll('span', {'class': {'LeaguePoints', 'wins', 'losses', 'winratio'}}))
                # [자유랭 5:5,Flexrank Tier,Flextier leaguepoint + W/L,Flextier win ratio]
                flexrank_Types_and_Tier_Info = deleteTags(bs.findAll('div', {
                    'class': {'sub-tier__rank-type', 'sub-tier__rank-tier', 'sub-tier__league-point',
                              'sub-tier__gray-text'}}))
                # ['Flextier W/L]
                flexrank_Point_and_winratio = deleteTags(bs.findAll('span', {'class': {'sub-tier__gray-text'}}))

                # embed.set_imag()는 하나만 들어갈수 있다.

                # 솔랭, 자랭 둘다 배치 안되어있는 경우 -> 모스트 챔피언 출력 X
                if len(solorank_Point_and_winratio) == 0 and len(flexrank_Point_and_winratio) == 0:
                    embed = discord.Embed(title="소환사 전적검색", description="", color=0x5CD1E5)
                    embed.add_field(name="소환사의 op.gg 주소", value=opggsummonersearch + playerNickname,
                                    inline=False)
                    embed.add_field(name="솔랭 : Unranked", value="Unranked", inline=False)
                    embed.add_field(name="자유랭 5:5 : Unranked", value="Unranked", inline=False)
                    embed.set_thumbnail(url='https:' + RankMedal[0]['src'])
                    await message.channel.send("소환사 " + playerNickname + "님의 전적", embed=embed)

                # 솔로랭크 기록이 없는경우
                elif len(solorank_Point_and_winratio) == 0:

                    # most Used Champion Information : Champion Name, KDA, Win Rate
                    mostUsedChampion = bs.find('div', {'class': 'ChampionName'})
                    mostUsedChampion = mostUsedChampion.a.text.strip()
                    mostUsedChampionKDA = bs.find('span', {'class': 'KDA'})
                    mostUsedChampionKDA = mostUsedChampionKDA.text.split(':')[0]
                    mostUsedChampionWinRate = bs.find('div', {'class': "Played"})
                    mostUsedChampionWinRate = mostUsedChampionWinRate.div.text.strip()

                    FlexRankTier = flexrank_Types_and_Tier_Info[0] + ' : ' + flexrank_Types_and_Tier_Info[1]
                    FlexRankPointAndWinRatio = flexrank_Types_and_Tier_Info[2] + " /" + flexrank_Types_and_Tier_Info[-1]
                    embed = discord.Embed(title="소환사 전적검색", description="", color=0x5CD1E5)
                    embed.add_field(name="소환사의 op.gg 주소", value=opggsummonersearch + playerNickname,
                                    inline=False)
                    embed.add_field(name="솔랭 : Unranked", value="Unranked", inline=False)
                    embed.add_field(name="자유랭 5:5 :"+FlexRankTier[15:], value=FlexRankPointAndWinRatio, inline=False)
                    embed.add_field(name="모스트 : " + mostUsedChampion,
                                    value="KDA : " + mostUsedChampionKDA + " / " + " WinRate : " + mostUsedChampionWinRate,
                                    inline=False)
                    embed.set_thumbnail(url='https:' + RankMedal[1]['src'])
                    await message.channel.send("소환사 " + playerNickname + "님의 전적", embed=embed)

                # 자유랭크 기록이 없는경우
                elif len(flexrank_Point_and_winratio) == 0:

                    # most Used Champion Information : Champion Name, KDA, Win Rate
                    mostUsedChampion = bs.find('div', {'class': 'ChampionName'})
                    mostUsedChampion = mostUsedChampion.a.text.strip()
                    mostUsedChampionKDA = bs.find('span', {'class': 'KDA'})
                    mostUsedChampionKDA = mostUsedChampionKDA.text.split(':')[0]
                    mostUsedChampionWinRate = bs.find('div', {'class': "Played"})
                    mostUsedChampionWinRate = mostUsedChampionWinRate.div.text.strip()

                    SoloRankTier = solorank_Types_and_Tier_Info[0] + ' : ' + solorank_Types_and_Tier_Info[1]
                    SoloRankPointAndWinRatio = solorank_Point_and_winratio[0] + "/ " + solorank_Point_and_winratio[
                        1] + " " + solorank_Point_and_winratio[2] + " /" + solorank_Point_and_winratio[3]
                    embed = discord.Embed(title="소환사 전적검색", description="", color=0x5CD1E5)
                    embed.add_field(name="소환사의 op.gg 주소", value=opggsummonersearch + playerNickname,
                                    inline=False)
                    embed.add_field(name="솔랭 :"+SoloRankTier[13:], value=SoloRankPointAndWinRatio, inline=False)
                    embed.add_field(name="자유랭 5:5 : Unranked", value="Unranked", inline=False)
                    embed.add_field(name="모스트 : " + mostUsedChampion,
                                    value="KDA : " + mostUsedChampionKDA + " / " + "WinRate : " + mostUsedChampionWinRate,
                                    inline=False)
                    embed.set_thumbnail(url='https:' + RankMedal[0]['src'])
                    await message.channel.send("소환사 " + playerNickname + "님의 전적", embed=embed)
                # 두가지 유형의 랭크 모두 완료된사람
                else:
                    # 더 높은 티어를 thumbnail에 안착
                    solorankmedal = RankMedal[0]['src'].split('/')[-1].split('?')[0].split('.')[0].split('_')
                    flexrankmedal = RankMedal[1]['src'].split('/')[-1].split('?')[0].split('.')[0].split('_')

                    # Make State
                    SoloRankTier = solorank_Types_and_Tier_Info[0] + ' : ' + solorank_Types_and_Tier_Info[1]
                    SoloRankPointAndWinRatio = solorank_Point_and_winratio[0] + "/ " + solorank_Point_and_winratio[
                        1] + " " + solorank_Point_and_winratio[2] + " /" + solorank_Point_and_winratio[3]
                    FlexRankTier = flexrank_Types_and_Tier_Info[0] + ' : ' + flexrank_Types_and_Tier_Info[1]
                    FlexRankPointAndWinRatio = flexrank_Types_and_Tier_Info[2] + " /" + flexrank_Types_and_Tier_Info[-1]

                    # most Used Champion Information : Champion Name, KDA, Win Rate
                    mostUsedChampion = bs.find('div', {'class': 'ChampionName'})
                    mostUsedChampion = mostUsedChampion.a.text.strip()
                    mostUsedChampionKDA = bs.find('span', {'class': 'KDA'})
                    mostUsedChampionKDA = mostUsedChampionKDA.text.split(':')[0]
                    mostUsedChampionWinRate = bs.find('div', {'class': "Played"})
                    mostUsedChampionWinRate = mostUsedChampionWinRate.div.text.strip()

                    cmpTier = tierCompare(solorankmedal[0], flexrankmedal[0])
                    embed = discord.Embed(title="소환사 전적검색", description="", color=0x5CD1E5)
                    embed.add_field(name="소환사의 op.gg 주소", value=opggsummonersearch + playerNickname,
                                    inline=False)
                    embed.add_field(name="솔랭 :"+SoloRankTier[13:], value=SoloRankPointAndWinRatio, inline=False)
                    embed.add_field(name="자유랭 5:5 :"+FlexRankTier[15:], value=FlexRankPointAndWinRatio, inline=False)
                    embed.add_field(name="모스트 : " + mostUsedChampion,
                                    value="KDA : " + mostUsedChampionKDA + " / " + " WinRate : " + mostUsedChampionWinRate,
                                    inline=False)
                    if cmpTier == 0:
                        embed.set_thumbnail(url='https:' + RankMedal[0]['src'])
                    elif cmpTier == 1:
                        embed.set_thumbnail(url='https:' + RankMedal[1]['src'])
                    else:
                        if solorankmedal[1] > flexrankmedal[1]:
                            embed.set_thumbnail(url='https:' + RankMedal[0]['src'])
                        elif solorankmedal[1] < flexrankmedal[1]:
                            embed.set_thumbnail(url='https:' + RankMedal[0]['src'])
                        else:
                            embed.set_thumbnail(url='https:' + RankMedal[0]['src'])

                    await message.channel.send("소환사 " + playerNickname + "님의 전적", embed=embed)
        except HTTPError as e:
            embed = discord.Embed(title="소환사 전적검색 실패", description="", color=0x5CD1E5)
            embed.add_field(name="", value="올바르지 않은 소환사 이름입니다. 다시 확인해주세요!", inline=False)
            await message.channel.send("Wrong Summoner Nickname")

        except UnicodeEncodeError as e:
            embed = discord.Embed(title="소환사 전적검색 실패", description="", color=0x5CD1E5)
            embed.add_field(name="???", value="올바르지 않은 소환사 이름입니다. 다시 확인해주세요!", inline=False)
            await message.channel.send("Wrong Summoner Nickname", embed=embed)

        except AttributeError as e:
            embed = discord.Embed(title="존재하지 않는 소환사", description="", color=0x5CD1E5)
            embed.add_field(name="해당 닉네임의 소환사가 존재하지 않습니다.", value="소환사 이름을 확인해주세요", inline=False)
            await message.channel.send("Error : Non existing Summoner ", embed=embed)

@app.event
async def on_voice_state_update(member, before, after):
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
            if not member.name in daily: #출석체크 명단에 있는지 체크 없으면 출첵
                daily.append(member.name)
                await member.guild.system_channel.send(str(member.name) + " 님 "\
                    + str(now[:10]) + " :white_check_mark: 출석체크 완료")

global daily
daily = []
global timestamp
timestamp = []

#@app.event
#async def on_voice_state_update(member, before, after):
 #   if(os.path.exists("LogCH/" + str(member.guild.id) + ".txt") != True):
  #      return
    
    
   # file = open("LogCH/" + str(member.guild.id) + ".txt", "r")
 #   path = file.read()
  #  file.close()
   # ch = member.guild.get_channel(int(path))
   # if(before.channel == None):
    #    now = datetime.datetime.now()
     #   embed = discord.Embed(title = "보이스 참여", description = "<#" + str(after.channel.id)+">채널에 "+str(member.name)+'님이 참여하셨습니다.', color = 0x00ff00)
      #  embed.add_field(name = "id", value = str(member.id), inline=False)
       # embed.add_field(name = "시간", value = str(now), inline=False)
        #await ch.send(embed=embed)
  #  else:
   #     now = datetime.datetime.now()
    #    embed = discord.Embed(title = "보이스 종료", description = "<#" + str(before.channel.id)+">채널에서 "+str(member.name)+'님이 떠나셨습니다.', color = 0x00ff00)
     #   embed.add_field(name = "id", value = str(member.id), inline=False)
     #   embed.add_field(name = "시간", value = str(now), inline=False)
     #   await ch.send(embed=embed)
app.run(token)
