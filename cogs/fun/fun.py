import math
import os
import random
import discord
from discord.ext import commands


class Bunger(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def bunger(self, ctx):
        embed = discord.Embed(color=ctx.author.color)

        embed.set_image(url=os.getenv('BUNGER_IMAGE'))
        await ctx.reply(embed=embed,
                        mention_author=False)


class EightBall(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *args):
        embed_name = ':8ball: 8ball :8ball:'
        embed = discord.Embed(color=ctx.author.color)
        responses = ['As I see it, yes.', 'Don’t count on it.', 'It is certain.',
                     'It is decidedly so.', 'Most likely.', 'My reply is no.',
                     'My sources say no.', 'Outlook good.', 'Outlook not so good.',
                     'Signs point to yes.', 'Very doubtful.', 'Without a doubt.',
                     'Yes – definitely.', 'Yes.', 'You may rely on it.']

        if len(args) == 0:
            embed.add_field(name=embed_name,
                            value=':warning: This command requires **1 or more** arguments!\n'
                                  'Example 1: `.8ball Is @LoadXBare a nerd?`\n'
                                  'Example 2: `.8ball Gaming?`',
                            inline=False)
            await ctx.reply(embed=embed,
                            mention_author=False)
            return

        embed.add_field(name=embed_name,
                        value=random.choice(responses),
                        inline=False)
        await ctx.reply(embed=embed,
                        mention_author=False)


class Flip(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def flip(self, ctx):
        embed = discord.Embed(color=ctx.author.color)
        num = random.randint(0, 1)
        responses = ['Heads!', 'Tails!']
        images = [os.getenv('FLIP_IMAGE_1'), os.getenv('FLIP_IMAGE_2')]

        embed.add_field(name=':coin: Flip :coin:',
                        value=responses[num],
                        inline=False)
        embed.set_image(url=images[num])
        await ctx.reply(embed=embed,
                        mention_author=False)


class Loaf(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def loaf(self, ctx):
        embed = discord.Embed(color=ctx.author.color)

        embed.add_field(name=':bread: LoafXBare :bread:',
                        value='I am not a loaf of bread ;-;\n'
                              'Perhaps you meant to run the command `.load`',
                        inline=False)
        embed.set_image(url=os.getenv('LOAF_IMAGE'))
        await ctx.reply(embed=embed,
                        mention_author=False)


class Owo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def owo(self, ctx):
        embed = discord.Embed(color=ctx.author.color)

        embed.set_image(url=os.getenv('OWO_IMAGE'))
        await ctx.reply(embed=embed,
                        mention_author=False)


class PetTheBot(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def petthebot(self, ctx):
        embed = discord.Embed(color=ctx.author.color)

        embed.set_image(url=os.getenv('PETTHEBOT_IMAGE'))
        await ctx.reply(embed=embed,
                        mention_author=False)


class PetTheBunger(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def petthebunger(self, ctx):
        embed = discord.Embed(color=ctx.author.color)

        embed.set_image(url=os.getenv('PETTHEBUNGER_IMAGE'))
        await ctx.reply(embed=embed,
                        mention_author=False)


class Rate(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rate(self, ctx, *args):
        embed_name = ':memo: Rate :memo:'
        embed = discord.Embed(color=ctx.author.color)
        rating = random.randint(0, 101)
        query = ' '.join(args).replace('_', '').replace('*', '').replace('`', '')

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
            embed.set_image(url=os.getenv('RATE_IMAGE_1'))
            await ctx.reply(embed=embed,
                            mention_author=False)
            return

        if rating == 101:
            rating = 11
        else:
            rating = int(math.ceil(rating / 10.0))

        responses = [f'Hmmm, I would rate **{query}** at a solid **{rating} / 10**!',
                     f'I think **{query}** deserves a **{rating} / 10**!',
                     f'Heh, easy, **{query}** is a **{rating} / 10**!',
                     f'**{query}**? Sounds like a **{rating} / 10**!',
                     f'Oh, **{query}** is definitely a **{rating} / 10**!',
                     f'**{query}** is a **{rating} / 10** in my books!']

        embed.add_field(name=embed_name,
                        value=random.choice(responses),
                        inline=False)

        if rating == 11:
            embed.set_image(url=os.getenv('RATE_IMAGE_2'))
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
            embed.set_image(url=os.getenv('RATE_IMAGE_3'))
        await ctx.reply(embed=embed,
                        mention_author=False)


class Uwu(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def uwu(self, ctx):
        embed = discord.Embed(color=ctx.author.color)

        embed.set_image(url=os.getenv('UWU_IMAGE'))
        await ctx.reply(embed=embed,
                        mention_author=False)
