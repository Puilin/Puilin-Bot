import asyncio
import discord
from discord.ext import commands
from discord import app_commands
import os
import pymongo
import random

client = pymongo.MongoClient("your string here")
db = client.point

class Gambling(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="도박", description="포인트를 걸고 도박을 시작합니다.")
    async def gamble(self, interaction: discord.Interaction, point: int):
        if point < 100:
            await interaction.response.send_message("최소 100 Pt 이상 도박에 걸어야합니다.")
            return
        server_id = str(interaction.user.guild.id)
        user_id = str(interaction.user.id)
        entry = db[server_id].find_one({'id': user_id})
        if entry is None or entry['points'] < point:
            await interaction.response.send_message("포인트가 부족합니다")
            return

        ctx = await commands.Context.from_interaction(interaction)


        async def dice_callback(interaction):
            async def dice_s_callback(interaction):
                dice = random.randint(1, 6)
                await ctx.send(f"주사위 결과 : {dice}\n예측한 결과 : {select.values[0]}")
                if dice == int(select.values[0]):
                    db[server_id].update_one({'id':str(interaction.user.id)}, {'$inc':{'points':point * 3}})
                    await interaction.response.send_message(f"{point * 3} Pt를 획득하였습니다.")
                else:
                    await interaction.response.send_message("포인트를 획득하지 못하였습니다. 다시 도전해보세요.")
            
            db[server_id].update_one({'id': user_id}, {'$inc':{'points': -point}})
            view = discord.ui.View(timeout=15.0)
            opts = []
            for i in range(1, 7):
                opts.append(discord.SelectOption(label=str(i)))
            select = discord.ui.Select(options=opts)
            select.callback = dice_s_callback
            view.add_item(select)
            await interaction.response.send_message("주사위는 몇이 나올까요? (시간제한 15초)", view=view)
        
        async def cancle_callback(interaction):
            interaction.respone.send_message("도박이 취소되었습니다.")

        view = discord.ui.View(timeout=10.0)
        button1 = discord.ui.Button(label="주사위 굴리기", emoji="🎲")
        button2 = discord.ui.Button(label="취소", emoji="❌")
        button1.callback = dice_callback
        button2.callback = cancle_callback
        view.add_item(button1)
        view.add_item(button2)
        embed = discord.Embed(title=f"도박 (베팅 : {point} Pt)", description="이용하고자 하는 서비스를 선택해주세요", color=0xAE221F)
        embed.add_field(name="🎲 주사위 굴리기", value="X3 배율", inline=False)
        embed.add_field(name="❌ 도박 취소", value="지나친 도박은 몸에 해롭습니다.", inline=False)
        await ctx.send(embed=embed, view=view)

    
async def setup(bot):
    gambling = Gambling(bot)
    await bot.add_cog(gambling)