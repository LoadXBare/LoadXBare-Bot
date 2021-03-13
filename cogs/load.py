import discord
from discord.ext import commands


class Load(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def load(self, ctx):
        embed = discord.Embed(color=0x1e507d)
        embed.set_image(url='https://i.imgur.com/bsLgC8a.png')
        await ctx.send(embed=embed)
        if ctx.channel.id == 799220260695441418:
            embed.set_image(url='https://i.imgur.com/0E9SUSm.png')
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Load(client))
