from discord.ext import commands
import asyncio
import random
import discord

def probability(num):
    if num <= 325:
        return 1 - (num * 0.003)**0.9
    else:
        return 0.01

def destroy(num):
    if num <= 50:
        return 0.00
    else:
        return (1 - probability(num)) / 800 * num # 801부터 음수 됨


class Inchant(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="강화", pass_context=True)
    async def inc(self, ctx, *who):
        try:
            server_id = ctx.guild.id
            f = open(str(server_id) + ".txt", 'r')
            str_list = f.readlines()
            find = False
            for i in str_list:
                lst1 = i.strip('\n').split("-")
                if lst1[0] == str(' '.join(who)):
                    find = True
                    idx = str_list.index(i)
                    lv = int(lst1[1])
                    embed = discord.Embed(title="강화", description=lst1[0] + ' 🌟' + str(lv) + " -> " + '🌟' + str(lv+1), color=0xCC723D)
                    if lv <= 50:
                        embed.add_field(name="강화하시겠습니까?", value="성공확률 : " + str(round(probability(int(lv)), 2) * 100) + " %\n실패(하락)확률 : " + str(round(1-probability(int(lv)),2)*100) + " %", inline=False)
                    else:
                        embed.add_field(name="강화하시겠습니까?", value="성공확률 : " + str(round(probability(int(lv)), 2) * 100) + " %\n실패(하락)확률 : " + str(round(1-probability(int(lv))-destroy(int(lv)),2)*100) + " %\n실패(파괴)확률 : " + str(round(destroy(int(lv)),2)*100) + " %", inline=False)
                    message = await ctx.send(embed=embed)
                    await message.add_reaction('✔')
                    await message.add_reaction('❌')
                    def check1(reaction, user):
                        return user == ctx.author
                    try:
                        reaction, user = await self.bot.wait_for('reaction_add', timeout=10.0, check=check1)
                        if str(reaction.emoji) == "✔":
                            weight = probability(lv)
                            inchant_list = ["성공", "실패"]
                            choice = random.choices(inchant_list, cum_weights=(weight,1.00), k=1)
                            if choice[0] == "성공":
                                embed = discord.Embed(title="강화결과", description="", color=0xCC723D)
                                embed.add_field(name="강화성공", value='🌟' + str(lv) + " -> " + '🌟' + str(lv+1),inline=False)
                                await ctx.send(embed=embed)
                                f.close()
                                f2 = open(str(server_id) + ".txt", 'w')
                                str_list[idx] = lst1[0] + "-" + str(lv+1) + "\n"
                                for i in str_list:
                                    f2.write(i)
                                f2.close()
                                return None
                            else:
                                weight = destroy(lv)
                                inchant_list = ["파괴", "유지"]
                                choice = random.choices(inchant_list, cum_weights=(weight,1.00), k=1)
                                if choice[0] == "파괴":
                                    embed = discord.Embed(title="강화결과", description="", color=0xCC723D)
                                    embed.add_field(name="파괴됨", value='🌟' + str(lv) + " -> " + '🌟' + str(0),inline=False)
                                    await ctx.send(embed=embed)
                                    f.close()
                                    f3 = open(str(server_id) + ".txt", 'w')
                                    str_list[idx] = lst1[0] + "-" + str(0) + "\n"
                                    for i in str_list:
                                        f3.write(i)
                                    f3.close()
                                    return None
                                else:
                                    embed = discord.Embed(title="강화결과", description="", color=0xCC723D)
                                    embed.add_field(name="단계 하락", value='🌟' + str(lv) + " -> " + '🌟' + str(lv-1),inline=False)
                                    await ctx.send(embed=embed)
                                    f.close()
                                    f4 = open(str(server_id) + ".txt", 'w')
                                    str_list[idx] = lst1[0] + "-" + str(lv-1) + "\n"
                                    for i in str_list:
                                        f4.write(i)
                                    f4.close()
                                    return None
                        else:
                            f.close()
                    except asyncio.TimeoutError:
                        f.close()
            if not find:
                await ctx.send("존재하지 않는 멤버입니다.")
            f.close()
        except FileNotFoundError:
            f = open(str(server_id) + ".txt", 'w')
            member_list = []
            for i in ctx.guild.members:
                member_list.append(i.name)
            for i in member_list:
                if i == str(' '.join(who)):
                    weight = probability(0)
                    inchant_list = ["성공", "실패"]
                    choice = random.choices(inchant_list, cum_weights=(weight,1.00), k=1)
                    if choice[0] == "성공":
                        embed = discord.Embed(title="강화결과", description="", color=0xCC723D)
                        embed.add_field(name="강화성공", value='🌟' + str(0) + " -> " + '🌟' + str(1),inline=False)
                        await ctx.send(embed=embed)
                        f.write(i + "-" + "1\n")
                else:
                    f.write(i + "-" + "0\n")
            f.close()
    
    @commands.command(name="강화확률", pass_context=True)
    async def prob(self, ctx, lv):
        embed = discord.Embed(title="강화확률", description="", color=0xCC723D)
        if int(lv) <= 50:
            embed.add_field(name=str('🌟' + str(int(lv))) + " -> " + '🌟' + str(int(lv)+1), value="성공확률 : " + str(round(probability(int(lv)), 2) * 100) + " %\n실패(하락)확률 : " + str(round(1-probability(int(lv)),2)*100) + " %", inline=False)
        else:
            embed.add_field(name=str('🌟' + str(int(lv))) + " -> " + '🌟' + str(int(lv)+1), value="성공확률 : " + str(round(probability(int(lv)), 2) * 100) + " %\n실패(하락)확률 : " + str(round(1-probability(int(lv))-destroy(int(lv)),2)*100) + " %\n실패(파괴)확률 : " + str(round(destroy(int(lv)),2)*100) + " %", inline=False)
        await ctx.send(embed=embed)
    
    @commands.command(name="강화현황", pass_context=True)
    async def now(self, ctx, *who):
        try:
            found = False
            f = open(str(ctx.guild.id) + ".txt", "r")
            my_list = f.readlines()
            f.close()
            for i in my_list:
                my_list2 = i.strip("\n").split("-")
                if my_list2[0] == ' '.join(who):
                    found = True
                    embed = discord.Embed(title=my_list2[0], description="🌟 " + my_list2[1], color=0xCC723D)
                    await ctx.send(embed=embed)
            if not found:
                await ctx.send("존재하지 않는 멤버입니다.")
        except FileNotFoundError:
            f = open(str(ctx.guild.id) + ".txt", 'w')
            member_list = []
            for i in ctx.guild.members:
                member_list.append(i.name)
            for i in member_list:
                f.write(i + "-" + "0\n")
            f.close()
            found = False
            f = open(str(ctx.guild.id) + ".txt", "r")
            my_list = f.readlines()
            f.close()
            for i in my_list:
                my_list2 = i.strip("\n").split("-")
                if my_list2[0] == ' '.join(who):
                    found = True
                    embed = discord.Embed(title=my_list2[0], description="🌟 " + my_list2[1], color=0xCC723D)
                    await ctx.send(embed=embed)
            if not found:
                await ctx.send("존재하지 않는 멤버입니다.")
        

    @commands.command(name="강화랭킹", pass_context=True)
    async def rank(self, ctx):
        guild_id = ctx.guild.id
        try:
            f = open(str(guild_id) + ".txt", "r")
            my_list = f.readlines()
            arr = []
            for i in my_list:
                lst = i.strip("\n").split("-")
                arr.append((lst[0], lst[1]))
            arr = sorted(arr, key=lambda x:int(x[1]), reverse=True)
            embed = discord.Embed(title="강화 랭킹", description="", color=0xCC723D)
            for i in arr:
                embed.add_field(name=i[0], value="🌟 " + i[1], inline=False)
            await ctx.send(embed=embed)
        except FileNotFoundError:
            f = open(str(guild_id) + ".txt", 'w')
            member_list = []
            for i in ctx.guild.members:
                member_list.append(i.name)
            for i in member_list:
                f.write(i + "-" + "0\n")
            f.close()
            f = open(str(guild_id) + ".txt", "r")
            my_list = f.readlines()
            arr = []
            for i in my_list:
                lst = i.strip("\n").split("-")
                arr.append((lst[0], lst[1]))
            arr = sorted(arr, key=lambda x:int(x[1]), reverse=True)
            embed = discord.Embed(title="강화 랭킹", description="", color=0xCC723D)
            for i in arr:
                embed.add_field(name=i[0], value="🌟 " + i[1], inline=False)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Inchant(bot))