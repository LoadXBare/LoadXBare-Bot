import math
import discord
import random
from discord.ext import commands


class Rate(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rate(self, ctx, *args):
        embed_name = ':memo: Rate :memo:'
        if len(args) > 1 or len(args) == 0:
            embed = discord.Embed(color=0x1e507d)
            embed.add_field(name=embed_name,
                            value=':warning: This command requires **1** argument!\n'
                                  'Example 1: `.rate @LoadXBare`\n'
                                  'Example 2: `.rate "Among Us"`',
                            inline=False)
            await ctx.send(embed=embed)
            return

        if len(args[0]) > 32:
            embed = discord.Embed(color=0x1e507d)
            embed.add_field(name=embed_name,
                            value=':warning: The thing you are rating cannot exceed **32** characters!',
                            inline=False)
            await ctx.send(embed=embed)
            return

        if args[0] == '<@!819664773146345503>' or args[0] == '<@819664773146345503>':
            embed = discord.Embed(color=0x1e507d)
            embed.add_field(name=embed_name,
                            value='I will always be a **10 / 10**',
                            inline=False)
            embed.set_image(url='https://i.imgur.com/1dqEXs5.png')
            await ctx.send(embed=embed)
            return

        rating = random.randint(0, 101)
        if rating == 101:
            embed = discord.Embed(color=0x1e507d)
            embed.add_field(name=embed_name,
                            value='Hmmm, I would rate **' + args[0] + '** at a solid **' + str(rating) + ' / 10**!',
                            inline=False)
            embed.set_image(url='https://i.imgur.com/XyX0Xip.gif')
        else:
            rating = int(math.ceil(rating / 10.0))
            if rating == 10:
                embed = discord.Embed(color=0x1e507d)
                embed.add_field(name=embed_name,
                                value='Hmmm, I would rate **' + args[0] + '** at a solid **' + str(rating) + ' / 10**!',
                                inline=False)
                embed.set_image(url='https://i.imgur.com/G4AvmnO.png')
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(color=0x1e507d)
                embed.add_field(name=embed_name,
                                value='Hmmm, I would rate **' + args[0] + '** at a solid **' + str(rating) + ' / 10**!',
                                inline=False)
                await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Rate(client))
