from cogs.init_cogs import init_cogs
from discord.ext import commands
import os

client = commands.Bot(command_prefix='.',
                      help_command=None,
                      case_insensitive=True)
init_cogs(client)

client.run(os.getenv('TOKEN'))
