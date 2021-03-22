from discord.ext import commands


class OnCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command(self, ctx):
        print(f'{ctx.author} ran the command .{ctx.command} in #{ctx.channel}')


def setup(client):
    client.add_cog(OnCommand(client))
