import math
import discord
import random
from discord.ext import commands
from cogs.cog_settings import embed_color


class Rate(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rate(self, ctx, *args):
        embed_name = ':memo: Rate :memo:'
        embed = discord.Embed(color=embed_color)
        rating = random.randint(0, 101)

        if len(args) > 1 or len(args) == 0:
            embed.add_field(name=embed_name,
                            value=':warning: This command requires **1** argument!\n'
                                  'Example 1: `.rate @LoadXBare`\n'
                                  'Example 2: `.rate "Among Us"`',
                            inline=False)
            await ctx.reply(embed=embed,
                            mention_author=False)
            return

        if len(args[0]) > 128:
            embed.add_field(name=embed_name,
                            value=':warning: The thing you are rating cannot exceed **128** characters!',
                            inline=False)
            await ctx.reply(embed=embed,
                            mention_author=False)
            return

        if args[0] == '<@!819664773146345503>' or args[0] == '<@819664773146345503>':
            embed.add_field(name=embed_name,
                            value='I will always be a **10 / 10**',
                            inline=False)
            embed.set_image(url='https://i.imgur.com/1dqEXs5.png')
            await ctx.reply(embed=embed,
                            mention_author=False)
            return

        if rating == 101:
            embed.add_field(name=embed_name,
                            value='Hmmm, I would rate **' + args[0] + '** at a solid **' + str(rating) + ' / 10**!',
                            inline=False)
            embed.set_image(url='https://i.imgur.com/XyX0Xip.gif')
        else:
            rating = int(math.ceil(rating / 10.0))
            if rating == 10:
                embed.add_field(name=embed_name,
                                value='Hmmm, I would rate **' + args[0] + '** at a solid **' + str(rating) + ' / 10**!',
                                inline=False)
                embed.set_image(url='https://i.imgur.com/G4AvmnO.png')
                await ctx.reply(embed=embed,
                                mention_author=False)
            else:
                embed.add_field(name=embed_name,
                                value='Hmmm, I would rate **' + args[0] + '** at a solid **' + str(rating) + ' / 10**!',
                                inline=False)
                await ctx.reply(embed=embed,
                                mention_author=False)
