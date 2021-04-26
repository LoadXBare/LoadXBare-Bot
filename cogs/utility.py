import datetime
import os
import discord
from discord.ext import commands
from cogs.listeners import Listeners


class Utility(commands.Cog):
    def __init__(self, client): self.client = client

    @commands.command()
    async def code(self, ctx):
        embed_name = 'Code <:code:820378072427528213>'
        embed = discord.Embed(color=ctx.author.color)

        embed.add_field(name=embed_name,
                        value='My code is publicly available to view on '
                              'GitHub [here](https://github.com/LoadXBare/LoadXBare-Bot)!', inline=False)
        embed.set_thumbnail(url=os.getenv('CODE_IMAGE'))
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title='__Commands List__', color=ctx.author.color)
        fun_commands_list, user_commands_list, utility_commands_list = [], [], []
        fun_commands, user_commands, utility_commands = '', '', ''

        for x in self.client.walk_commands():
            if x.cog_name == 'User': user_commands_list.append(str(x))
            elif x.cog_name == 'Fun': fun_commands_list.append(str(x))
            elif x.cog_name == 'Utility': utility_commands_list.append(str(x))

        for x in fun_commands_list: fun_commands += f'`{x}`, '
        for x in user_commands_list: user_commands += f'`{x}`, '
        for x in utility_commands_list: utility_commands += f'`{x}`, '

        embed.add_field(name='Fun :tada:', value=fun_commands.rstrip(', '), inline=False)
        embed.add_field(name='User :person_standing:', value=user_commands.rstrip(', '), inline=False)
        embed.add_field(name='Utility :tools:', value=utility_commands.rstrip(', '), inline=False)
        embed.set_thumbnail(url=self.client.user.avatar_url)
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def ping(self, ctx):
        embed_name = 'Ping :stopwatch:'
        embed = discord.Embed(color=ctx.author.color)

        embed.add_field(name=embed_name, value=f'{round(self.client.latency * 1000)}ms', inline=False)
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def uptime(self, ctx):
        embed_name = 'Uptime :calendar:'
        delta_uptime = datetime.datetime.utcnow() - Listeners.start_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        embed = discord.Embed(color=ctx.author.color)

        embed.add_field(name=embed_name,
                        value=f'{days} days, {hours} hours, {minutes} minutes, {seconds} seconds', inline=False)
        await ctx.reply(embed=embed, mention_author=False)
