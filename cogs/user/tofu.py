import random
import discord
from discord.ext import commands
from cogs.cog_settings import embed_color


class Tofu(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def tofu(self, ctx):
        embed_name = 'Tofu'
        images = ['https://i.imgur.com/NyqAPsq.png', 'https://i.imgur.com/vGWSZkz.png',
                  'https://i.imgur.com/ZDwTrBr.png', 'https://i.imgur.com/v7oB4jR.png',
                  'https://i.imgur.com/Pk7P4yv.png', 'https://i.imgur.com/UZOGoAg.png',
                  'https://i.imgur.com/1vjzZ4y.png', 'https://i.imgur.com/LBdWpIs.png']
        embed = discord.Embed(color=embed_color)
        embed.add_field(name=embed_name,
                        value=f'<@{ctx.message.author.id}> I would like to have a word with you.',
                        inline=False)
        embed.set_image(url=random.choice(images))
        await ctx.reply(embed=embed,
                        mention_author=False)
