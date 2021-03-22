import discord
from discord.ext import commands

from cogs.cog_settings import embed_color


class Noham(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def noham(self, ctx):
        embed_name = 'Noham'
        embed = discord.Embed(color=embed_color)
        embed.add_field(name=embed_name,
                        value='[PLACEHOLDER]',
                        inline=False)
        await ctx.reply(embed=embed,
                        mention_author=False)
