from discord.ext import commands
from cogs.__init__ import init_cogs

client = commands.Bot(command_prefix='.', help_command=None)

init_cogs(client)

client.run('TOKEN')
