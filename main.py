import random
import math
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='UwU | .help'))
    print(f'Logged in as {client.user}, id: {client.user.id}')


@client.event
async def on_command(ctx):
    print(f'{ctx.author} ran the command {ctx.message.content} in #{ctx.channel}')


@client.command()
async def ping(ctx):
    embed = discord.Embed(color=0x1e507d)
    embed.add_field(name='Ping',
                    value=' :stopwatch: - ' + str(round(client.latency * 1000)) + 'ms',
                    inline=False)
    await ctx.send(embed=embed)


@client.command()
async def code(ctx):
    embed = discord.Embed(color=0x1e507d)
    embed.add_field(name='Code',
                    value='My code is publicly available to view on GitHub [here](https://github.com/LoadXBare/LoadXBare-Bot)!',
                    inline=False)
    await ctx.send(embed=embed)


@client.command(aliases=['8ball'])
async def _8ball(ctx, *args):
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


@client.command()
async def load(ctx):
    embed = discord.Embed(color=0x1e507d)
    embed.set_image(url='https://i.imgur.com/bsLgC8a.png')
    await ctx.send(embed=embed)
    if ctx.channel.id == 799220260695441418:
        embed.set_image(url='https://i.imgur.com/0E9SUSm.png')
        await ctx.send(embed=embed)


@client.command()
async def loaf(ctx):
    embed = discord.Embed(color=0x1e507d)
    embed.add_field(name="LoafXBare",
                    value="I am not a loaf of bread ;-;\n"
                          "Perhaps you meant to run the command `.load`",
                    inline=False)
    embed.set_image(url='https://i.imgur.com/NAdoFK6.png')
    await ctx.send(embed=embed)


@client.command()
async def petthebot(ctx):
    embed = discord.Embed(color=0x1e507d)
    embed.set_image(url='https://i.imgur.com/sOA7hzb.gif')
    await ctx.send(embed=embed)


@client.command()
async def bunger(ctx):
    embed = discord.Embed(color=0x1e507d)
    embed.set_image(url='https://i.imgur.com/SlkSrxI.gif')
    await ctx.send(embed=embed)


@client.command()
async def petthebunger(ctx):
    embed = discord.Embed(color=0x1e507d)
    embed.set_image(url='https://i.imgur.com/avHG1hq.gif')
    await ctx.send(embed=embed)


@client.command()
async def owo(ctx):
    embed = discord.Embed(color=0x1e507d)
    embed.set_image(url='https://i.imgur.com/M9oRGbT.png')
    await ctx.send(embed=embed)


@client.command()
async def uwu(ctx):
    embed = discord.Embed(color=0x1e507d)
    embed.set_image(url='https://i.imgur.com/jJfknqA.png')
    await ctx.send(embed=embed)


@client.command()
async def rate(ctx, *args):
    if len(args) > 1 or len(args) == 0:
        embed = discord.Embed(color=0x1e507d)
        embed.add_field(name='Rate',
                        value=':warning: This command requires **1** argument!\n'
                              'Example 1: `.rate @LoadXBare`\n'
                              'Example 2: `.rate "Among Us"`',
                        inline=False)
        await ctx.send(embed=embed)
        return

    if len(args[0]) > 32:
        embed = discord.Embed(color=0x1e507d)
        embed.add_field(name='Rate',
                        value=':warning: The thing you are rating cannot exceed **32** characters!',
                        inline=False)
        await ctx.send(embed=embed)
        return

    if args[0] == '<@!819664773146345503>' or args[0] == '<@819664773146345503>':
        embed = discord.Embed(color=0x1e507d)
        embed.add_field(name='Rate',
                        value='I will always be a **10 / 10**',
                        inline=False)
        embed.set_image(url='https://i.imgur.com/1dqEXs5.png')
        await ctx.send(embed=embed)
        return

    rating = random.randint(0, 101)
    if rating == 101:
        embed = discord.Embed(color=0x1e507d)
        embed.add_field(name='Rate',
                        value='Hmmm, I would rate **' + args[0] + '** at a solid **' + str(rating) + ' / 10**!',
                        inline=False)
        embed.set_image(url='https://i.imgur.com/XyX0Xip.gif')
    else:
        rating = int(math.ceil(rating / 10.0))
        if rating == 10:
            embed = discord.Embed(color=0x1e507d)
            embed.add_field(name='Rate',
                            value='Hmmm, I would rate **' + args[0] + '** at a solid **' + str(rating) + ' / 10**!',
                            inline=False)
            embed.set_image(url='https://i.imgur.com/G4AvmnO.png')
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(color=0x1e507d)
            embed.add_field(name='Rate',
                            value='Hmmm, I would rate **' + args[0] + '** at a solid **' + str(rating) + ' / 10**!',
                            inline=False)
            await ctx.send(embed=embed)


@client.command()
async def help(ctx):
    embed = discord.Embed(title='__Commands List__',
                          color=0x1e507d)
    embed.add_field(name='Utility',
                    value='`.code`, `.help`, `.ping`',
                    inline=False)
    embed.add_field(name='Fun',
                    value='`.8ball`, `.bunger`, `.load`, '
                          '`.loaf`, `.owo`, `.petthebot`, '
                          '`.petthebunger`, `.rate`, `.uwu`',
                    inline=False)
    embed.set_footer(text='LoadXBare Bot v1.11.0')
    await ctx.send(embed=embed)

client.run('TOKEN')
