import discord
from discord.ext import commands
bot = commands.Bot(command_prefix=".", intents=discord.Intents.all(), help_command=None)
@bot.command()


async def hi(ctx):
    await ctx.send("hi :D")

bot.run("MTA2NjU4NzMxMDk5MDMxNTYzMA.G86h_H.RE566GotH0EzWUC_dLrpDKRKpx07a5hFVjyOjo")