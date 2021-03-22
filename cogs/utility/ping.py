import discord
from discord.ext import commands
from cogs.cog_settings import embed_color


class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        embed_name = ':stopwatch: Ping :stopwatch:'
        embed = discord.Embed(color=embed_color)
        embed.add_field(name=embed_name,
                        value=f'{round(self.client.latency * 1000)}ms',
                        inline=False)
        await ctx.reply(embed=embed,
                        mention_author=False)
