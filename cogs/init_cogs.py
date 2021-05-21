from cogs.fun import Fun
from cogs.listeners import Listeners
from cogs.utility import Utility


def init_cogs(client):
    cogs = [Fun, Listeners, Utility]
    for cog in cogs:
        client.add_cog(cog(client))
