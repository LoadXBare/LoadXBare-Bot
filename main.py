import os
from discord.ext import commands
from cogs.__init__ import init_cogs

client = commands.Bot(command_prefix='.', help_command=None, case_insensitive=True)
init_cogs(client)

client.run(os.getenv('BOT_TOKEN'))
