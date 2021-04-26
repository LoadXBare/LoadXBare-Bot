import datetime
import discord
from discord.ext import commands


class Listeners(commands.Cog):
    def __init__(self, client):
        self.client = client

    start_time = datetime.datetime.utcnow()

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game(name='UwU | .help'))
        print(f'Successfully logged in as {self.client.user}, id: {self.client.user.id}!')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        ignored = (commands.CommandNotFound, )

        if hasattr(ctx.command, 'on_error'):
            return
        elif isinstance(error, ignored):
            return
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(color=ctx.author.color)
            embed.add_field(name='Error :warning:',
                            value=f'The command `{self.client.command_prefix}{ctx.command}` '
                                  f'requires **1 or more** arguments!', inline=False)
            await ctx.reply(embed=embed, mention_author=False)
            return
        raise error
