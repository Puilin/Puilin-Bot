import asyncio
import discord
from discord.ext import commands
import random

class Maple(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="메이플", pass_context=True)
    async def maple(self, ctx):
        embed = discord.Embed(title="메이플 편의기능", description="", color=0xFAE0D4)
        embed.add_field(name="직업뽑기  (🎲)", value="봇이 직업을 무작위로 뽑아줍니다. (링크/유니온 육성에 유용)", inline=False)
        embed.add_field(name="추옵  (\u2694)" ,value="무기의 추가옵션을 봅니다.", inline=False)
        embed.add_field(name="코강  (💎)" ,value="전직업 코어강화 정리", inline=False)
        embed.add_field(name="심볼  (❄)" ,value="심볼 강화 비용 계산", inline=False)
        embed.add_field(name="계산기  (🧮)" ,value="각종 계산 기능", inline=False)
        
        message = await ctx.send(embed=embed)

        for i in ["🎲", "\u2694", "💎", "❄", "🧮"]:
            await message.add_reaction(i)

        def check_m1(reaction, user):
            return user == ctx.author
        try:
            reaction, user = await self.bot.wait_for("reaction_add", timeout=10, check=check_m1)
            if str(reaction.emoji) == "🎲":
                embed = discord.Embed(title="직업뽑기", description="분류를 선택하세요.", color=0xFAE0D4)
                embed.add_field(name="모든 직업  (🎲)" ,value="전체 직업 중 랜덤 추출", inline=False)
                embed.add_field(name="직업  (🕐)" ,value="ex) 전사, 궁수, 도적 등", inline=False)
                embed.add_field(name="종족[소속]  (🕑)" ,value="ex) 모험가, 영웅, 노바 ...", inline=False)
                message = await ctx.send(embed=embed)

                await message.add_reaction('🎲')
                await message.add_reaction('🕐')
                await message.add_reaction('🕑')
                
                def check_m6(reaction, user):
                    return user == ctx.author
                try:
                    reaction, user = await self.bot.wait_for("reaction_add", timeout=10, check=check_m6)
                    if str(reaction.emoji) == '🎲':
                        all_jobs = [
                            '히어로', '팔라딘', '다크나이트', '아크메이지(불,독)', '아크메이지(썬,콜)', '비숍', '보우마스터',
                            '신궁', '패스파인더', '나이트로드', '섀도어', '듀얼블레이드', '바이퍼', '캡틴', '캐논슈터', '소울마스터',
                            '미하일', '플레임위자드', '윈드브레이커', '나이트워커', '스트라이커', '블래스터', '배틀메이지',
                            '와일드헌터', '메카닉', '제논', '데몬슬레이어', '데몬어벤져', '아란', '에반', '루미너스', '메르세데스',
                            '팬텀', ' ', '카이저', '카인', '카데나', '엔젤릭버스터', '아델', '일리움', '아크',
                            '라라', '호영', '제로', '키네시스'
                        ]
                        picked = random.sample(all_jobs, 1)
                        await ctx.send("%s" %picked)
                    elif str(reaction.emoji) == '🕐':
                        embed = discord.Embed(title="직업뽑기", description="직업별", color=0xFAE0D4)
                        embed.add_field(name="전사 직업군" ,value="⚔️", inline=False)
                        embed.add_field(name="마법사 직업군" ,value="🔮", inline=False)
                        embed.add_field(name="궁수 직업군" ,value="🏹", inline=False)
                        embed.add_field(name="도적 직업군" ,value="🔪", inline=False)
                        embed.add_field(name="해적 직업군" ,value="🔫", inline=False)
                        message = await ctx.send(embed=embed)

                        await message.add_reaction('⚔️')
                        await message.add_reaction('🔮')
                        await message.add_reaction('🏹')
                        await message.add_reaction('🔪')
                        await message.add_reaction('🔫')

                        def check_m7(reaction, user):
                            return user == ctx.author
                        try:
                            reaction, user = await self.bot.wait_for("reaction_add", timeout=10, check=check_m7)
                            if str(reaction.emoji) == '⚔️':
                                warrior = [
                                    '히어로', '팔라딘', '다크나이트', '소울마스터', '미하일', '블래스터',
                                    '데몬슬레이어', '데몬어벤져', '아란', '카이저', '아델', '제로'
                                ]
                                picked = random.sample(warrior, 1)
                                await ctx.send("%s" %picked)
                            elif str(reaction.emoji) == '🔮':
                                mage = [
                                    '아크메이지(불,독)', '아크메이지(썬,콜)', '비숍', '플레임위자드', '배틀메이지', '에반', '루미너스',
                                    '일리움', '라라', '키네시스'
                                ]
                                picked = random.sample(mage, 1)
                                await ctx.send("%s" %picked)
                            elif str(reaction.emoji) == '🏹':
                                archer = [
                                    '보우마스터', '신궁', '패스파인더', '윈드브레이커', '와일드헌터', '메르세데스', '카인'
                                ]
                                picked = random.sample(archer, 1)
                                await ctx.send("%s" %picked)
                            elif str(reaction.emoji) == '🔪':
                                assesin = [
                                    '나이트로드', '섀도어', '듀얼블레이드', '나이트워커', '제논', '팬텀', '카데나', '호영'
                                ]
                                picked = random.sample(assesin, 1)
                                await ctx.send("%s" %picked)
                            elif str(reaction.emoji) == '🔫':
                                gun = [
                                    '바이퍼', '캡틴', '캐논슈터', '스트라이커', '메카닉', '제논', ' ', '엔젤릭버스터', '아크'
                                ]
                                picked = random.sample(gun, 1)
                                await ctx.send("%s" %picked)
                        except asyncio.TimeoutError:
                            await ctx.send("입력 시간 초과")
                    elif str(reaction.emoji) == '🕑':
                        embed = discord.Embed(title="직업뽑기", description="종족(소속)별", color=0xFAE0D4)
                        embed.add_field(name="모험가" ,value="⚔️", inline=False)
                        embed.add_field(name="시그너스 기사단" ,value="🛡️", inline=False)
                        embed.add_field(name="레지스탕스" ,value="⚙️", inline=False)
                        embed.add_field(name="영웅" ,value="🦋", inline=False)
                        embed.add_field(name="노바" ,value="🐉", inline=False)
                        embed.add_field(name="레프" ,value="🧝", inline=False)
                        embed.add_field(name="아니마" ,value="🐰", inline=False)
                        embed.add_field(name="초월자/초능력자" ,value="👑", inline=False)
                        message = await ctx.send(embed=embed)

                        for i in ['⚔️', '🛡️', '⚙️', '🦋', '🐉', '🧝', '🐰', '👑']:
                            await message.add_reaction(i)

                        def check_m8(reaction, user):
                            return user == ctx.author
                        try:
                            reaction, user = await self.bot.wait_for("reaction_add", timeout=10, check=check_m8)
                            if str(reaction.emoji) == '⚔️':
                                adventure = [
                                    '히어로', '팔라딘', '다크나이트', '아크메이지(불,독)', '아크메이지(썬,콜)', '비숍', '보우마스터',
                                    '신궁', '패스파인더', '나이트로드', '섀도어', '듀얼블레이드', '바이퍼', '캡틴', '캐논슈터'
                                ]
                                picked = random.sample(adventure, 1)
                                await ctx.send("%s" %picked)
                            elif str(reaction.emoji) == '🛡️':
                                knights = [
                                    '소울마스터', '미하일', '플레임위자드', '윈드브레이커', '나이트워커',
                                    '스트라이커'
                                ]
                                picked = random.sample(knights, 1)
                                await ctx.send("%s" %picked)
                            elif str(reaction.emoji) == '⚙️':
                                resistance = [
                                    '블래스터', '배틀메이지', '와일드헌터', '메카닉', '제논',
                                    '데몬슬레이어', '데몬어벤져'
                                ]
                                picked = random.sample(resistance, 1)
                                await ctx.send("%s" %picked)
                            elif str(reaction.emoji) == '🦋':
                                hero = [
                                    '아란', '에반', '루미너스', '메르세데스', '팬텀', ' '
                                ]
                                picked = random.sample(hero, 1)
                                await ctx.send("%s" %picked)
                            elif str(reaction.emoji) == '🐉':
                                nova = [
                                    '카이저', '카인', '카데나', '엔젤릭버스터'
                                ]
                                picked = random.sample(nova, 1)
                                await ctx.send("%s" %picked)
                            elif str(reaction.emoji) == '🧝':
                                reff = [
                                    '아델', '일리움', '아크'
                                ]
                                picked = random.sample(reff, 1)
                                await ctx.send("%s" %picked)
                            elif str(reaction.emoji) == '🐰':
                                anima = [
                                    '라라', '호영'
                                ]
                                picked = random.sample(anima, 1)
                                await ctx.send("%s" %picked)
                            elif str(reaction.emoji) == '👑':
                                superior = [
                                    '제로', '키네시스'
                                ]
                                picked = random.sample(superior, 1)
                                await ctx.send("%s" %picked)
                        except asyncio.TimeoutError:
                            await ctx.send("입력 시간 초과")
                except asyncio.TimeoutError:
                    await ctx.send("입력 시간 초과")
            elif str(reaction.emoji) == "\u2694":
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
                        embed.set_image(url='https://postfiles.pstatic.net/MjAyMDA4MjdfMTI3/MDAxNTk4NTEyNDgxMjMw.a98DwNNZKZI3ickoniMc2Gg7ydi22-gTbO95ZYthWUcg.5Rmy6QtesPH9eX559vqm1qY2fz233YLFp2RMiM26koUg.PNG.khs20010327/1598512478511.png?type=w773')
                        embed.set_footer(text='출처 : https://blog.naver.com/khs20010327/222072627480')
                        await ctx.send(embed=embed)
                    elif str(reaction.emoji) == '🕑':
                        embed = discord.Embed()
                        embed.set_image(url='https://postfiles.pstatic.net/MjAyMDA4MjdfNDAg/MDAxNTk4NTEyNDgzNDgy.sMaxGixBHfX6MLc8fh1zrzTDAe7sXNfk1E8_QBVwXrMg.kcSI6R_ePzj6NcoMLXmNkGdrSSpodhcZex14a_t3yLAg.PNG.khs20010327/1598512480239.png?type=w773')
                        embed.set_footer(text='출처 : https://blog.naver.com/khs20010327/222072627480')
                        await ctx.send(embed=embed)
                    elif str(reaction.emoji) == '🕒':
                        embed = discord.Embed()
                        embed.set_image(url='https://postfiles.pstatic.net/MjAyMDA4MjdfMTEx/MDAxNTk4NTEyNDg4MzA0.n5owscR_Qu9axvL8s8BRcJLAmAcZIteKKo5OZjgk72Ug.faaU0KcLHHBQr6USShNYFgRXu8V5zxRO6DHAe9fU0xMg.PNG.khs20010327/1598512483475.png?type=w773')
                        embed.set_footer(text='출처 : https://blog.naver.com/khs20010327/222072627480')
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
            elif str(reaction.emoji) == '🧮':
                embed = discord.Embed(title="계산 기능", description="", color=0xFAE0D4)
                embed.add_field(name="보스 방무 딜 계산  (🛡️)" ,value="보스에게 들어가는 실제 데미지를 계산합니다.", inline=False)
                embed.add_field(name="극성비 경험치 계산  (🧪)" ,value="극성비 사용 후 예상 레벨을 계산합니다", inline=False)
                message = await ctx.send(embed=embed)
                for i in ['🕐']:
                    await message.add_reaction(i)
                def check_m6(reaction, user):
                    return user == ctx.author
                try:
                    reaction, user = await self.bot.wait_for("reaction_add", timeout=10, check=check_m6)
                    if str(reaction.emoji) == '🕐':
                        await ctx.send("보스의 방어율을 입력해주세요. (0 이상)")
                        def check_m7(message):
                            return message.author == ctx.author and message.content.isdigit() and int(message.content) >= 0
                        try:
                            message = await self.bot.wait_for("message", timeout=10, check=check_m7)
                            boss = int(message.content)
                            await ctx.send("자신의 방어 무시율을 입력해주세요. (0 이상, 소수점 아래 2자리까지)")
                            def check_m8(message):
                                return message.author == ctx.author and float(message.content) >= 0
                            try:
                                message = await self.bot.wait_for("message", timeout=10, check=check_m8)
                                ignore = float(message.content)
                                result = 100 - (boss * (1.0 - ignore * 0.01))
                                await ctx.send("해당 보스에게 " + str(round(result, 2)) + " % 만큼 딜이 들어갑니다.")
                            except ValueError:
                                await ctx.send("숫자를 입력해주세요")
                            except asyncio.TimeoutError:
                                await ctx.send("입력 시간 초과")
                        except asyncio.TimeoutError:
                            await ctx.send("입력 시간 초과")
                    elif str(reaction.emoji) == '🧪':
                        await ctx.send("레벨과 경험치 비율(%), 극성비 개수를 입력해주세요. (띄어쓰기로 구분)\nex) 261 10.597 2")
                        def check_m9(message):
                            def isfloat(num):
                                try:
                                    float(num)
                                    return True
                                except ValueError:
                                    return False
                            parsed = message.content.split()
                            return message.author == ctx.author and len(parsed) >= 2 and parsed[0].isdigit() and isfloat(parsed[1])
                        try:
                            message = await self.bot.wait_for("message", timeout=15, check=check_m9)
                            parsed = message.content.split()
                            gsb_count = 0
                            if len(parsed) == 2:
                                gsb_count = 1
                            else:
                                if int(parsed[2]) > 100:
                                    await ctx.send("최대 100개의 극성비만 계산할 수 있습니다.")
                                    return
                                gsb_count = int(parsed[2])
                            if int(parsed[0]) < 200:
                                await ctx.send("극한 성장의 비약은 200레벨 이상의 캐릭터만 사용할 수 있습니다.")
                                return
                            if int(parsed[0]) >= 300:
                                embed = discord.Embed(title="극성비", description="", color=0xCBDD61)
                                embed.add_field(name="예상 레벨" ,value="Lv.300 -> Lv.300", inline=False)
                                embed.add_field(name="예상 경험치량" ,value="0.000 % -> 0.000 %", inline=False)
                                await ctx.send(embed=embed)
                            df = pd.read_csv('./exp.csv', names = ['lv', 'exp', 'cum'])
                            lv = int(parsed[0])
                            find_row = df.loc[df['lv'] == int(parsed[0])]
                            gsb = 0
                            req_exp = int(list(find_row['exp'])[0]) # 경험치 요구량
                            cur_exp = req_exp * (float(parsed[1]) / 100.0) # 현재 경험치
                            ratio = 0.0
                            predict_exp = 0
                            for _ in range(gsb_count):
                                if lv < 250:
                                    gsb = req_exp
                                else:
                                    gsb = 627637515116
                                predict_exp = cur_exp + gsb
                                if (predict_exp > req_exp):
                                    lv += 1
                                    find_row = df.loc[df['lv'] == lv]
                                    cur_exp = predict_exp - req_exp
                                else:
                                    cur_exp = predict_exp
                                try:
                                    req_exp = int(list(find_row['exp'])[0])
                                except IndexError:
                                    embed = discord.Embed(title="극성비", description="", color=0xCBDD61)
                                    embed.add_field(name="예상 레벨" ,value="Lv.{} -> Lv.300".format(parsed[0]), inline=False)
                                    embed.add_field(name="예상 경험치량" ,value="{} % -> 0.000 %".format(parsed[1]), inline=False)
                                    await ctx.send(embed=embed)
                                    return None
                                ratio = cur_exp / req_exp * 100.0
                            if ratio == 100.0:
                                lv += 1
                                ratio = 0.0
                            embed = discord.Embed(title="극성비", description="", color=0xCBDD61)
                            embed.add_field(name="예상 레벨" ,value="Lv.{} -> Lv.{}".format(parsed[0], lv), inline=False)
                            embed.add_field(name="예상 경험치량" ,value="{} % -> {} %".format(parsed[1], round(ratio, 3)), inline=False)
                            await ctx.send(embed=embed)
                        except asyncio.TimeoutError:
                            await ctx.send("입력 시간 초과")
                except asyncio.TimeoutError:
                    await ctx.send("입력 시간 초과")
                
        except asyncio.TimeoutError:
            await ctx.send("입력 시간 초과")

    @commands.command(name="극성비", pass_context=True)
    async def gsb(self, ctx):
        await ctx.send("레벨과 경험치 비율(%), 극성비 개수를 입력해주세요. (띄어쓰기로 구분)\nex) 261 10.597 2")
        def check_m10(message):
            def isfloat(num):
                try:
                    float(num)
                    return True
                except ValueError:
                    return False
            parsed = message.content.split()
            return message.author == ctx.author and len(parsed) >= 2 and parsed[0].isdigit() and isfloat(parsed[1])
        try:
            message = await self.bot.wait_for("message", timeout=15, check=check_m10)
            parsed = message.content.split()
            gsb_count = 0
            if len(parsed) == 2:
                gsb_count = 1
            else:
                if int(parsed[2]) > 100:
                    await ctx.send("최대 100개의 극성비만 계산할 수 있습니다.")
                    return
                gsb_count = int(parsed[2])
            if int(parsed[0]) < 200:
                await ctx.send("극한 성장의 비약은 200레벨 이상의 캐릭터만 사용할 수 있습니다.")
                return
            if int(parsed[0]) >= 300:
                embed = discord.Embed(title="극성비", description="", color=0xCBDD61)
                embed.add_field(name="예상 레벨" ,value="Lv.300 -> Lv.300", inline=False)
                embed.add_field(name="예상 경험치량" ,value="0.000 % -> 0.000 %", inline=False)
                await ctx.send(embed=embed)
            df = pd.read_csv('./exp.csv', names = ['lv', 'exp', 'cum'])
            lv = int(parsed[0])
            find_row = df.loc[df['lv'] == int(parsed[0])]
            gsb = 0
            req_exp = int(list(find_row['exp'])[0]) # 경험치 요구량
            cur_exp = req_exp * (float(parsed[1]) / 100.0) # 현재 경험치
            ratio = 0.0
            predict_exp = 0
            for _ in range(gsb_count):
                if lv < 250:
                    gsb = req_exp
                else:
                    gsb = 627637515116
                predict_exp = cur_exp + gsb
                if (predict_exp > req_exp):
                    lv += 1
                    find_row = df.loc[df['lv'] == lv]
                    cur_exp = predict_exp - req_exp
                else:
                    cur_exp = predict_exp
                try:
                    req_exp = int(list(find_row['exp'])[0])
                except IndexError:
                    embed = discord.Embed(title="극성비", description="", color=0xCBDD61)
                    embed.add_field(name="예상 레벨" ,value="Lv.{} -> Lv.300".format(parsed[0]), inline=False)
                    embed.add_field(name="예상 경험치량" ,value="{} % -> 0.000 %".format(parsed[1]), inline=False)
                    await ctx.send(embed=embed)
                    return None
                ratio = cur_exp / req_exp * 100.0
            if ratio == 100.0:
                lv += 1
                ratio = 0.0
            embed = discord.Embed(title="극성비", description="", color=0xCBDD61)
            embed.add_field(name="예상 레벨" ,value="Lv.{} -> Lv.{}".format(parsed[0], lv), inline=False)
            embed.add_field(name="예상 경험치량" ,value="{} % -> {} %".format(parsed[1], round(ratio, 3)), inline=False)
            await ctx.send(embed=embed)
        except asyncio.TimeoutError:
            await ctx.send("입력 시간 초과")

def setup(bot):
    bot.add_cog(Maple(bot))