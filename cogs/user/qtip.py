import random

import discord
from discord.ext import commands

from cogs.cog_settings import embed_color


class Qtip(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def qtip(self, ctx):
        user = await discord.Client.fetch_user(self=self.client, user_id=453976398701395968)
        num = random.randint(0, 1)
        images = ['https://i.imgur.com/GzYSgow.png', 'https://i.imgur.com/pXX5NKX.png']
        responses = ['I have never fapped', 'aha']
        embed = discord.Embed(title=f'> {responses[num]}',
                              color=embed_color)

        embed.set_image(url=images[num])
        embed.set_author(name='qTiP',
                         icon_url=user.avatar_url)
        await ctx.reply(embed=embed,
                        mention_author=False)
