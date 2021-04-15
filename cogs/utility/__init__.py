from .utility import Code, Help, Ping


def init_utility(client):
    client.add_cog(Code(client))
    client.add_cog(Help(client))
    client.add_cog(Ping(client))
