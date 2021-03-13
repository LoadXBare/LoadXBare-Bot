import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title='__Commands List__',
                              color=0x1e507d)
        embed.add_field(name=':tools: Utility :tools:',
                        value='`.code`, `.help`, `.ping`',
                        inline=False)
        embed.add_field(name=':tada: Fun :tada:',
                        value='`.8ball`, `.bunger`, `.load`, '
                              '`.loaf`, `.owo`, `.petthebot`, '
                              '`.petthebunger`, `.rate`, `.uwu`',
                        inline=False)
        embed.set_footer(text='LoadXBare Bot v2.0.1')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))
