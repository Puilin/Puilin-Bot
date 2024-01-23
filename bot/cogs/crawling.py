import discord
from discord.ext import commands
from discord.ext import tasks
from discord import app_commands
from urllib.request import urlopen, Request, URLError, HTTPError
import urllib
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import quote
import warnings
import re
import os
import asyncio
import requests
import random
import pymongo

client = pymongo.MongoClient(os.environ.get("DB_str"))
db_patch = client.patch
collection = db_patch.temp

class Crawling(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="이미지", description="봇이 입력한 검색어로 랜덤한 이미지를 가져옵니다.")
    async def image(self, interaction: discord.Interaction, search: str):
        enc_txt = urllib.parse.quote(search)
        url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query=" + enc_txt
        hdr = {'User-Agent':'Mozilla/5.0'}
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        soup = BeautifulSoup(html,'html.parser')
        images = soup.find_all("img")
        try:
            rand_num = random.randrange(1, len(images))
            image = images[rand_num]['src'][:-12]
            embed = discord.Embed(colour=0xFAE0D4)
            embed.set_image(url=image)
            await interaction.response.send_message(embed=embed)
        except ValueError:
            await interaction.response.send_message("해당 검색어에 대한 이미지를 찾을 수 없습니다.")

    @tasks.loop(minutes=10)
    async def check_fetch(self):
        guilds = self.bot.guilds
        url = "https://maplestory.nexon.com/News/Update"
        with requests.Session() as s:
            res = s.get(url)
            if res.status_code == requests.codes.ok:
                soup = BeautifulSoup(res.text, "html.parser")
                board = soup.find("div", attrs={"class": "update_board"})
                articles = board.find_all("a")
                article = articles[0] # 최신 업데이트
                patch_name = article.contents[1].contents[0]
                entry = collection.find_one({"name": patch_name})
                if entry is None: # 새로운 패치 발견
                    embed = discord.Embed(title="새로운 패치가 감지되었습니다.", description="", color=0xeee8aa)
                    embed.add_field(name=patch_name, value="https://maplestory.nexon.com"+article["href"])
                    collection.drop()
                    collection.insert_one({"name": patch_name})
                    for guild in guilds:
                        await guild.system_channel.send(embed=embed)
                
    

async def setup(bot):
    crawling = Crawling(bot)
    await bot.add_cog(crawling)
    crawling.check_fetch.start()