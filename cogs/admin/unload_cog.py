import os

import discord
from discord.ext import commands


class UnloadCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def unload_cog(self, ctx, extension):
        for subdir, dirs, files in os.walk('./cogs'):
            for filename in files:
                if filename.endswith('.py') and filename[:-3] == extension:
                    extension_path = subdir[2:].replace('\\', '.') + '.' + filename[:-3]
                    self.client.unload_extension(extension_path)
                    embed = discord.Embed(color=0x1e507d)
                    embed.add_field(name=':gear: Cog :gear:',
                                    value=f'<:success:820648498893553685> Successfully loaded the cog **{extension}**!',
                                    inline=False)
                    await ctx.send(embed=embed)
                    return
        embed = discord.Embed(color=0x1e507d)
        embed.add_field(name=':gear: Cog :gear:',
                        value=f'<:fail:820648499183878154> Unable to find the cog **{extension}**!',
                        inline=False)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(UnloadCog(client))
