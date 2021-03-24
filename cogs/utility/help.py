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
        user = self.client.user

        embed.add_field(name=':tools: Utility :tools:',
                        value='`.code`, `.help`, `.ping`',
                        inline=False)
        embed.add_field(name=':tada: Fun :tada:',
                        value='`.8ball`, `.bunger`, `.loaf`, `.owo`, `.petthebot`, `.petthebunger`, `.rate`, `.uwu`',
                        inline=False)
        embed.add_field(name=':person_standing: User :person_standing:',
                        value='`.dragon`, `.eli`, `.lino`, `.load`, `.noham`, `.pengu`, `.qtip`, `.tofu`',
                        inline=False)
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.reply(embed=embed,
                        mention_author=False)
