from .user import Dragon, Eli, Lino, Load, Noham, Pengu, Qtip, Tofu


def init_user(client):
    client.add_cog(Dragon(client))
    client.add_cog(Eli(client))
    client.add_cog(Lino(client))
    client.add_cog(Load(client))
    client.add_cog(Noham(client))
    client.add_cog(Pengu(client))
    client.add_cog(Qtip(client))
    client.add_cog(Tofu(client))
