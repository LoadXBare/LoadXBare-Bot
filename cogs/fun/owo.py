import discord
from discord.ext import commands
from cogs.cog_settings import embed_color


class Owo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def owo(self, ctx):
        embed = discord.Embed(color=embed_color)
        embed.set_image(url='https://i.imgur.com/M9oRGbT.png')
        await ctx.reply(embed=embed,
                        mention_author=False)
