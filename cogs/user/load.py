import discord
from discord.ext import commands
from cogs.cog_settings import embed_color


class Load(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def load(self, ctx):
        embed = discord.Embed(color=embed_color)
        embed.set_image(url='https://i.imgur.com/bsLgC8a.png')
        await ctx.reply(embed=embed,
                        mention_author=False)
        if ctx.channel.id == 799220260695441418:
            embed.set_image(url='https://i.imgur.com/0E9SUSm.png')
            await ctx.send(embed=embed)
