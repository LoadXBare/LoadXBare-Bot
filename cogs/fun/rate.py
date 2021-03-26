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
        query = ' '.join(args).replace('_', '').replace('*', '').replace('`', '')
        responses = [f'Hmmm, I would rate **{query}** at a solid **{rating} / 10**!',
                     f'I think **{query}** deserves a **{rating} / 10**!',
                     f'Heh, easy, **{query}** is a **{rating} / 10**!',
                     f'**{query}**? Sounds like a **{rating} / 10**!',
                     f'Oh, **{query}** is definitely a **{rating} / 10**!',
                     f'**{query}** is a **{rating} / 10** in my books!']

        if ctx.message.content.find('"') != -1:
            embed.add_field(name=embed_name,
                            value=':warning: Refrain from using quotation marks as they may break the bot!',
                            inline=False)
            await ctx.reply(embed=embed,
                            mention_author=False)
            return

        if len(query) == 0:
            embed.add_field(name=embed_name,
                            value=':warning: This command requires **1 or more** arguments!\n'
                                  'Example 1: `.rate @LoadXBare`\n'
                                  'Example 2: `.rate Among Us`',
                            inline=False)
            await ctx.reply(embed=embed,
                            mention_author=False)
            return
        elif len(query) > 128:
            embed.add_field(name=embed_name,
                            value=':warning: The thing you are rating cannot exceed **128** characters!',
                            inline=False)
            await ctx.reply(embed=embed,
                            mention_author=False)
            return

        if query == '<@!819664773146345503>' or query == '<@819664773146345503>':
            embed.add_field(name=embed_name,
                            value='I will always be a **10 / 10**',
                            inline=False)
            embed.set_image(url='https://i.imgur.com/1dqEXs5.png')
            await ctx.reply(embed=embed,
                            mention_author=False)
            return

        if rating == 101:
            rating = 11
        else:
            rating = int(math.ceil(rating / 10.0))

        embed.add_field(name=embed_name,
                        value=random.choice(responses),
                        inline=False)

        if rating == 11:
            embed.set_image(url='https://i.imgur.com/XyX0Xip.gif')
        elif rating == 10:
            if len(args) == 1:
                try:
                    queryuser = query.replace('<', '').replace('!', '').replace('@', '').replace('>', '')
                    await discord.Client.fetch_user(self=self.client, user_id=int(queryuser))
                    embed.clear_fields()
                    embed.add_field(name=embed_name,
                                    value=f'Awww, **{query}** is a hecking cutie! **{rating} / 10**!')
                except:
                    pass
            embed.set_image(url='https://i.imgur.com/G4AvmnO.png')
        await ctx.reply(embed=embed,
                        mention_author=False)
