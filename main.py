import os
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='UwU | .help'))
    print(f'Successfully logged in as {client.user}, id: {client.user.id}!')


@client.event
async def on_command(ctx):
    print(f'{ctx.author} ran the command .{ctx.command} in #{ctx.channel}')


for subdir, dirs, files in os.walk('./cogs'):
    for filename in files:
        filepath = subdir[2:].replace('\\', '.') + '.' + filename[:-3]
        if filename.endswith('.py'):
            client.load_extension(filepath)

client.run('TOKEN')
