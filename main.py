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


@client.command()
async def load_cog(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    embed = discord.Embed(color=0x1e507d)
    embed.add_field(name=':gear: Cog :gear:',
                    value=f'Successfully loaded the cog **{extension}**!',
                    inline=False)
    await ctx.send(embed=embed)


@client.command()
async def unload_cog(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    embed = discord.Embed(color=0x1e507d)
    embed.add_field(name=':gear: Cog :gear:',
                    value=f'Successfully unloaded the cog **{extension}**!',
                    inline=False)
    await ctx.send(embed=embed)


@client.command()
async def reload_cog(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    embed = discord.Embed(color=0x1e507d)
    embed.add_field(name=':gear: Cog :gear:',
                    value=f'Successfully reloaded the cog **{extension}**!',
                    inline=False)
    await ctx.send(embed=embed)

for subdir, dirs, files in os.walk('./cogs'):
    for filename in files:
        filepath = subdir[2:].replace('\\', '.') + '.' + filename[:-3]
        if filename.endswith('.py'):
            client.load_extension(filepath)

client.run('TOKEN')
