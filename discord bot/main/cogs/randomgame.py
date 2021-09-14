from discord.ext import commands
import asyncio
import random
import discord
from cardgame import *

class RandomGame(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):


        if message.author.bot:
            return None
        if message.content == "/랜덤게임":
            game_list = ["가위바위보", "끝말잇기", "블랙잭", "업다운"]
            sample = random.sample(game_list, 1)
            await message.channel.send("뽑힌 게임은 %s입니다." %sample)
            if sample[0] == "가위바위보":
                embed = discord.Embed(title="가위바위보!", description="", color=0x5CD1E5)
                embed.add_field(name="퓨이린의 랜덤게임" ,value="시작하려면 /시작\n끝내려면 /종료", inline=False)
                await message.channel.send(embed=embed)
                def check15(res):
                    return res.content == '/시작' or res.content == '/종료'
                try:
                    res = await self.bot.wait_for('message', timeout=10.0, check=check15)
                    if res.content == '/시작':
                        await message.channel.send("가위, 바위, 보 중에 고르세요! 제한시간은 10초입니다!")
                        def check16(res2):
                            return res2.content == '가위' or res2.content == '바위' or res2.content == '보'
                        try:
                            res2 = await self.bot.wait_for('message', timeout=10.0, check=check16)
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
                def check17(res):
                    return res.content == '/시작' or res.content == '/종료'
                try:
                    res = await self.bot.wait_for('message', timeout=10.0, check=check17)
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
                                    query = await self.bot.wait_for("message", timeout=5.0)
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
                def check18(res):
                    return res.content == '/시작' or res.content == '/종료'
                try:
                    res = await self.bot.wait_for('message', timeout=10.0, check=check18)
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
                                def check19(res):
                                    return res.content == 'y' or res.content == 'n'
                                try:
                                    res = await self.bot.wait_for('message', timeout=10.0, check=check19)
                                    if res.content == 'y':
                                        continue
                                    else:
                                        break
                                except asyncio.TimeoutError:
                                    await message.channel.send('응답하지 않아 게임을 종료합니다.')
                            await message.channel.send('카드를 더 받으시겠습니까? (y/n)')
                            def more_card2(res):
                                return res.content == 'y' or res.content == 'n'
                            try:
                                res = await self.bot.wait_for('message', timeout=10.0, check=more_card2)
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
                                    def check20(res):
                                        return res.content == 'y' or res.content == 'n'
                                    try:
                                        res = await self.bot.wait_for('message', timeout=10.0, check=check20)
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
                                    def check21(res):
                                        return res.content == 'y' or res.content == 'n'
                                    try:
                                        res = await self.bot.wait_for('message', timeout=10.0, check=check21)
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
                                    def check22(res):
                                        return res.content == 'y' or res.content == 'n'
                                    try:
                                        res = await self.bot.wait_for('message', timeout=10.0, check=check22)
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
                                        def check23(res):
                                            return res.content == 'y' or res.content == 'n'
                                        try:
                                            res = await self.bot.wait_for('message', timeout=10.0, check=check23)
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
                                        def check24(res):
                                            return res.content == 'y' or res.content == 'n'
                                        try:
                                            res = await self.bot.wait_for('message', timeout=10.0, check=check24)
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
                    else:
                        await message.channel.send("게임이 종료되었습니다.")
                except asyncio.TimeoutError:
                    await message.channel.send("게임이 취소되었습니다. 장비를 정지합니다.")
            elif sample[0] == "업다운":
                embed = discord.Embed(title="업다운!", description="", color=0xA566FF)
                embed.add_field(name="퓨이린의 랜덤게임" ,value="시작하려면 /시작\n끝내려면 /종료", inline=False)
                await message.channel.send(embed=embed)
                def check25(res):
                    return res.content == '/시작' or res.content == '/종료'
                try:
                    res = await self.bot.wait_for('message', timeout=10.0, check=check25)
                    if res.content == '/시작':
                        await message.channel.send("업다운은 봇이 뽑은 숫자를 10회 안에 맞추는 게임입니다.")
                        await message.channel.send("숫자의 자릿수를 입력해주세요. 입력시간 초과시 기본값으로 설정됩니다. (기본값 : 3)")
                        def check26(res):
                            return res.content.isdigit()
                        try:
                            res = await self.bot.wait_for('message', timeout=10.0, check=check26)
                            len_of_num = int(res.content)
                            maximum = (10**len_of_num) - 1
                            minimum = (10**(len_of_num-1))
                            bots_num = random.randint(minimum, maximum)
                            def check27(res):
                                return res.content.isdigit()
                            try:
                                count = 0
                                embed = discord.Embed(color=0xA566FF)
                                embed.add_field(name="업다운 게임", value="봇의 숫자는? [제한시간 20초]")
                                embed.set_footer(text="남은 기회 : %d" %(10-count))
                                await message.channel.send(embed=embed)
                                res = await self.bot.wait_for('message', timeout=20.0, check=check27)
                                while count < 9 and int(res.content) != bots_num:
                                    embed = discord.Embed(color=0xA566FF)
                                    if int(res.content) > bots_num:
                                        embed.add_field(name="업다운 게임", value="다운!")
                                    else:
                                        embed.add_field(name="업다운 게임", value="업!")
                                    count += 1
                                    embed.set_footer(text="남은 기회 : %d" %(10-count))
                                    await message.channel.send(embed=embed)
                                    try:
                                        res = await self.bot.wait_for('message', timeout=20.0, check=check27)
                                    except asyncio.TimeoutError:
                                        await message.channel.send("시간초과! 봇이 뽑은 숫자 : %d" %bots_num)
                                if int(res.content) == bots_num:
                                    await message.channel.send("축하합니다, 정답입니다! 봇이 뽑은 숫자 : %d" %bots_num)
                                else:
                                    await message.channel.send("봇이 뽑은 숫자는 [ %d ] 였습니다..." %bots_num)
                            except asyncio.TimeoutError:
                                await message.channel.send("시간초과! 봇이 뽑은 숫자 : %d" %bots_num)
                        except asyncio.TimeoutError:
                            await message.channel.send("기본값으로 설정되었습니다.")
                            bots_num = random.randint(100, 999)
                            def check28(res):
                                return res.content.isdigit()
                            try:
                                count = 0
                                embed = embed = discord.Embed(color=0xA566FF)
                                embed.add_field(name="업다운 게임", value="봇의 숫자는? [제한시간 20초]")
                                embed.set_footer(text="남은 기회 : %d" %(10-count))
                                await message.channel.send(embed=embed)
                                res = await self.bot.wait_for('message', timeout=20.0, check=check28)
                                while count < 9 and int(res.content) != bots_num:
                                    embed = discord.Embed(color=0xA566FF)
                                    if int(res.content) > bots_num:
                                        embed.add_field(name="업다운 게임", value="다운!")
                                    else:
                                        embed.add_field(name="업다운 게임", value="업!")
                                    count += 1
                                    embed.set_footer(text="남은 기회 : %d" %(10-count))
                                    await message.channel.send(embed=embed)
                                    try:
                                        res = await self.bot.wait_for('message', timeout=20.0, check=check28)
                                    except asyncio.TimeoutError:
                                        await message.channel.send("시간초과! 봇이 뽑은 숫자 : %d" %bots_num)
                                if int(res.content) == bots_num:
                                    await message.channel.send("축하합니다, 정답입니다! 봇이 뽑은 숫자 : %d" %bots_num)
                                else:
                                    await message.channel.send("봇이 뽑은 숫자는 [ %d ] 였습니다..." %bots_num)
                            except asyncio.TimeoutError:
                                await message.channel.send("시간초과! 봇이 뽑은 숫자 : %d" %bots_num)
                    else:
                        await message.channel.send("게임이 종료되었습니다.")
                except asyncio.TimeoutError:
                    await message.channel.send("게임이 취소되었습니다. 장비를 정지합니다.")
            else:
                pass
        if message.content == '/가위바위보':
            embed = discord.Embed(title="가위바위보!", description="", color=0x5CD1E5)
            embed.add_field(name="퓨이린의 랜덤게임" ,value="시작하려면 /시작\n끝내려면 /종료", inline=False)
            await message.channel.send(embed=embed)
            def check(res):
                return res.content == '/시작' or res.content == '/종료'
            try:
                res = await self.bot.wait_for('message', timeout=10.0, check=check)
                if res.content == '/시작':
                    await message.channel.send("가위, 바위, 보 중에 고르세요! 제한시간은 10초입니다!")
                    def check2(res2):
                        return res2.content == '가위' or res2.content == '바위' or res2.content == '보'
                    try:
                        res2 = await self.bot.wait_for('message', timeout=10.0, check=check2)
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
        if message.content == "/끝말잇기":
            embed = discord.Embed(title="끝말잇기!", description="", color=0xf69fa8)
            embed.add_field(name="퓨이린의 랜덤게임" ,value="시작하려면 /시작\n끝내려면 /종료", inline=False)
            await message.channel.send(embed=embed)
            def check3(res):
                return res.content == '/시작' or res.content == '/종료'
            try:
                res = await self.bot.wait_for('message', timeout=10.0, check=check3)
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
                                query = await self.bot.wait_for("message", timeout=5.0)
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
        if message.content == "/블랙잭":
            embed = discord.Embed(title="블랙잭!", description="", color=0xFF5E00)
            embed.add_field(name="퓨이린의 랜덤게임" ,value="시작하려면 /시작\n끝내려면 /종료", inline=False)
            await message.channel.send(embed=embed)
            def check4(res):
                return res.content == '/시작' or res.content == '/종료'
            try:
                res = await self.bot.wait_for('message', timeout=10.0, check=check4)
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
                                res = await self.bot.wait_for('message', timeout=10.0, check=check5)
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
                            res = await self.bot.wait_for('message', timeout=10.0, check=more_card)
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
                                def check6(res):
                                    return res.content == 'y' or res.content == 'n'
                                try:
                                    res = await self.bot.wait_for('message', timeout=10.0, check=check6)
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
                                def check7(res):
                                    return res.content == 'y' or res.content == 'n'
                                try:
                                    res = await self.bot.wait_for('message', timeout=10.0, check=check7)
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
                                def check8(res):
                                    return res.content == 'y' or res.content == 'n'
                                try:
                                    res = await self.bot.wait_for('message', timeout=10.0, check=check8)
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
                                    def check9(res):
                                        return res.content == 'y' or res.content == 'n'
                                    try:
                                        res = await self.bot.wait_for('message', timeout=10.0, check=check9)
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
                                    def check10(res):
                                        return res.content == 'y' or res.content == 'n'
                                    try:
                                        res = await self.bot.wait_for('message', timeout=10.0, check=check10)
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
                else:
                    await message.channel.send("게임이 종료되었습니다.")
            except asyncio.TimeoutError:
                await message.channel.send("게임이 취소되었습니다. 장비를 정지합니다.")
        if message.content == "/업다운":
            embed = discord.Embed(title="업다운!", description="", color=0xA566FF)
            embed.add_field(name="퓨이린의 랜덤게임" ,value="시작하려면 /시작\n끝내려면 /종료", inline=False)
            await message.channel.send(embed=embed)
            def check11(res):
                return res.content == '/시작' or res.content == '/종료'
            try:
                res = await self.bot.wait_for('message', timeout=10.0, check=check11)
                if res.content == '/시작':
                    await message.channel.send("업다운은 봇이 뽑은 숫자를 10회 안에 맞추는 게임입니다.")
                    await message.channel.send("숫자의 자릿수를 입력해주세요. 입력시간 초과시 기본값으로 설정됩니다. (기본값 : 3)")
                    def check12(res):
                        return res.content.isdigit()
                    try:
                        res = await self.bot.wait_for('message', timeout=10.0, check=check12)
                        len_of_num = int(res.content)
                        maximum = (10**len_of_num) - 1
                        minimum = (10**(len_of_num-1))
                        bots_num = random.randint(minimum, maximum)
                        def check13(res):
                            return res.content.isdigit()
                        try:
                            count = 0
                            embed = discord.Embed(color=0xA566FF)
                            embed.add_field(name="업다운 게임", value="봇의 숫자는? [제한시간 20초]")
                            embed.set_footer(text="남은 기회 : %d" %(10-count))
                            await message.channel.send(embed=embed)
                            res = await self.bot.wait_for('message', timeout=20.0, check=check13)
                            while count < 9 and int(res.content) != bots_num:
                                embed = discord.Embed(color=0xA566FF)
                                if int(res.content) > bots_num:
                                    embed.add_field(name="업다운 게임", value="다운!")
                                else:
                                    embed.add_field(name="업다운 게임", value="업!")
                                count += 1
                                embed.set_footer(text="남은 기회 : %d" %(10-count))
                                await message.channel.send(embed=embed)
                                try:
                                    res = await self.bot.wait_for('message', timeout=20.0, check=check13)
                                except asyncio.TimeoutError:
                                    await message.channel.send("시간초과! 봇이 뽑은 숫자 : %d" %bots_num)
                            if int(res.content) == bots_num:
                                await message.channel.send("축하합니다, 정답입니다! 봇이 뽑은 숫자 : %d" %bots_num)
                            else:
                                await message.channel.send("봇이 뽑은 숫자는 [ %d ] 였습니다..." %bots_num)
                        except asyncio.TimeoutError:
                            await message.channel.send("시간초과! 봇이 뽑은 숫자 : %d" %bots_num)
                    except asyncio.TimeoutError:
                        await message.channel.send("기본값으로 설정되었습니다.")
                        bots_num = random.randint(100, 999)
                        def check14(res):
                            return res.content.isdigit()
                        try:
                            count = 0
                            embed = embed = discord.Embed(color=0xA566FF)
                            embed.add_field(name="업다운 게임", value="봇의 숫자는? [제한시간 20초]")
                            embed.set_footer(text="남은 기회 : %d" %(10-count))
                            await message.channel.send(embed=embed)
                            res = await self.bot.wait_for('message', timeout=20.0, check=check14)
                            while count < 9 and int(res.content) != bots_num:
                                embed = discord.Embed(color=0xA566FF)
                                if int(res.content) > bots_num:
                                    embed.add_field(name="업다운 게임", value="다운!")
                                else:
                                    embed.add_field(name="업다운 게임", value="업!")
                                count += 1
                                embed.set_footer(text="남은 기회 : %d" %(10-count))
                                await message.channel.send(embed=embed)
                                try:
                                    res = await self.bot.wait_for('message', timeout=20.0, check=check14)
                                except asyncio.TimeoutError:
                                    await message.channel.send("시간초과! 봇이 뽑은 숫자 : %d" %bots_num)
                            if int(res.content) == bots_num:
                                await message.channel.send("축하합니다, 정답입니다! 봇이 뽑은 숫자 : %d" %bots_num)
                            else:
                                await message.channel.send("봇이 뽑은 숫자는 [ %d ] 였습니다..." %bots_num)
                        except asyncio.TimeoutError:
                            await message.channel.send("시간초과! 봇이 뽑은 숫자 : %d" %bots_num)
                else:
                    await message.channel.send("게임이 종료되었습니다.")
            except asyncio.TimeoutError:
                await message.channel.send("게임이 취소되었습니다. 장비를 정지합니다.")

def setup(bot):
    bot.add_cog(RandomGame(bot))