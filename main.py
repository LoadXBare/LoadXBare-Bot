import datetime
import os
from discord.ext import commands
from cogs.__init__ import init_cogs
from dotenv import load_dotenv

client = commands.Bot(command_prefix='.', help_command=None, case_insensitive=True)
client.start_time = datetime.datetime.utcnow()

init_cogs(client)
load_dotenv()
token = os.getenv('BOT_TOKEN')


client.run(token)
