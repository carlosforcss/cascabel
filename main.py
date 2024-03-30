import discord
from discord.ext import commands
import os, asyncio

# import all of the cogs
from helptopic import HelpTopic
from music_cog import MusicTopic

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="#", intents=intents)

# remove the default help command so that we can write out own
bot.remove_command("help")


async def main():
    async with bot:
        discord.opus.load_opus("/Users/carlosdavidsanchezmoreno/lib/opus/1.5.1/lib/libopus.dylib")
        await bot.add_cog(HelpTopic(bot))
        await bot.add_cog(MusicTopic(bot))
        await bot.start(os.getenv("TOKEN"))


asyncio.run(main())
