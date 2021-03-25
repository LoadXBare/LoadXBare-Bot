import random
import discord
from discord.ext import commands
from cogs.cog_settings import embed_color


class Flip(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def flip(self, ctx):
        embed = discord.Embed(color=embed_color)
        num = random.randint(0, 1)
        responses = ['Heads!', 'Tails!']
        images = ['https://i.imgur.com/V1fnHOn.png', 'https://i.imgur.com/rSBOErA.png']

        embed.add_field(name=':coin: Flip :coin:',
                        value=responses[num],
                        inline=False)
        embed.set_image(url=images[num])
        await ctx.reply(embed=embed,
                        mention_author=False)
