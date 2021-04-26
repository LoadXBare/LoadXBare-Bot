import os
import random
import discord
from discord.ext import commands


class User(commands.Cog):
    def __init__(self, client): self.client = client

    @commands.command()
    async def eli(self, ctx):
        user = await discord.Client.fetch_user(self=self.client, user_id=448232336472014858)
        num = random.randrange(0, 3, 2)
        responses = ['FiREA MALM', os.getenv('ELI_IMAGE_1'), 'when you call eli short', os.getenv('ELI_IMAGE_2')]
        embed = discord.Embed(title=f'> {responses[num]}', color=ctx.author.color)

        embed.set_author(name='Eli', icon_url=user.avatar_url)
        embed.set_image(url=responses[num + 1])
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def lino(self, ctx):
        user = await discord.Client.fetch_user(self=self.client, user_id=332142876207349764)
        embed = discord.Embed(title='> sup mortal', color=ctx.author.color)

        embed.set_author(name='Lino', icon_url=user.avatar_url)
        embed.set_image(url=os.getenv('LINO_IMAGE'))
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def load(self, ctx):
        user = await discord.Client.fetch_user(self=self.client, user_id=455321156224942091)
        embed = discord.Embed(title='> UwU', color=ctx.author.color)

        embed.set_author(name='Load', icon_url=user.avatar_url)
        embed.set_image(url=os.getenv('LOAD_IMAGE_1'))
        await ctx.reply(embed=embed, mention_author=False)
        if ctx.channel.id == 799220260695441418:
            embed.set_image(url=os.getenv('LOAD_IMAGE_2'))
            await ctx.send(embed=embed)

    @commands.command()
    async def noham(self, ctx):
        user = await discord.Client.fetch_user(self=self.client, user_id=528846496620085248)
        embed = discord.Embed(title='> (Aggressive Silence)', color=ctx.author.color)

        embed.set_author(name='Noham', icon_url=user.avatar_url)
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def pengu(self, ctx):
        user = await discord.Client.fetch_user(self=self.client, user_id=322063964219637771)
        embed = discord.Embed(title='> AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', color=ctx.author.color)

        embed.set_author(name='Pengu', icon_url=user.avatar_url)
        embed.set_image(url=os.getenv('PENGU_IMAGE'))
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def qtip(self, ctx):
        user = await discord.Client.fetch_user(self=self.client, user_id=453976398701395968)
        num = random.randrange(0, 3, 2)
        responses = ['I have never fapped', os.getenv('QTIP_IMAGE_1'), 'aha', os.getenv('QTIP_IMAGE_2')]
        embed = discord.Embed(title=f'> {responses[num]}', color=ctx.author.color)

        embed.set_image(url=responses[num + 1])
        embed.set_author(name='qTiP', icon_url=user.avatar_url)
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    async def tofu(self, ctx):
        user = await discord.Client.fetch_user(self=self.client, user_id=221493681075650560)
        images = [os.getenv('TOFU_IMAGE_1'), os.getenv('TOFU_IMAGE_2'),
                  os.getenv('TOFU_IMAGE_3'), os.getenv('TOFU_IMAGE_4'),
                  os.getenv('TOFU_IMAGE_5'), os.getenv('TOFU_IMAGE_6'),
                  os.getenv('TOFU_IMAGE_7'), os.getenv('TOFU_IMAGE_8')]
        embed = discord.Embed(title='> I would like to have a word with you.', color=ctx.author.color)

        embed.set_author(name='Tofu', icon_url=user.avatar_url)
        embed.set_image(url=random.choice(images))
        await ctx.reply(embed=embed, mention_author=True)
