from discord.ext import commands
import discord
import os
import random


class User(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='eli')
    async def eli(self, ctx):
        num = random.randrange(0, 3, 2)
        responses = ['FiREA MALM', 'https://i.imgur.com/gdfbqED.png',
                     'when you call eli short', 'https://i.imgur.com/1L0Rc9t.png']
        embed = discord.Embed(title=f'> {responses[num]}',
                              color=ctx.author.color)
        user = await discord.Client.fetch_user(self=self.client,
                                               user_id=448232336472014858)

        embed.set_author(name='Eli',
                         icon_url=user.avatar_url)
        embed.set_image(url=responses[num + 1])
        await ctx.reply(embed=embed,
                        mention_author=False)

    @commands.command(name='lino')
    async def lino(self, ctx):
        embed = discord.Embed(title='> sup mortal',
                              color=ctx.author.color)
        user = await discord.Client.fetch_user(self=self.client,
                                               user_id=332142876207349764)

        embed.set_author(name='Lino',
                         icon_url=user.avatar_url)
        embed.set_image(url='https://i.imgur.com/qiytpdU.png')
        await ctx.reply(embed=embed,
                        mention_author=False)

    @commands.command(aliases=['loadxbare'],
                      name='load')
    async def load(self, ctx):
        embed = discord.Embed(title='> UwU',
                              color=ctx.author.color)
        user = await discord.Client.fetch_user(self=self.client,
                                               user_id=455321156224942091)

        embed.set_author(name='Load',
                         icon_url=user.avatar_url)
        embed.set_image(url='https://i.imgur.com/fMSxU0y.png')
        await ctx.reply(embed=embed,
                        mention_author=False)
        if ctx.channel.id == 799220260695441418:
            embed.set_image(url=os.getenv('LOAD_IMAGE'))
            await ctx.send(embed=embed)

    @commands.command(aliases=['epicnoham'],
                      name='noham')
    async def noham(self, ctx):
        embed = discord.Embed(title='> (Aggressive Silence)',
                              color=ctx.author.color)
        user = await discord.Client.fetch_user(self=self.client,
                                               user_id=528846496620085248)

        embed.set_author(name='Noham',
                         icon_url=user.avatar_url)
        await ctx.reply(embed=embed,
                        mention_author=False)

    @commands.command(aliases=['smellypengu'],
                      name='pengu')
    async def pengu(self, ctx):
        embed = discord.Embed(title='> AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
                              color=ctx.author.color)
        user = await discord.Client.fetch_user(self=self.client,
                                               user_id=322063964219637771)

        embed.set_author(name='Pengu',
                         icon_url=user.avatar_url)
        embed.set_image(url='https://i.imgur.com/5rntduX.gif')
        await ctx.reply(embed=embed,
                        mention_author=False)

    @commands.command(aliases=['qtipster'],
                      name='qtip')
    async def qtip(self, ctx):
        num = random.randrange(0, 3, 2)
        responses = ['I have never fapped', 'https://i.imgur.com/miRpdpK.png',
                     'aha', 'https://i.imgur.com/An4cJSQ.png']
        embed = discord.Embed(title=f'> {responses[num]}',
                              color=ctx.author.color)
        user = await discord.Client.fetch_user(self=self.client,
                                               user_id=453976398701395968)

        embed.set_image(url=responses[num + 1])
        embed.set_author(name='qTiP',
                         icon_url=user.avatar_url)
        await ctx.reply(embed=embed,
                        mention_author=False)

    @commands.command(aliases=['tofucookie'],
                      name='tofu')
    async def tofu(self, ctx):
        embed = discord.Embed(title='> I would like to have a word with you.',
                              color=ctx.author.color)
        images = ['https://i.imgur.com/Ov79PVe.png', 'https://i.imgur.com/yv3QPVR.png',
                  'https://i.imgur.com/3a7nFNA.png', 'https://i.imgur.com/5pIvF6t.png',
                  'https://i.imgur.com/CSuHdjB.png', 'https://i.imgur.com/KlixO73.png',
                  'https://i.imgur.com/0xznrqE.png']
        user = await discord.Client.fetch_user(self=self.client,
                                               user_id=221493681075650560)

        embed.set_author(name='Tofu',
                         icon_url=user.avatar_url)
        embed.set_image(url=random.choice(images))
        await ctx.reply(embed=embed,
                        mention_author=True)
