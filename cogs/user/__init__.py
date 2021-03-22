from .dragon import Dragon
from .eli import Eli
from .lino import Lino
from .load import Load
from .noham import Noham
from .pengu import Pengu
from qtip import Qtip
from .tofu import Tofu


def init_user(client):
    client.add_cog(Dragon(client))
    client.add_cog(Eli(client))
    client.add_cog(Lino(client))
    client.add_cog(Load(client))
    client.add_cog(Noham(client))
    client.add_cog(Pengu(client))
    client.add_cog(Qtip(client))
    client.add_cog(Tofu(client))
