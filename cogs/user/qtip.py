import discord
from discord.ext import commands

from cogs.cog_settings import embed_color


class Qtip(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def qtip(self, ctx):
        user = await discord.Client.fetch_user(self=self.client, user_id=453976398701395968)
        embed = discord.Embed(title='> [PLACEHOLDER]',
                              color=embed_color)

        embed.set_author(name='qTiP',
                         icon_url=user.avatar_url)
        await ctx.reply(embed=embed,
                        mention_author=False)
