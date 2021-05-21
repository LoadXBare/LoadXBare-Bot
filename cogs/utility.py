from cogs.constants import start_time
from discord.ext import commands
import datetime
import discord


class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='sourcecode',
                      aliases=['code', 'source'])
    async def sourcecode(self, ctx):
        embed = discord.Embed(color=ctx.author.color)

        embed.add_field(name='Source code <:code:820378072427528213>',
                        value='My source code is publicly available to view on '
                              'GitHub [here](https://github.com/LoadXBare/LoadXBare-Bot)!\n'
                              'You can also view the [Trello](https://trello.com/b/3WbHFrY8) for development updates!',
                        inline=False)
        embed.set_thumbnail(url='https://i.imgur.com/S4MmPpL.png')
        await ctx.reply(embed=embed,
                        mention_author=False)

    @commands.command(aliases=['h', 'commands', 'commandslist', 'commandlist'],
                      name='help')
    async def help(self, ctx):
        embed = discord.Embed(title='__Commands List__',
                              color=ctx.author.color)
        fun_commands, utility_commands = '', ''
        fun_commands_list, utility_commands_list = [], []

        for command in self.client.walk_commands():
            if command.cog_name == 'Fun':
                fun_commands_list.append(str(command))
            elif command.cog_name == 'Utility':
                utility_commands_list.append(str(command))

        fun_commands_list = sorted(fun_commands_list)
        utility_commands_list = sorted(utility_commands_list)

        for item in fun_commands_list:
            fun_commands += f'`{item}`, '
        for item in utility_commands_list:
            utility_commands += f'`{item}`, '

        embed.add_field(name='Fun :tada:',
                        value=fun_commands.rstrip(', '),
                        inline=False)
        embed.add_field(name='Utility :tools:',
                        value=utility_commands.rstrip(', '),
                        inline=False)
        embed.set_thumbnail(url=self.client.user.avatar_url)
        embed.set_footer(text='Developed by LoadXBare#7156')
        await ctx.reply(embed=embed,
                        mention_author=False)

    @commands.command(name='ping')
    async def ping(self, ctx):
        embed = discord.Embed(color=ctx.author.color)

        embed.add_field(name='Ping :stopwatch:',
                        value=f'{round(self.client.latency * 1000)}ms',
                        inline=False)
        await ctx.reply(embed=embed,
                        mention_author=False)

    @commands.command(name='uptime')
    async def uptime(self, ctx):
        delta_uptime = datetime.datetime.utcnow() - start_time
        embed = discord.Embed(color=ctx.author.color)
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        days, hours = divmod(hours, 24)
        minutes, seconds = divmod(remainder, 60)

        embed.add_field(name='Uptime :calendar:',
                        value=f'{days} days, {hours} hours, {minutes} minutes, {seconds} seconds',
                        inline=False)
        await ctx.reply(embed=embed,
                        mention_author=False)
