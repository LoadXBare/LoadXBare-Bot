from cogs.fun import Fun
from cogs.listeners import Listeners
from cogs.user import User
from cogs.utility import Utility


def init_cogs(client):
    cogs = [Fun, Listeners, User, Utility]
    for cog in cogs:
        client.add_cog(cog(client))
