import discord
from discord.ext import commands

from cogs.cog_settings import embed_color


class Eli(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def eli(self, ctx):
        user = await discord.Client.fetch_user(self=self.client, user_id=448232336472014858)
        embed = discord.Embed(title='> [PLACEHOLDER]',
                              color=embed_color)

        embed.set_author(name='Eli',
                         icon_url=user.avatar_url)
        await ctx.reply(embed=embed,
                        mention_author=False)
