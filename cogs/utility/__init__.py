from .code import Code
from .help import Help
from .ping import Ping


def init_utility(client):
    client.add_cog(Code(client))
    client.add_cog(Help(client))
    client.add_cog(Ping(client))
