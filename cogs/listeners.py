from discord.ext import commands
import discord


class Listeners(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game(name='UwU | .help'))
        print(f'Successfully logged in as {self.client.user}, id: {self.client.user.id}!')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        ignored = (commands.CommandNotFound, )
        embed = discord.Embed(color=ctx.author.color)

        if hasattr(ctx.command, 'on_error'):
            return
        elif isinstance(error, ignored):
            return
        elif isinstance(error, commands.MissingRequiredArgument):
            embed.add_field(name=':warning: Missing required arguments!',
                            value=f'The command `{self.client.command_prefix}{ctx.command}` '
                                  f'requires **1 or more** arguments.',
                            inline=False)
            await ctx.reply(embed=embed,
                            mention_author=False)
            return

        # Custom raised errors
        if 'Invalid query length' in str(error):
            embed.add_field(name=':warning: Invalid argument length!',
                            value='The argument(s) you entered must be between **1 to 128** characters in length.',
                            inline=False)
            await ctx.reply(embed=embed,
                            mention_author=False)
            return

        raise error
