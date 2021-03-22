import discord
from discord.ext import commands
from cogs.cog_settings import embed_color


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title='__Commands List__',
                              color=embed_color)
        embed.add_field(name=':tools: Utility :tools:',
                        value='`.code`, `.help`, `.ping`',
                        inline=False)
        embed.add_field(name=':tada: Fun :tada:',
                        value='`.8ball`, `.bunger`, `.loaf`, `.owo`, `.petthebot`, `.petthebunger`, `.rate`, `.uwu`',
                        inline=False)
        embed.add_field(name=':person_standing: User :person_standing:',
                        value='`.lino`, `.load`, `.pengu`, `.tofu`',
                        inline=False)
        embed.set_footer(text='LoadXBare Bot | Owner: LoadXBare#7156',
                         icon_url='https://i.imgur.com/RDuA1YW.png')
        await ctx.reply(embed=embed,
                        mention_author=False)
