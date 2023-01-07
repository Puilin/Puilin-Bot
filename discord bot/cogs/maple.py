import asyncio
import discord
from discord import app_commands
from discord.ext import commands
import random
import pandas as pd


class Maple(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    
    @app_commands.command(name="메이플", description="메이플 편의기능 호출")
    async def maple(self, interaction :discord.Interaction):
        ctx = await commands.Context.from_interaction(interaction)

        async def choose_job(interaction):

            async def all_jobs(interaction):
                all_jobs = [
                        '히어로', '팔라딘', '다크나이트', '아크메이지(불,독)', '아크메이지(썬,콜)', '비숍', '보우마스터',
                        '신궁', '패스파인더', '나이트로드', '섀도어', '듀얼블레이드', '바이퍼', '캡틴', '캐논슈터', '소울마스터',
                        '미하일', '플레임위자드', '윈드브레이커', '나이트워커', '스트라이커', '블래스터', '배틀메이지',
                        '와일드헌터', '메카닉', '제논', '데몬슬레이어', '데몬어벤져', '아란', '에반', '루미너스', '메르세데스',
                        '팬텀', ' ', '카이저', '카인', '카데나', '엔젤릭버스터', '아델', '일리움', '칼리', '아크',
                        '라라', '호영', '제로', '키네시스'
                    ]
                picked = random.sample(all_jobs, 1)
                await interaction.response.send_message("%s" %picked)

            async def categorical(interaction):

                async def warrior(interaction):
                    warrior = [
                            '히어로', '팔라딘', '다크나이트', '소울마스터', '미하일', '블래스터',
                            '데몬슬레이어', '데몬어벤져', '아란', '카이저', '아델', '제로'
                        ]
                    picked = random.sample(warrior, 1)
                    await interaction.response.send_message("%s" %picked)
                
                async def mage(interaction):
                    mage = [
                            '아크메이지(불,독)', '아크메이지(썬,콜)', '비숍', '플레임위자드', '배틀메이지', '에반', '루미너스',
                            '일리움', '라라', '키네시스'
                        ]
                    picked = random.sample(mage, 1)
                    await interaction.response.send_message("%s" %picked)
                
                async def archer(interaction):
                    archer = [
                            '보우마스터', '신궁', '패스파인더', '윈드브레이커', '와일드헌터', '메르세데스', '카인'
                        ]
                    picked = random.sample(archer, 1)
                    await interaction.response.send_message("%s" %picked)
                
                async def logue(interaction):
                    assesin = [
                            '나이트로드', '섀도어', '듀얼블레이드', '나이트워커', '제논', '팬텀', '카데나', '칼리', '호영'
                        ]
                    picked = random.sample(assesin, 1)
                    await interaction.response.send_message("%s" %picked)
                
                async def gunner(interaction):
                    gun = [
                            '바이퍼', '캡틴', '캐논슈터', '스트라이커', '메카닉', '제논', ' ', '엔젤릭버스터', '아크'
                        ]
                    picked = random.sample(gun, 1)
                    await interaction.response.send_message("%s" %picked)
                
                embed = discord.Embed(title="직업뽑기", description="직업별", color=0xFAE0D4)
                embed.add_field(name="전사 직업군" ,value="⚔️", inline=False)
                embed.add_field(name="마법사 직업군" ,value="🔮", inline=False)
                embed.add_field(name="궁수 직업군" ,value="🏹", inline=False)
                embed.add_field(name="도적 직업군" ,value="🔪", inline=False)
                embed.add_field(name="해적 직업군" ,value="🔫", inline=False)

                view = discord.ui.View(timeout=10.0)
                button1 = discord.ui.Button(label="전사 직업군", emoji="⚔️")
                button2 = discord.ui.Button(label="마법사 직업군", emoji="🔮")
                button3 = discord.ui.Button(label="궁수 직업군", emoji="🏹")
                button4 = discord.ui.Button(label="도적 직업군", emoji="🔪")
                button5 = discord.ui.Button(label="해적 직업군", emoji="🔫")

                button1.callback = warrior
                button2.callback = mage
                button3.callback = archer
                button4.callback = logue
                button5.callback = gunner

                view.add_item(button1)
                view.add_item(button2)
                view.add_item(button3)
                view.add_item(button4)
                view.add_item(button5)

                await interaction.response.send_message(embed=embed, view=view)

            async def race(interaction):

                async def adventure(interaction):
                    adventure = [
                            '히어로', '팔라딘', '다크나이트', '아크메이지(불,독)', '아크메이지(썬,콜)', '비숍', '보우마스터',
                            '신궁', '패스파인더', '나이트로드', '섀도어', '듀얼블레이드', '바이퍼', '캡틴', '캐논슈터'
                        ]
                    picked = random.sample(adventure, 1)
                    await interaction.response.send_message("%s" %picked)
                
                async def knights(interaction):
                    knights = [
                            '소울마스터', '미하일', '플레임위자드', '윈드브레이커', '나이트워커',
                            '스트라이커'
                        ]
                    picked = random.sample(knights, 1)
                    await interaction.response.send_message("%s" %picked)
                
                async def resistance(interaction):
                    resistance = [
                            '블래스터', '배틀메이지', '와일드헌터', '메카닉', '제논',
                            '데몬슬레이어', '데몬어벤져'
                        ]
                    picked = random.sample(resistance, 1)
                    await interaction.response.send_message("%s" %picked)
                
                async def hero(interaction):
                    hero = [
                            '아란', '에반', '루미너스', '메르세데스', '팬텀', ' '
                        ]
                    picked = random.sample(hero, 1)
                    await interaction.response.send_message("%s" %picked)
                
                async def nova(interaction):
                    nova = [
                            '카이저', '카인', '카데나', '엔젤릭버스터'
                        ]
                    picked = random.sample(nova, 1)
                    await interaction.response.send_message("%s" %picked)
                
                async def reff(interaction):
                    reff = [
                            '아델', '일리움', '칼리', '아크'
                        ]
                    picked = random.sample(reff, 1)
                    await interaction.response.send_message("%s" %picked)
                
                async def anima(interaction):
                    anima = [
                            '라라', '호영'
                        ]
                    picked = random.sample(anima, 1)
                    await interaction.response.send_message("%s" %picked)
                
                async def superior(interaction):
                    superior = [
                            '제로', '키네시스'
                        ]
                    picked = random.sample(superior, 1)
                    await interaction.response.send_message("%s" %picked)
                
                embed = discord.Embed(title="직업뽑기", description="종족(소속)별", color=0xFAE0D4)
                embed.add_field(name="모험가" ,value="⚔️", inline=False)
                embed.add_field(name="시그너스 기사단" ,value="🛡️", inline=False)
                embed.add_field(name="레지스탕스" ,value="⚙️", inline=False)
                embed.add_field(name="영웅" ,value="🦋", inline=False)
                embed.add_field(name="노바" ,value="🐉", inline=False)
                embed.add_field(name="레프" ,value="🧝", inline=False)
                embed.add_field(name="아니마" ,value="🐰", inline=False)
                embed.add_field(name="초월자/초능력자" ,value="👑", inline=False)

                view = discord.ui.View()
                button1 = discord.ui.Button(label="모험가", emoji="⚔️")
                button2 = discord.ui.Button(label="시그너스 기사단", emoji="🛡️")
                button3 = discord.ui.Button(label="레지스탕스", emoji="⚙️")
                button4 = discord.ui.Button(label="영웅", emoji="🦋")
                button5 = discord.ui.Button(label="노바", emoji="🐉")
                button6 = discord.ui.Button(label="레프", emoji="🧝")
                button7 = discord.ui.Button(label="아니마", emoji="🐰")
                button8 = discord.ui.Button(label="초월자/초능력자", emoji="👑")

                button1.callback = adventure
                button2.callback = knights
                button3.callback = resistance
                button4.callback = hero
                button5.callback = nova
                button6.callback = reff
                button7.callback = anima
                button8.callback = superior

                view.add_item(button1)
                view.add_item(button2)
                view.add_item(button3)
                view.add_item(button4)
                view.add_item(button5)
                view.add_item(button6)
                view.add_item(button7)
                view.add_item(button8)

                await interaction.response.send_message(embed=embed, view=view)
        
            embed = discord.Embed(title="직업뽑기", description="분류를 선택하세요.", color=0xFAE0D4)
            embed.add_field(name="모든 직업  (🎲)" ,value="전체 직업 중 랜덤 추출", inline=False)
            embed.add_field(name="직업  (🕐)" ,value="ex) 전사, 궁수, 도적 등", inline=False)
            embed.add_field(name="종족[소속]  (🕑)" ,value="ex) 모험가, 영웅, 노바 ...", inline=False)

            view = discord.ui.View(timeout=10.0)
            button1 = discord.ui.Button(label="모든 직업", emoji="🎲")
            button2 = discord.ui.Button(label="직업", emoji="🕐")
            button3 = discord.ui.Button(label="종족[소속]", emoji="🕑")
            
            button1.callback = all_jobs
            button2.callback = categorical
            button3.callback = race
            
            view.add_item(button1)
            view.add_item(button2)
            view.add_item(button3)

            await interaction.response.send_message(embed=embed, view=view)
                    
        async def choo_op(interaction):

            async def papnir(interaction):
                embed = discord.Embed()
                embed.set_image(url='https://postfiles.pstatic.net/MjAyMzAxMDJfMjYg/MDAxNjcyNjQ0MTQzNTQ4.POCKM0PIgFOSe9dyjE-Nm5H9RAnIoiufMjMw_gOKJj0g.ioV1c-scnlP1--EpUyLm8fnDnQ6UDf901ZrQJrPW8sIg.PNG.suryblue/i13353553723.png?type=w966')
                embed.set_footer(text='출처 : https://blog.naver.com/hongs1904/222221149711')
                await interaction.response.send_message(embed=embed)
            
            async def absolas(interaction):
                embed = discord.Embed()
                embed.set_image(url='https://postfiles.pstatic.net/MjAyMzAxMDJfNDkg/MDAxNjcyNjQ0MTQzNDkx.RGh9YDENkFYrmgDL47MpfwWZCe84AjIxpsB_rn0GrvIg.PVatc2BGqddXOeB87i-uV9eL5I3tRg7gdTH7wr6axCEg.PNG.suryblue/i13318233624.png?type=w966')
                embed.set_footer(text='출처 : https://blog.naver.com/hongs1904/222221149711')
                await interaction.response.send_message(embed=embed)
            
            async def arcane(interaction):
                embed = discord.Embed()
                embed.set_image(url='https://postfiles.pstatic.net/MjAyMzAxMDJfMTU1/MDAxNjcyNjQ0MTQzNTU2.yQNMXw5DLVjLojuSc3vD-rfLhpxlHrmSXmla7gKjmAEg.4qZJSB0R4Zcwnu0L4bULmORSc1tUoe9PSZKszO5vpm0g.PNG.suryblue/i13384268658.png?type=w966')
                embed.set_footer(text='출처 : https://blog.naver.com/hongs1904/222221149711')
                await interaction.response.send_message(embed=embed)
            
            async def genesis(interaction):
                embed = discord.Embed()
                embed.set_image(url='https://postfiles.pstatic.net/MjAyMzAxMDJfMjg3/MDAxNjcyNjQ0MTQzNTYw.cmpxf_w1o_F3jkCrrzbw4VMpB-7UbpHjgJB4xbXHXzQg.HYnlpbCgsFDB9T9B8-usoSyRb81HU0rggfRj-D2GFqsg.PNG.suryblue/i13351743797.png?type=w966')
                embed.set_footer(text='출처 : https://blog.naver.com/hongs1904/222221149711')
                await interaction.response.send_message(embed=embed)
            
            embed = discord.Embed(title="추옵", description="", color=0xFAE0D4)
            embed.add_field(name="파프니르  (🕐)" ,value="150제", inline=False)
            embed.add_field(name="앱솔랩스  (🕑)" ,value="160제", inline=False)
            embed.add_field(name="아케인셰이드  (🕒)" ,value="200제", inline=False)
            embed.add_field(name="제네시스  (🕓)" ,value="200제", inline=False)

            view = discord.ui.View()
            button1 = discord.ui.Button(label="파프니르", emoji="🕐")
            button2 = discord.ui.Button(label="앱솔랩스", emoji="🕑")
            button3 = discord.ui.Button(label="아케인셰이드", emoji="🕒")
            button4 = discord.ui.Button(label="제네시스", emoji="🕓")

            button1.callback = papnir
            button2.callback = absolas
            button3.callback = arcane
            button4.callback = genesis

            view.add_item(button1)
            view.add_item(button2)
            view.add_item(button3)
            view.add_item(button4)

            await interaction.response.send_message(embed=embed, view=view)
        
        async def cogang(interaction):
            await interaction.response.send_message("https://www.youtube.com/watch?v=x1CzCgimoVA")
        
        async def symbol(interaction):

            class text_modal(discord.ui.Modal):
                level = discord.ui.TextInput(label="현재 심볼의 레벨을 입력해주세요", placeholder="1")
                self.level = level

                def __init__(self, base:int, coef:int):
                    super().__init__(title='아케인심볼 강화', timeout=30.0, custom_id="sym")
                    self.base = base
                    self.coef = coef

                async def on_submit(self, interaction):
                    if not self.level.value.isdigit() or int(self.level.value) > 20 or int(self.level.value) < 1:
                        await interaction.response.send_message("1~20 사이의 숫자를 입력해주세요.")
                        return
                    if int(self.level.value) == 20:
                        await interaction.response.send_message("최대 레벨입니다.")
                        return
                    meso = self.base + int(self.level.value) * self.coef
                    growth = int(self.level.value)**2 + 11
                    await interaction.response.send_message("lv.%d -> lv.%d\n필요 성장치 : %d\n강화 비용 : %d 메소" %(int(self.level.value), int(self.level.value) + 1 ,growth,meso))

            async def yeoro(interaction):
                await interaction.response.send_modal(text_modal(3110000, 3960000))
            
            async def chuchu(interaction):
                await interaction.response.send_modal(text_modal(6220000, 4620000))
            
            async def lachelen(interaction):
                await interaction.response.send_modal(text_modal(9330000, 5280000))
            
            async def etc(interaction):
                await interaction.response.send_modal(text_modal(11196000, 5940000))

            embed = discord.Embed(title="심볼", description="", color=0xFAE0D4)
            embed.add_field(name="소멸의 여로  (🕐)" ,value="lv.200", inline=False)
            embed.add_field(name="츄츄 아일랜드 (🕑)" ,value="lv.210", inline=False)
            embed.add_field(name="레헬른  (🕒)" ,value="lv.220", inline=False)
            embed.add_field(name="아르카나~에스페라  (🕓)" ,value="lv.225~235", inline=False)

            view = discord.ui.View()
            button1 = discord.ui.Button(label="소멸의 여로", emoji="🕐")
            button2 = discord.ui.Button(label="츄츄 아일랜드", emoji="🕑")
            button3 = discord.ui.Button(label="레헬른", emoji="🕒")
            button4 = discord.ui.Button(label="아르카나~에스페라", emoji="🕓")

            button1.callback = yeoro
            button2.callback = chuchu
            button3.callback = lachelen
            button4.callback = etc

            view.add_item(button1)
            view.add_item(button2)
            view.add_item(button3)
            view.add_item(button4)
            
            await interaction.response.send_message(embed=embed, view=view)
            
        async def calc(interaction):

            async def boss(interaction):
                await interaction.response.send_message("보스의 방어율을 입력해주세요. (0 이상)")
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
            
            async def gsb(interaction: discord.Interaction):
                await interaction.response.send_message("레벨과 경험치 비율(%), 극성비 개수를 입력해주세요. (띄어쓰기로 구분)\nex) 261 10.597 2")
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
                            await interaction.response.send_message("최대 100개의 극성비만 계산할 수 있습니다.")
                            return
                        gsb_count = int(parsed[2])
                    if int(parsed[0]) < 200:
                        await interaction.response.send_message("극한 성장의 비약은 200레벨 이상의 캐릭터만 사용할 수 있습니다.")
                        return
                    if int(parsed[0]) >= 300:
                        embed = discord.Embed(title="극성비", description="", color=0xCBDD61)
                        embed.add_field(name="예상 레벨" ,value="Lv.300 -> Lv.300", inline=False)
                        embed.add_field(name="예상 경험치량" ,value="0.000 % -> 0.000 %", inline=False)
                        await interaction.response.send_message(embed=embed)
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
                        if (predict_exp >= req_exp):
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
                    embed = discord.Embed(title="극성비", description="", color=0xCBDD61)
                    embed.add_field(name="예상 레벨" ,value="Lv.{} -> Lv.{}".format(parsed[0], lv), inline=False)
                    embed.add_field(name="예상 경험치량" ,value="{} % -> {} %".format(parsed[1], round(ratio, 3)), inline=False)
                    await interaction.response.send_message(embed=embed)
                except asyncio.TimeoutError:
                    await interaction.response.send_message("입력 시간 초과")
            
            embed = discord.Embed(title="계산 기능", description="", color=0xFAE0D4)
            embed.add_field(name="보스 방무 딜 계산  (🛡️)" ,value="보스에게 들어가는 실제 데미지를 계산합니다.", inline=False)
            embed.add_field(name="극성비 경험치 계산  (🧪)" ,value="극성비 사용 후 예상 레벨을 계산합니다", inline=False)

            view = discord.ui.View()
            button1 = discord.ui.Button(label="방무 딜계산", emoji="🛡️")
            button2 = discord.ui.Button(label="극성비 경험치 계산", emoji="🧪")

            button1.callback = boss
            button2.callback = gsb

            view.add_item(button1)
            view.add_item(button2)

            await interaction.response.send_message(embed=embed, view=view)

        async def protect_espera(interaction):
            embed1 = discord.Embed(color=0xa2cd5a)
            embed2 = discord.Embed(color=0xa2cd5a)
            embed1.set_image(url="https://upload3.inven.co.kr/upload/2021/08/24/bbs/i13535684383.png?MW=800")
            embed2.set_image(url="https://upload3.inven.co.kr/upload/2021/08/24/bbs/i14155987428.png?MW=800")
            embed2.set_footer(text="출처 : https://www.inven.co.kr/board/maple/2304/28788")
            embeds = [embed1, embed2]
            await interaction.response.send_message(embeds=embeds)
        
        embed = discord.Embed(title="메이플 편의기능", description="", color=0xFAE0D4)
        embed.add_field(name="직업뽑기  (🎲)", value="봇이 직업을 무작위로 뽑아줍니다. (링크/유니온 육성에 유용)", inline=False)
        embed.add_field(name="추옵  (\u2694)" ,value="무기의 추가옵션을 봅니다.", inline=False)
        embed.add_field(name="코강  (💎)" ,value="전직업 코어강화 정리", inline=False)
        embed.add_field(name="심볼  (❄)" ,value="심볼 강화 비용 계산", inline=False)
        embed.add_field(name="계산기  (🧮)" ,value="각종 계산 기능", inline=False)
        embed.add_field(name="프로텍트 에스페라  (💣)" ,value="프로텍트 에스페라 공략", inline=False)

        view = discord.ui.View(timeout=10.0)
        button1 = discord.ui.Button(label="직업뽑기", emoji="🎲")
        button2 = discord.ui.Button(label="추옵", emoji="\u2694")
        button3 = discord.ui.Button(label="코강", emoji="💎")
        button4 = discord.ui.Button(label="심볼", emoji="❄")
        button5 = discord.ui.Button(label="계산기", emoji="🧮")
        button6 = discord.ui.Button(label="프로텍트 에스페라", emoji="💣")

        button1.callback = choose_job
        button2.callback = choo_op
        button3.callback = cogang
        button4.callback = symbol
        button5.callback = calc
        button6.callback = protect_espera
        
        view.add_item(button1)
        view.add_item(button2)
        view.add_item(button3)
        view.add_item(button4)
        view.add_item(button5)
        view.add_item(button6)

        await interaction.response.send_message(embed=embed, view=view)

    @app_commands.command(name="극성비", description="극성비 사용 후 예상 레벨 계산")
    async def gsb(self, interaction: discord.Interaction):
        ctx = await commands.Context.from_interaction(interaction)
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
                if (predict_exp >= req_exp):
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
            embed = discord.Embed(title="극성비", description="", color=0xCBDD61)
            embed.add_field(name="예상 레벨" ,value="Lv.{} -> Lv.{}".format(parsed[0], lv), inline=False)
            embed.add_field(name="예상 경험치량" ,value="{} % -> {} %".format(parsed[1], round(ratio, 3)), inline=False)
            await ctx.send(embed=embed)
        except asyncio.TimeoutError:
            await ctx.send("입력 시간 초과")

    @app_commands.command(name="직업뽑기", description="봇이 무작위로 직업을 뽑아줍니다.")
    async def choose_job_(self, interaction: discord.Interaction):
        async def all_jobs(interaction):
            all_jobs = [
                    '히어로', '팔라딘', '다크나이트', '아크메이지(불,독)', '아크메이지(썬,콜)', '비숍', '보우마스터',
                    '신궁', '패스파인더', '나이트로드', '섀도어', '듀얼블레이드', '바이퍼', '캡틴', '캐논슈터', '소울마스터',
                    '미하일', '플레임위자드', '윈드브레이커', '나이트워커', '스트라이커', '블래스터', '배틀메이지',
                    '와일드헌터', '메카닉', '제논', '데몬슬레이어', '데몬어벤져', '아란', '에반', '루미너스', '메르세데스',
                    '팬텀', ' ', '카이저', '카인', '카데나', '엔젤릭버스터', '아델', '일리움', '칼리', '아크',
                    '라라', '호영', '제로', '키네시스'
                ]
            picked = random.sample(all_jobs, 1)
            await interaction.response.send_message("%s" %picked)

        async def categorical(interaction):

            async def warrior(interaction):
                warrior = [
                        '히어로', '팔라딘', '다크나이트', '소울마스터', '미하일', '블래스터',
                        '데몬슬레이어', '데몬어벤져', '아란', '카이저', '아델', '제로'
                    ]
                picked = random.sample(warrior, 1)
                await interaction.response.send_message("%s" %picked)
            
            async def mage(interaction):
                mage = [
                        '아크메이지(불,독)', '아크메이지(썬,콜)', '비숍', '플레임위자드', '배틀메이지', '에반', '루미너스',
                        '일리움', '라라', '키네시스'
                    ]
                picked = random.sample(mage, 1)
                await interaction.response.send_message("%s" %picked)
            
            async def archer(interaction):
                archer = [
                        '보우마스터', '신궁', '패스파인더', '윈드브레이커', '와일드헌터', '메르세데스', '카인'
                    ]
                picked = random.sample(archer, 1)
                await interaction.response.send_message("%s" %picked)
            
            async def logue(interaction):
                assesin = [
                        '나이트로드', '섀도어', '듀얼블레이드', '나이트워커', '제논', '팬텀', '카데나', '칼리', '호영'
                    ]
                picked = random.sample(assesin, 1)
                await interaction.response.send_message("%s" %picked)
            
            async def gunner(interaction):
                gun = [
                        '바이퍼', '캡틴', '캐논슈터', '스트라이커', '메카닉', '제논', ' ', '엔젤릭버스터', '아크'
                    ]
                picked = random.sample(gun, 1)
                await interaction.response.send_message("%s" %picked)
            
            embed = discord.Embed(title="직업뽑기", description="직업별", color=0xFAE0D4)
            embed.add_field(name="전사 직업군" ,value="⚔️", inline=False)
            embed.add_field(name="마법사 직업군" ,value="🔮", inline=False)
            embed.add_field(name="궁수 직업군" ,value="🏹", inline=False)
            embed.add_field(name="도적 직업군" ,value="🔪", inline=False)
            embed.add_field(name="해적 직업군" ,value="🔫", inline=False)

            view = discord.ui.View(timeout=10.0)
            button1 = discord.ui.Button(label="전사 직업군", emoji="⚔️")
            button2 = discord.ui.Button(label="마법사 직업군", emoji="🔮")
            button3 = discord.ui.Button(label="궁수 직업군", emoji="🏹")
            button4 = discord.ui.Button(label="도적 직업군", emoji="🔪")
            button5 = discord.ui.Button(label="해적 직업군", emoji="🔫")

            button1.callback = warrior
            button2.callback = mage
            button3.callback = archer
            button4.callback = logue
            button5.callback = gunner

            view.add_item(button1)
            view.add_item(button2)
            view.add_item(button3)
            view.add_item(button4)
            view.add_item(button5)

            await interaction.response.send_message(embed=embed, view=view)

        async def race(interaction):

            async def adventure(interaction):
                adventure = [
                        '히어로', '팔라딘', '다크나이트', '아크메이지(불,독)', '아크메이지(썬,콜)', '비숍', '보우마스터',
                        '신궁', '패스파인더', '나이트로드', '섀도어', '듀얼블레이드', '바이퍼', '캡틴', '캐논슈터'
                    ]
                picked = random.sample(adventure, 1)
                await interaction.response.send_message("%s" %picked)
            
            async def knights(interaction):
                knights = [
                        '소울마스터', '미하일', '플레임위자드', '윈드브레이커', '나이트워커',
                        '스트라이커'
                    ]
                picked = random.sample(knights, 1)
                await interaction.response.send_message("%s" %picked)
            
            async def resistance(interaction):
                resistance = [
                        '블래스터', '배틀메이지', '와일드헌터', '메카닉', '제논',
                        '데몬슬레이어', '데몬어벤져'
                    ]
                picked = random.sample(resistance, 1)
                await interaction.response.send_message("%s" %picked)
            
            async def hero(interaction):
                hero = [
                        '아란', '에반', '루미너스', '메르세데스', '팬텀', ' '
                    ]
                picked = random.sample(hero, 1)
                await interaction.response.send_message("%s" %picked)
            
            async def nova(interaction):
                nova = [
                        '카이저', '카인', '카데나', '엔젤릭버스터'
                    ]
                picked = random.sample(nova, 1)
                await interaction.response.send_message("%s" %picked)
            
            async def reff(interaction):
                reff = [
                        '아델', '일리움', '칼리', '아크'
                    ]
                picked = random.sample(reff, 1)
                await interaction.response.send_message("%s" %picked)
            
            async def anima(interaction):
                anima = [
                        '라라', '호영'
                    ]
                picked = random.sample(anima, 1)
                await interaction.response.send_message("%s" %picked)
            
            async def superior(interaction):
                superior = [
                        '제로', '키네시스'
                    ]
                picked = random.sample(superior, 1)
                await interaction.response.send_message("%s" %picked)
            
            embed = discord.Embed(title="직업뽑기", description="종족(소속)별", color=0xFAE0D4)
            embed.add_field(name="모험가" ,value="⚔️", inline=False)
            embed.add_field(name="시그너스 기사단" ,value="🛡️", inline=False)
            embed.add_field(name="레지스탕스" ,value="⚙️", inline=False)
            embed.add_field(name="영웅" ,value="🦋", inline=False)
            embed.add_field(name="노바" ,value="🐉", inline=False)
            embed.add_field(name="레프" ,value="🧝", inline=False)
            embed.add_field(name="아니마" ,value="🐰", inline=False)
            embed.add_field(name="초월자/초능력자" ,value="👑", inline=False)

            view = discord.ui.View()
            button1 = discord.ui.Button(label="모험가", emoji="⚔️")
            button2 = discord.ui.Button(label="시그너스 기사단", emoji="🛡️")
            button3 = discord.ui.Button(label="레지스탕스", emoji="⚙️")
            button4 = discord.ui.Button(label="영웅", emoji="🦋")
            button5 = discord.ui.Button(label="노바", emoji="🐉")
            button6 = discord.ui.Button(label="레프", emoji="🧝")
            button7 = discord.ui.Button(label="아니마", emoji="🐰")
            button8 = discord.ui.Button(label="초월자/초능력자", emoji="👑")

            button1.callback = adventure
            button2.callback = knights
            button3.callback = resistance
            button4.callback = hero
            button5.callback = nova
            button6.callback = reff
            button7.callback = anima
            button8.callback = superior

            view.add_item(button1)
            view.add_item(button2)
            view.add_item(button3)
            view.add_item(button4)
            view.add_item(button5)
            view.add_item(button6)
            view.add_item(button7)
            view.add_item(button8)

            await interaction.response.send_message(embed=embed, view=view)
    
        embed = discord.Embed(title="직업뽑기", description="분류를 선택하세요.", color=0xFAE0D4)
        embed.add_field(name="모든 직업  (🎲)" ,value="전체 직업 중 랜덤 추출", inline=False)
        embed.add_field(name="직업  (🕐)" ,value="ex) 전사, 궁수, 도적 등", inline=False)
        embed.add_field(name="종족[소속]  (🕑)" ,value="ex) 모험가, 영웅, 노바 ...", inline=False)

        view = discord.ui.View(timeout=10.0)
        button1 = discord.ui.Button(label="모든 직업", emoji="🎲")
        button2 = discord.ui.Button(label="직업", emoji="🕐")
        button3 = discord.ui.Button(label="종족[소속]", emoji="🕑")
        
        button1.callback = all_jobs
        button2.callback = categorical
        button3.callback = race
        
        view.add_item(button1)
        view.add_item(button2)
        view.add_item(button3)

        await interaction.response.send_message(embed=embed, view=view)
    
    @app_commands.command(name="추옵", description="무기의 추가옵션을 확인합니다.")
    async def choo_op(self, interaction):

        async def papnir(interaction):
            embed = discord.Embed()
            embed.set_image(url='https://postfiles.pstatic.net/MjAyMzAxMDJfMjYg/MDAxNjcyNjQ0MTQzNTQ4.POCKM0PIgFOSe9dyjE-Nm5H9RAnIoiufMjMw_gOKJj0g.ioV1c-scnlP1--EpUyLm8fnDnQ6UDf901ZrQJrPW8sIg.PNG.suryblue/i13353553723.png?type=w966')
            embed.set_footer(text='출처 : https://blog.naver.com/hongs1904/222221149711')
            await interaction.response.send_message(embed=embed)
        
        async def absolas(interaction):
            embed = discord.Embed()
            embed.set_image(url='https://postfiles.pstatic.net/MjAyMzAxMDJfNDkg/MDAxNjcyNjQ0MTQzNDkx.RGh9YDENkFYrmgDL47MpfwWZCe84AjIxpsB_rn0GrvIg.PVatc2BGqddXOeB87i-uV9eL5I3tRg7gdTH7wr6axCEg.PNG.suryblue/i13318233624.png?type=w966')
            embed.set_footer(text='출처 : https://blog.naver.com/hongs1904/222221149711')
            await interaction.response.send_message(embed=embed)
        
        async def arcane(interaction):
            embed = discord.Embed()
            embed.set_image(url='https://postfiles.pstatic.net/MjAyMzAxMDJfMTU1/MDAxNjcyNjQ0MTQzNTU2.yQNMXw5DLVjLojuSc3vD-rfLhpxlHrmSXmla7gKjmAEg.4qZJSB0R4Zcwnu0L4bULmORSc1tUoe9PSZKszO5vpm0g.PNG.suryblue/i13384268658.png?type=w966')
            embed.set_footer(text='출처 : https://blog.naver.com/hongs1904/222221149711')
            await interaction.response.send_message(embed=embed)
        
        async def genesis(interaction):
            embed = discord.Embed()
            embed.set_image(url='https://postfiles.pstatic.net/MjAyMzAxMDJfMjg3/MDAxNjcyNjQ0MTQzNTYw.cmpxf_w1o_F3jkCrrzbw4VMpB-7UbpHjgJB4xbXHXzQg.HYnlpbCgsFDB9T9B8-usoSyRb81HU0rggfRj-D2GFqsg.PNG.suryblue/i13351743797.png?type=w966')
            embed.set_footer(text='출처 : https://blog.naver.com/hongs1904/222221149711')
            await interaction.response.send_message(embed=embed)
        
        embed = discord.Embed(title="추옵", description="", color=0xFAE0D4)
        embed.add_field(name="파프니르  (🕐)" ,value="150제", inline=False)
        embed.add_field(name="앱솔랩스  (🕑)" ,value="160제", inline=False)
        embed.add_field(name="아케인셰이드  (🕒)" ,value="200제", inline=False)
        embed.add_field(name="제네시스  (🕓)" ,value="200제", inline=False)

        view = discord.ui.View()
        button1 = discord.ui.Button(label="파프니르", emoji="🕐")
        button2 = discord.ui.Button(label="앱솔랩스", emoji="🕑")
        button3 = discord.ui.Button(label="아케인셰이드", emoji="🕒")
        button4 = discord.ui.Button(label="제네시스", emoji="🕓")

        button1.callback = papnir
        button2.callback = absolas
        button3.callback = arcane
        button4.callback = genesis

        view.add_item(button1)
        view.add_item(button2)
        view.add_item(button3)
        view.add_item(button4)

        await interaction.response.send_message(embed=embed, view=view)
    

    @app_commands.command(name="심볼", description="심볼 강화 비용을 조회합니다.")
    async def symbol(self, interaction):

        class text_modal(discord.ui.Modal):
            level = discord.ui.TextInput(label="현재 심볼의 레벨을 입력해주세요", placeholder="1")
            self.level = level

            def __init__(self, base:int, coef:int):
                super().__init__(title='아케인심볼 강화', timeout=30.0, custom_id="sym")
                self.base = base
                self.coef = coef

            async def on_submit(self, interaction):
                if not self.level.value.isdigit() or int(self.level.value) > 20 or int(self.level.value) < 1:
                    await interaction.response.send_message("1~20 사이의 숫자를 입력해주세요.")
                    return
                if int(self.level.value) == 20:
                    await interaction.response.send_message("최대 레벨입니다.")
                    return
                meso = self.base + int(self.level.value) * self.coef
                growth = int(self.level.value)**2 + 11
                await interaction.response.send_message("lv.%d -> lv.%d\n필요 성장치 : %d\n강화 비용 : %d 메소" %(int(self.level.value), int(self.level.value) + 1 ,growth,meso))

        async def yeoro(interaction):
            await interaction.response.send_modal(text_modal(3110000, 3960000))
        
        async def chuchu(interaction):
            await interaction.response.send_modal(text_modal(6220000, 4620000))
        
        async def lachelen(interaction):
            await interaction.response.send_modal(text_modal(9330000, 5280000))
        
        async def etc(interaction):
            await interaction.response.send_modal(text_modal(11196000, 5940000))

        embed = discord.Embed(title="심볼", description="", color=0xFAE0D4)
        embed.add_field(name="소멸의 여로  (🕐)" ,value="lv.200", inline=False)
        embed.add_field(name="츄츄 아일랜드 (🕑)" ,value="lv.210", inline=False)
        embed.add_field(name="레헬른  (🕒)" ,value="lv.220", inline=False)
        embed.add_field(name="아르카나~에스페라  (🕓)" ,value="lv.225~235", inline=False)

        view = discord.ui.View()
        button1 = discord.ui.Button(label="소멸의 여로", emoji="🕐")
        button2 = discord.ui.Button(label="츄츄 아일랜드", emoji="🕑")
        button3 = discord.ui.Button(label="레헬른", emoji="🕒")
        button4 = discord.ui.Button(label="아르카나~에스페라", emoji="🕓")

        button1.callback = yeoro
        button2.callback = chuchu
        button3.callback = lachelen
        button4.callback = etc

        view.add_item(button1)
        view.add_item(button2)
        view.add_item(button3)
        view.add_item(button4)
        
        await interaction.response.send_message(embed=embed, view=view)
        
    @app_commands.command(name="프로텍트", description="프로텍트 에스페라 공략을 확인합니다.")
    async def protect_espera(self, interaction: discord.Interaction):
        embed1 = discord.Embed(color=0xa2cd5a)
        embed2 = discord.Embed(color=0xa2cd5a)
        embed1.set_image(url="https://upload3.inven.co.kr/upload/2021/08/24/bbs/i13535684383.png?MW=800")
        embed2.set_image(url="https://upload3.inven.co.kr/upload/2021/08/24/bbs/i14155987428.png?MW=800")
        embed2.set_footer(text="출처 : https://www.inven.co.kr/board/maple/2304/28788")
        embeds = [embed1, embed2]
        await interaction.response.send_message(embeds=embeds)

async def setup(bot):
    maple = Maple(bot)
    await bot.add_cog(maple)
    try:
        bot.tree.add_command(maple.maple)
        bot.tree.add_command(maple.gsb)
    except app_commands.CommandAlreadyRegistered:
        pass