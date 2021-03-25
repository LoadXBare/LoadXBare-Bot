import discord
from discord.ext import commands
from cogs.cog_settings import embed_color


class Load(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def load(self, ctx):
        user = await discord.Client.fetch_user(self=self.client, user_id=455321156224942091)
        embed = discord.Embed(title='> UwU',
                              color=embed_color)

        embed.set_author(name='Load',
                         icon_url=user.avatar_url)
        embed.set_image(url='https://i.imgur.com/bsLgC8a.png')
        await ctx.reply(embed=embed,
                        mention_author=False)
        if ctx.channel.id == 799220260695441418:
            embed.set_image(url='https://i.imgur.com/nfOAOBg.png')
            await ctx.send(embed=embed)
