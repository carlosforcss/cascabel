import os, asyncio
import platform
import discord
from discord.ext import commands
from src.utils.logger import get_logger
from src.topics.music import MusicTopic
from src.topics.help import HelpTopic


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="#", intents=intents)
bot.remove_command("help")


async def initialize_bot():
    logger = get_logger()
    logger.info("Initializing project.")
    async with bot:
        if platform.system() == "Darwin":
            logger.info("Using opus from library.")
            discord.opus.load_opus("/Users/carlosdavidsanchezmoreno/lib/opus/1.5.1/lib/libopus.dylib")
        await bot.add_cog(HelpTopic(bot))
        await bot.add_cog(MusicTopic(bot))
        await bot.start(os.getenv("TOKEN"))
