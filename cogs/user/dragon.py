import discord
from discord.ext import commands

from cogs.cog_settings import embed_color


class Dragon(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dragon(self, ctx):
        user = await discord.Client.fetch_user(self=self.client, user_id=391660977449467904)
        embed = discord.Embed(title='> Oh you poor Miserable Soul, '
                                    'What lead you the misfortune of wanting to use a command about me? '
                                    'Go hydrate yourself with some Dihydrogen Monoxide. Bye Bye Now.',
                              color=embed_color)

        embed.set_author(name='Dragon',
                         icon_url=user.avatar_url)
        await ctx.reply(embed=embed,
                        mention_author=False)
