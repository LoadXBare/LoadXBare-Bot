from cogs.fun.__init__ import init_fun
from cogs.listeners.__init__ import init_listeners
from cogs.utility.__init__ import init_utility


def init_cogs(client):
    init_fun(client)
    init_listeners(client)
    init_utility(client)
