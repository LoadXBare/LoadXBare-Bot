import random

import discord
from discord.ext import commands

from cogs.cog_settings import embed_color


class Eli(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def eli(self, ctx):
        user = await discord.Client.fetch_user(self=self.client, user_id=448232336472014858)
        num = random.randint(0, 1)
        images = ['https://i.imgur.com/kxD9RoJ.png', 'https://i.imgur.com/ro2T3RH.png']
        responses = ['FiREA MALM', 'when you call eli short']
        embed = discord.Embed(title=f'> {responses[num]}',
                              color=embed_color)

        embed.set_author(name='Eli',
                         icon_url=user.avatar_url)
        embed.set_image(url=images[num])
        await ctx.reply(embed=embed,
                        mention_author=False)
