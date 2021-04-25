import discord
from discord.ext import commands

class Listeners(commands.Cog):
    def __init__(self, client):
        self.client = client

    command_name = []
    command_times_used = []

    @commands.Cog.listener()
    async def on_command(self, ctx):
        if str(ctx.command) not in self.command_name:
            self.command_name.append(str(ctx.command))
            self.command_times_used.append(0)
        if str(ctx.command) in self.command_name:
            index = self.command_name.index(str(ctx.command))
            self.command_times_used[index] += 1

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game(name='UwU | .help'))
        print(f'Successfully logged in as {self.client.user}, id: {self.client.user.id}!')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        cog = ctx.cog

        if hasattr(ctx.command, 'on_error'):
            return
        elif cog and cog._get_overridden_method(cog.cog_command_error) is not None:
            return

        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(color=ctx.author.color)
            embed.add_field(name=':warning: Error :warning:',
                            value=f'The command `{self.client.command_prefix}{ctx.command}` '
                                  f'requires **1 or more** arguments!',
                            inline=False)
            await ctx.reply(embed=embed,
                            mention_author=False)
            return
        raise error
