import discord
from discord.ext import commands


class OnReady(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game(name='UwU | .help'))
        print(f'Successfully logged in as {self.client.user}, id: {self.client.user.id}!')
