from .user import User


def init_user(client):
    client.add_cog(User(client))
