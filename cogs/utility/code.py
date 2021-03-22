import discord
from discord.ext import commands
from cogs.cog_settings import embed_color


class Code(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def code(self, ctx):
        embed_name = '<:code:820378072427528213> Code <:code:820378072427528213>'
        embed = discord.Embed(color=embed_color)
        embed.add_field(name=embed_name,
                        value='My code is publicly available to view on '
                              'GitHub [here](https://github.com/LoadXBare/LoadXBare-Bot)!',
                        inline=False)
        await ctx.reply(embed=embed,
                        mention_author=False)
