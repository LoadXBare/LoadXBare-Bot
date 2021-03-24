import random
import discord
from discord.ext import commands
from cogs.cog_settings import embed_color


class Tofu(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def tofu(self, ctx):
        user = await discord.Client.fetch_user(self=self.client, user_id=221493681075650560)
        images = ['https://i.imgur.com/NyqAPsq.png', 'https://i.imgur.com/vGWSZkz.png',
                  'https://i.imgur.com/ZDwTrBr.png', 'https://i.imgur.com/Pk7P4yv.png',
                  'https://i.imgur.com/UZOGoAg.png', 'https://i.imgur.com/LBdWpIs.png',
                  'https://i.imgur.com/QOowvnp.png', 'https://i.imgur.com/kPptcmv.gif']
        embed = discord.Embed(title='> I would like to have a word with you.',
                              color=embed_color)

        embed.set_author(name='Tofu',
                         icon_url=user.avatar_url)
        embed.set_image(url=random.choice(images))
        await ctx.reply(embed=embed,
                        mention_author=True)
