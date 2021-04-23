import discord
from discord.ext import commands


class OnCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command(self, ctx):
        if str(ctx.command) not in self.client.command_name:
            self.client.command_name.append(str(ctx.command))
            self.client.command_times_used.append(0)

        if str(ctx.command) in self.client.command_name:
            index = self.client.command_name.index(str(ctx.command))
            self.client.command_times_used[index] += 1


class OnReady(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game(name='UwU | .help'))
        print(f'Successfully logged in as {self.client.user}, id: {self.client.user.id}!')
