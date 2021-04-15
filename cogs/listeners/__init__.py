from .listeners import OnCommand, OnReady


def init_listeners(client):
    client.add_cog(OnCommand(client))
    client.add_cog(OnReady(client))
