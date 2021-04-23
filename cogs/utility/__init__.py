from .utility import Code, Help, Ping, Uptime, Usage


def init_utility(client):
    client.add_cog(Code(client))
    client.add_cog(Help(client))
    client.add_cog(Ping(client))
    client.add_cog(Uptime(client))
    client.add_cog(Usage(client))
