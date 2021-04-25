from .listeners import Listeners


def init_listeners(client):
    client.add_cog(Listeners(client))
