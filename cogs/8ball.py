import random
import discord
from discord.ext import commands


class _8ball(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *args):
        if len(args) == 0:
            embed = discord.Embed(color=0x1e507d)
            embed.add_field(name='8ball',
                            value=':warning: This command requires **1 or more** arguments!\n'
                                  'Example 1: `.8ball Is @LoadXBare a nerd?`\n'
                                  'Example 2: `.8ball Gaming?`',
                            inline=False)
            await ctx.send(embed=embed)
            return
        responses = ['As I see it, yes.', 'Don’t count on it.',
                     'It is certain.', 'It is decidedly so.',
                     'Most likely.', 'My reply is no.',
                     'My sources say no.', 'Outlook good.',
                     'Outlook not so good.', 'Signs point to yes.',
                     'Very doubtful.', 'Without a doubt.',
                     'Yes – definitely.', 'Yes.', 'You may rely on it.']
        embed = discord.Embed(color=0x1e507d)
        embed.add_field(name='8ball',
                        value=f':8ball: {random.choice(responses)}',
                        inline=False)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(_8ball(client))
