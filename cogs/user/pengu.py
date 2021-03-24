import discord
from discord.ext import commands

from cogs.cog_settings import embed_color


class Pengu(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pengu(self, ctx):
        user = await discord.Client.fetch_user(self=self.client, user_id=322063964219637771)
        embed = discord.Embed(title='> AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
                              color=embed_color)

        embed.set_author(name='Pengu',
                         icon_url=user.avatar_url)
        embed.set_image(url='https://i.imgur.com/XbOlLJl.gif')
        await ctx.reply(embed=embed,
                        mention_author=False)
