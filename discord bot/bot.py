from discord.ext import commands
import discord
import asyncio

token = "Your token here"

class PuilinBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='/',
            intents=discord.Intents.all(),
            sync_command=True,
            application_id=710842722046574603
        )
        self.initial_extension = [
            "cogs.maincog",
            "cogs.randomgame",
            "cogs.crawling",
            "cogs.maple",
            "cogs.br31",
            "cogs.inchant",
            "cogs.setting",
            "cogs.conversation"
        ]
    
    async def setup_hook(self):
        for ext in self.initial_extension:
            await self.load_extension(ext)
        await bot.tree.sync()

    async def on_ready(self):
        print("등장 : ")
        print(self.user.name)
        print(self.user.id)
        print("----------")
        print(len(bot.guilds), "개 서버에서 동작 중")
        print("==========")
        game = discord.Game("퓨이린 봇 개발모드")
        await self.change_presence(status=discord.Status.online, activity=game)

# Windows의 경우 event loop 정책 설정 변경
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
bot = PuilinBot()
bot.run(token)