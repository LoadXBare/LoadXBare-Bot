import discord
from discord.ext import commands
from cogs.cog_settings import embed_color


class Lino(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def lino(self, ctx):
        embed_name = 'Lino'
        embed = discord.Embed(color=embed_color)
        embed.add_field(name=embed_name,
                        value='sup mortal',
                        inline=False)
        embed.set_image(url='https://i.imgur.com/moXGRdf.png')
        await ctx.reply(embed=embed,
                        mention_author=False)
