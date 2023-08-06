from discord.ext import commands
import asyncio
import random
import discord
from discord import app_commands
import pymongo
import numpy as np
import os

def sigmoid(x):
    return 1 / (1 + np.exp(-x * 0.1))

def probability(num):
    return sigmoid(30-num)

def destroy(num):
    if num <= 15:
        return 0.00
    elif num <= 50:
        return (1 - probability(num)) * num / 100
    else:
        return (1 - probability(num)) * 0.5

client = pymongo.MongoClient(os.environ.get("DB_str"))
db = client.inchant
db_point = client.point

class Inchant(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="강화", description="멤버를 인챈트합니다.")
    async def inc(self, interaction :discord.Interaction, member: discord.Member):
        ctx = await commands.Context.from_interaction(interaction)
        server_id = interaction.guild_id
        collection = db[str(server_id)]
        entry = collection.find_one({'id': str(member.id)})
        if entry is None:
            collection.insert_one({
                'id': str(member.id),
                'name': member.display_name,
                'level': 0
            })
            entry = collection.find_one({'id': str(member.id)})
        embed = discord.Embed(title="강화", description=f"{member.display_name} 🌟 {entry['level']} -> 🌟 {entry['level'] + 1}", color=0xCC723D)
        if entry['level'] <= 15:
            embed.add_field(name="강화하시겠습니까? (100 Pt 소모)", value=f"성공확률 : {round(probability(entry['level']), 4) * 100} %\n실패(하락)확률 : {round(1-probability(entry['level']),4)*100} %", inline=False)
        else:
            embed.add_field(name="강화하시겠습니까? (100 Pt 소모)", value=f"성공확률 : {round(probability(entry['level']), 4) * 100} %\n실패(하락)확률 : {round(1-probability(entry['level'])-destroy(entry['level']), 4) * 100} %\n실패(파괴)확률 : {round(destroy(entry['level']),4)*100} %", inline=False)
        message = await ctx.send(embed=embed)
        await message.add_reaction('✔')
        await message.add_reaction('❌')
        def check1(reaction, user):
            return user == ctx.author
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=10.0, check=check1)
            if str(reaction.emoji) == "✔":
                entry_p = db_point[str(server_id)].find_one({'id':str(interaction.user.id)})
                if entry_p is None or entry_p['points'] < 100:
                    await ctx.send(f"포인트가 부족합니다.")
                    return
                db_point[str(server_id)].update_one({'id':str(interaction.user.id)}, {'$inc': {'points': -100}})
                weight = probability(entry['level'])
                inchant_list = ["성공", "실패"]
                choice = random.choices(inchant_list, cum_weights=(weight,1.00), k=1)
                if choice[0] == "성공":
                    embed = discord.Embed(title="강화결과", description="", color=0xCC723D)
                    embed.add_field(name="강화성공", value=f"🌟{entry['level']} -> 🌟{entry['level'] + 1}", inline=False)
                    await ctx.send(embed=embed)
                    collection.update_one({'id':str(member.id)}, {'$inc': {'level' : 1}})
                    return None
                else:
                    weight = destroy(entry['level'])
                    inchant_list = ["파괴", "유지"]
                    choice = random.choices(inchant_list, cum_weights=(weight,1.00), k=1)
                    if choice[0] == "파괴":
                        embed = discord.Embed(title="강화결과", description="", color=0xCC723D)
                        embed.add_field(name="파괴됨", value=f"🌟{entry['level']} -> 🌟0", inline=False)
                        await ctx.send(embed=embed)
                        collection.update_one({'id' : str(member.id)}, {'$set' : {'level' : 0}})
                        return None
                    else:
                        embed = discord.Embed(title="강화결과", description="", color=0xCC723D)
                        embed.add_field(name="단계 하락", value=f"🌟{entry['level']} -> 🌟{entry['level']-1}", inline=False)
                        await ctx.send(embed=embed)
                        collection.update_one({'id' : str(member.id)}, {'$inc': {'level' : -1}})
                        return None
            else:
                return None
        except asyncio.TimeoutError:
            await ctx.send("시간이 초과되었습니다. 다시 시도하세요.")
            
    @app_commands.command(name="강화확률", description="해당 단계에서의 강화확률을 조회합니다.")
    async def prob(self, interaction: discord.Interaction, level: int):
        embed = discord.Embed(title="강화확률", description="", color=0xCC723D)
        if level <= 15:
            embed.add_field(name=str('🌟' + str(level)) + " -> " + '🌟' + str(level+1), value="성공확률 : " + str(round(probability(level), 4) * 100) + " %\n실패(하락)확률 : " + str(round(1-probability(level),4)*100) + " %", inline=False)
        else:
            embed.add_field(name=str('🌟' + str(level)) + " -> " + '🌟' + str(level+1), value="성공확률 : " + str(round(probability(level), 4) * 100) + " %\n실패(하락)확률 : " + str(round(1-probability(level)-destroy(level),4)*100) + " %\n실패(파괴)확률 : " + str(round(destroy(level),4)*100) + " %", inline=False)
        await interaction.response.send_message(embed=embed)
    
    @app_commands.command(name="강화현황", description="현재 내 레벨을 조회합니다.")
    async def now(self, interaction: discord.Interaction):
        server_id = interaction.guild_id
        collection = db[str(server_id)]
        entry = collection.find_one({'id': str(interaction.user.id)})
        embed = discord.Embed(title="강화단계 조회", description="", color=0xCC723D)
        if entry is None:
            embed.add_field(name=f"{interaction.user.display_name}", value="아직 강화를 하지 않으셨네요! /강화 로 인챈트에 도전해보세요!", inline=False)
        else:
            embed.add_field(name=f"{interaction.user.display_name}", value=f"🌟{entry['level']}", inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        

    @app_commands.command(name="강화랭킹", description="강화랭킹을 조회합니다.")
    async def rank(self, interaction: discord.Interaction):
        server_id = interaction.guild_id
        collection = db[str(server_id)]
        cursor = collection.find({}).sort('level', pymongo.DESCENDING)
        len_check = list(cursor)
        embed = discord.Embed(title="강화 랭킹", description="", color=0xCC723D)
        if len(len_check) == 0:
            embed.add_field(name="랭킹이 존재하지 않습니다.", value="아직 아무도 강화를 시도하지 않았어요!")
        else:
            for doc in len_check:
                embed.add_field(name=f"{doc['name']}", value=f"🌟{doc['level']}", inline=False)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    inchant = Inchant(bot)
    await bot.add_cog(inchant)
    try:
        bot.tree.add_command(inchant.inc)
        bot.tree.add_command(inchant.prob)
        bot.tree.add_command(inchant.now)
        bot.tree.add_command(inchant.rank)
    except app_commands.CommandAlreadyRegistered:
        pass