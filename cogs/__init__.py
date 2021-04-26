from dotenv import load_dotenv
from cogs.fun import Fun
from cogs.listeners import Listeners
from cogs.user import User
from cogs.utility import Utility


def init_cogs(client):
    load_dotenv()
    client.add_cog(Fun(client))
    client.add_cog(Listeners(client))
    client.add_cog(User(client))
    client.add_cog(Utility(client))
