import discord
from discord.ext import commands


class PetTheBot(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def petthebot(self, ctx):
        embed = discord.Embed(color=0x1e507d)
        embed.set_image(url='https://i.imgur.com/sOA7hzb.gif')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(PetTheBot(client))
