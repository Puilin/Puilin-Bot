from discord.ext import commands
import discord

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

token = ""

bot.load_extension("cogs.maincog")
bot.load_extension("cogs.randomgame")
bot.load_extension("cogs.crawling")
bot.load_extension("cogs.maple")
bot.load_extension("cogs.br31")
bot.load_extension("cogs.inchant")
bot.load_extension("cogs.music")
bot.load_extension("cogs.setting")
bot.load_extension("cogs.conversation")

@bot.event
async def on_ready():
    print("등장 : ")
    print(bot.user.name)
    print(bot.user.id)
    print("----------")
    print(len(bot.guilds), "개 서버에서 동작 중")
    print("==========")
    game = discord.Game("퓨이린 봇 개발모드")
    await bot.change_presence(status=discord.Status.online, activity=game)

bot.run(token)