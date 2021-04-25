from .fun import Fun


def init_fun(client):
    client.add_cog(Fun(client))
