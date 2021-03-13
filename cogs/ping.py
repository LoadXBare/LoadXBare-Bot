import discord
from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        embed_name = ':stopwatch: Ping :stopwatch:'
        embed = discord.Embed(color=0x1e507d)
        embed.add_field(name=embed_name,
                        value=f'{round(self.client.latency * 1000)}ms',
                        inline=False)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Ping(client))
