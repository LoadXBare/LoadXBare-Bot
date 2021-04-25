from .utility import Utility


def init_utility(client):
    client.add_cog(Utility(client))
