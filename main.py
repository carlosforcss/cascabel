import os, asyncio
import platform
import discord
from discord.ext import commands


# import all of the cogs
from helptopic import HelpTopic
from music_cog import MusicTopic
from utils.logger import get_logger

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="#", intents=intents)

# remove the default help command so that we can write out own
bot.remove_command("help")


async def main():
    logger = get_logger()
    logger.info("Initializing project.")
    async with bot:
        if platform.system() == "Darwin":
            logger.info("Using opus from library.")
            discord.opus.load_opus("/Users/carlosdavidsanchezmoreno/lib/opus/1.5.1/lib/libopus.dylib")
        await bot.add_cog(HelpTopic(bot))
        await bot.add_cog(MusicTopic(bot))
        await bot.start(os.getenv("TOKEN"))


asyncio.run(main())
