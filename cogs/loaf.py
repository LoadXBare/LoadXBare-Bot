import discord
from discord.ext import commands


class Loaf(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def loaf(self, ctx):
        embed_name = ':bread: LoafXBare :bread:'
        embed = discord.Embed(color=0x1e507d)
        embed.add_field(name=embed_name,
                        value='I am not a loaf of bread ;-;\n'
                              'Perhaps you meant to run the command `.load`',
                        inline=False)
        embed.set_image(url='https://i.imgur.com/NAdoFK6.png')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Loaf(client))
