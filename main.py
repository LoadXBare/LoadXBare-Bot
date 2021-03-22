from discord.ext import commands
from cogs.init_cogs import init_cogs

client = commands.Bot(command_prefix='.')
client.remove_command('help')

init_cogs(client)

client.run('TOKEN')
