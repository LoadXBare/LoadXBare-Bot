import discord
from discord.ext import commands


class Code(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def code(self, ctx):
        embed = discord.Embed(color=0x1e507d)
        embed.add_field(name='Code',
                        value='My code is publicly available to view on GitHub [here](https://github.com/LoadXBare/LoadXBare-Bot)!',
                        inline=False)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Code(client))
