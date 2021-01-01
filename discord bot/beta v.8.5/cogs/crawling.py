import discord
from discord.ext import commands
from urllib.request import urlopen, Request, URLError, HTTPError
import urllib
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import quote
import warnings
import re
import os
import asyncio

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

class Crawling(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        
        if message.author.bot:
            return None
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


def setup(bot):
    bot.add_cog(Crawling(bot))