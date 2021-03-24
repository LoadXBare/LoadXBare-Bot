import discord
from discord.ext import commands

from cogs.cog_settings import embed_color


class Noham(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def noham(self, ctx):
        user = await discord.Client.fetch_user(self=self.client, user_id=528846496620085248)
        embed = discord.Embed(title='> [PLACEHOLDER]',
                              color=embed_color)

        embed.set_author(name='Noham',
                         icon_url=user.avatar_url)
        await ctx.reply(embed=embed,
                        mention_author=False)
