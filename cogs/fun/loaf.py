import discord
from discord.ext import commands
from cogs.cog_settings import embed_color


class Loaf(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def loaf(self, ctx):
        embed = discord.Embed(color=embed_color)

        embed.add_field(name=':bread: LoafXBare :bread:',
                        value='I am not a loaf of bread ;-;\n'
                              'Perhaps you meant to run the command `.load`',
                        inline=False)
        embed.set_image(url='https://i.imgur.com/NAdoFK6.png')
        await ctx.reply(embed=embed,
                        mention_author=False)
