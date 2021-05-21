from cogs.constants import is_bot, database
from discord.ext import commands
import discord
import math
import random
import re


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='bunger')
    async def bunger(self, ctx):
        embed = discord.Embed(color=ctx.author.color)

        embed.set_image(url='https://i.imgur.com/h9Yg2VE.gif')
        await ctx.reply(embed=embed,
                        mention_author=False)

    @commands.command(aliases=['8b'],
                      name='8ball')
    async def eightball(self, ctx, *, args):
        embed = discord.Embed(color=ctx.author.color)
        responses = ['As I see it, yes.', 'Don’t count on it.', 'It is certain.',
                     'It is decidedly so.', 'Most likely.', 'My reply is no.',
                     'My sources say no.', 'Outlook good.', 'Outlook not so good.',
                     'Signs point to yes.', 'Very doubtful.', 'Without a doubt.',
                     'Yes – definitely.', 'Yes.', 'You may rely on it.']

        if args.endswith('?') is False:
            embed.add_field(name=':warning: Not a question!',
                            value='That doesn\'t look like a question, end your sentence with a `?`.',
                            inline=False)
            await ctx.reply(embed=embed,
                            mention_author=False)
            return

        embed.add_field(name=':8ball: 8ball',
                        value=random.choice(responses),
                        inline=False)
        await ctx.reply(embed=embed,
                        mention_author=False)

    @commands.command(aliases=['coin', 'coinflip'],
                      name='flip')
    async def flip(self, ctx):
        embed = discord.Embed(color=ctx.author.color)
        random_num = random.randrange(0, 3, 2)
        responses = ['Heads!', 'https://i.imgur.com/qk9SJG1.png',
                     'Tails!', 'https://i.imgur.com/NmQOV5v.png']

        embed.add_field(name=':coin: Flip',
                        value=responses[random_num],
                        inline=False)
        embed.set_image(url=responses[random_num + 1])
        await ctx.reply(embed=embed,
                        mention_author=False)

    @commands.command(name='owo')
    async def owo(self, ctx):
        embed = discord.Embed(color=ctx.author.color)

        embed.set_image(url='https://i.imgur.com/JgzU6ih.png')
        await ctx.reply(embed=embed,
                        mention_author=False)

    @commands.command(aliases=['petbot'],
                      name='petthebot')
    async def petthebot(self, ctx):
        embed = discord.Embed(color=ctx.author.color)

        embed.set_image(url='https://i.imgur.com/vrxxm3S.gif')
        await ctx.reply(embed=embed,
                        mention_author=False)

    @commands.command(aliases=['petbunger'],
                      name='petthebunger')
    async def petthebunger(self, ctx):
        embed = discord.Embed(color=ctx.author.color)

        embed.set_image(url='https://i.imgur.com/CfFlQne.gif')
        await ctx.reply(embed=embed,
                        mention_author=False)

    @commands.command(name='rate')
    async def rate(self, ctx, *, args):
        embed_name = ':memo: Rate'
        embed = discord.Embed(color=ctx.author.color)
        rating = random.randint(0, 101)
        query = re.sub('[_*`"\n]', '', args)

        if not 0 < len(query) < 128:
            raise Exception('Invalid query length')

        if query in is_bot:
            embed.add_field(name=embed_name,
                            value='I will always be a **10 / 10** <:rate:839967557117149184>',
                            inline=False)
            embed.set_image(url='https://i.imgur.com/1oTcQhf.png')
            await ctx.reply(embed=embed,
                            mention_author=False)
            return

        if rating == 101:
            rating = 11
            embed.set_image(url='https://i.imgur.com/L8kOWon.gif')
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

        if rating == 10:
            if await self.is_user(query):
                embed.clear_fields()
                embed.add_field(name=embed_name,
                                value=f'Awww, **{query}** is a hecking cutie! **{rating} / 10**!')
            embed.set_image(url='https://i.imgur.com/Uc0y3fH.png')
        await ctx.reply(embed=embed,
                        mention_author=False)

    @commands.command(name='uwu')
    async def uwu(self, ctx):
        embed = discord.Embed(color=ctx.author.color)

        embed.set_image(url='https://i.imgur.com/rjW3q5e.png')
        await ctx.reply(embed=embed,
                        mention_author=False)

    @commands.command(name='love')
    async def love(self, ctx, *, args):
        ascii_value = 0
        embed = discord.Embed(color=ctx.author.color)
        embed_name = ':heart: Love'
        query = re.sub('[_*`"\n]', '', args)

        if not 0 < len(query) < 128:
            raise Exception('Invalid query length')

        for character in query:
            ascii_value += ord(character)

        ascii_value += ctx.author.id
        random.seed(ascii_value)
        love_percent = random.randint(0, 100)

        if love_percent == 100:
            emote = ':revolving_hearts:'
            embed.set_image(url='https://i.imgur.com/oXAkKmk.png')
        elif 90 <= love_percent <= 99:
            emote = ':gift_heart:'
        elif 75 <= love_percent <= 89:
            emote = ':sparkling_heart:'
        elif 65 <= love_percent <= 74:
            emote = ':heartpulse:'
        elif 50 <= love_percent <= 64:
            emote = ':two_hearts:'
        elif 25 <= love_percent <= 49:
            emote = ':heartbeat:'
        elif 10 <= love_percent <= 24:
            emote = ':heart:'
        else:
            emote = ':broken_heart:'

        if query in is_bot:
            embed.set_image(url='https://i.imgur.com/EHtN8of.png')
            embed.add_field(name=embed_name,
                            value='I\'m flattered, however I am a bot and so cannot love...',
                            inline=False)
        elif await self.is_user(query) and re.sub('[<@!>]', '', query) == str(ctx.author.id):
            embed.add_field(name=embed_name,
                            value='smh you should always love yourself! **100%**!',
                            inline=False)
            embed.set_image(url='https://i.imgur.com/SbeauiW.gif')
        else:
            embed.add_field(name=embed_name,
                            value=f'**You** and **{query}** are **{love_percent}%** compatible! {emote}',
                            inline=False)

        await ctx.reply(embed=embed,
                        mention_author=False)

    @commands.command(name='hug')
    async def hug(self, ctx, arg):
        embed = discord.Embed(color=ctx.author.color)
        receiver_hugs_received, giver_hugs_given, giver_hugs_received = 0, 0, 0
        values = []

        if await self.is_user(arg) is False or str(ctx.author.id) == re.sub('[<@!>]', '', arg):
            embed.add_field(name=':warning: Invalid user!',
                            value=f'You must **ping another user** to use this command.',
                            inline=False)
            await ctx.reply(embed=embed,
                            mention_author=False)
            return
        else:
            receiver_id = re.sub('[<@!>]', '', arg)
            giver_id = ctx.author.id

        cursor = database.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS hugs (user_id VARCHAR(20), hugs_received VARCHAR(20), hugs_given VARCHAR(20), PRIMARY KEY(user_id))")
        cursor.execute(f"INSERT INTO hugs VALUES ('{receiver_id}', '0', '0') ON CONFLICT DO NOTHING")
        cursor.execute(f"INSERT INTO hugs VALUES ('{giver_id}', '0', '0') ON CONFLICT DO NOTHING")
        database.commit()

        cursor.execute(f"SELECT hugs_received, hugs_given FROM hugs WHERE user_id = '{giver_id}'")
        for x in cursor:
            for value in x:
                values.append(int(value))
        giver_hugs_received = values[0]
        giver_hugs_given = values[1] + 1

        cursor.execute(f"SELECT hugs_received FROM hugs WHERE user_id = '{receiver_id}'")
        for x in cursor:
            for value in x:
                receiver_hugs_received = int(value) + 1

        cursor.execute(f"UPDATE hugs SET hugs_received = '{receiver_hugs_received}' WHERE user_id = '{receiver_id}'")
        cursor.execute(f"UPDATE hugs SET hugs_given = '{giver_hugs_given}' WHERE user_id = '{giver_id}'")
        database.commit()
        cursor.close()

        embed.add_field(name=':people_hugging: Hug',
                        value=f'You have given <@!{receiver_id}> a hug!\n'
                              f'They have been hugged a total of **{receiver_hugs_received}** times!\n'
                              f'<:hugs_received:845338760422096966> {giver_hugs_received} | <:hugs_given:845338760312127528> {giver_hugs_given}',
                        inline=False)
        await ctx.reply(embed=embed,
                        mention_author=False)

    @commands.command(name='choose')
    async def choose(self, ctx, *, args):
        choices = []
        embed = discord.Embed(color=ctx.author.color)
        query = re.sub('[_*`"\n]', '', args).strip()

        if not 0 < len(query) < 128 or not 0 < len(query.replace(',', '').strip()) < 128:
            raise Exception('Invalid query length')

        for arg in query.split(','):
            choices.append(arg.strip())
        choices = list(filter(('').__ne__, choices))
        choice = random.choice(choices)

        responses = [f'I\'ll go for **{choice}**!', f'Hmm, I\'m thinking **{choice}**!',
                     f'**{choice}** sounds good!', f'I\'m gonna go for **{choice}**!',
                     f'Oh, definitely going for **{choice}**!', f'**{choice}** takes my fancy!',
                     f'This is an easy one! **{choice}**!', f'ooh, let\'s go for **{choice}**!']

        embed.add_field(name=':thinking: Choose',
                        value=random.choice(responses),
                        inline=False)
        await ctx.reply(embed=embed,
                        mention_author=False)

    async def is_user(self, user_id):
        try:
            query_user = re.sub('[<@!>]', '', user_id)

            await discord.Client.fetch_user(self=self.client,
                                            user_id=int(query_user))
        except:
            return False
        return True
