import os
import discord
from discord.ext import commands


class Code(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def code(self, ctx):
        embed_name = '<:code:820378072427528213> Code <:code:820378072427528213>'
        embed = discord.Embed(color=ctx.author.color)

        embed.add_field(name=embed_name,
                        value='My code is publicly available to view on '
                              'GitHub [here](https://github.com/LoadXBare/LoadXBare-Bot)!',
                        inline=False)
        embed.set_thumbnail(url=os.getenv('CODE_IMAGE'))
        await ctx.reply(embed=embed,
                        mention_author=False)


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title='__Commands List__',
                              color=ctx.author.color)

        embed.add_field(name=':tada: Fun :tada:',
                        value='`.bunger`, `.8ball`, `.flip`, '
                              '`.loaf`, `.owo`, `.petthebot`, '
                              '`.petthebunger`, `.rate`, `.uwu`',
                        inline=False)
        embed.add_field(name=':person_standing: User :person_standing:',
                        value='`.dragon`, `.eli`, `.lino`, '
                              '`.load`, `.noham`, `.pengu`, '
                              '`.qtip`, `.tofu`',
                        inline=False)
        embed.add_field(name=':tools: Utility :tools:',
                        value='`.code`, `.help`, `.ping`',
                        inline=False)
        embed.set_thumbnail(url=self.client.user.avatar_url)
        await ctx.reply(embed=embed,
                        mention_author=False)


class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        embed_name = ':stopwatch: Ping :stopwatch:'

        embed = discord.Embed(color=ctx.author.color)
        embed.add_field(name=embed_name,
                        value=f'{round(self.client.latency * 1000)}ms',
                        inline=False)
        await ctx.reply(embed=embed,
                        mention_author=False)
