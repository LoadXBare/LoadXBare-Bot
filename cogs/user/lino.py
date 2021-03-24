import discord
from discord.ext import commands
from cogs.cog_settings import embed_color


class Lino(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def lino(self, ctx):
        user = await discord.Client.fetch_user(self=self.client, user_id=332142876207349764)
        embed = discord.Embed(title='> sup mortal',
                              color=embed_color)

        embed.set_author(name='Lino',
                         icon_url=user.avatar_url)
        embed.set_image(url='https://i.imgur.com/moXGRdf.png')
        await ctx.reply(embed=embed,
                        mention_author=False)
