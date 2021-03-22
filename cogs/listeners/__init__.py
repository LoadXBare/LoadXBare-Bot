from .on_command import OnCommand
from .on_ready import OnReady


def init_listeners(client):
    client.add_cog(OnCommand(client))
    client.add_cog(OnReady(client))
