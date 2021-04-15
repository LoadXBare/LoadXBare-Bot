from .fun import Bunger, EightBall, Flip, Loaf, Owo, PetTheBot, PetTheBunger, Rate, Uwu


def init_fun(client):
    client.add_cog(Bunger(client))
    client.add_cog(EightBall(client))
    client.add_cog(Flip(client))
    client.add_cog(Loaf(client))
    client.add_cog(Owo(client))
    client.add_cog(PetTheBot(client))
    client.add_cog(PetTheBunger(client))
    client.add_cog(Rate(client))
    client.add_cog(Uwu(client))
