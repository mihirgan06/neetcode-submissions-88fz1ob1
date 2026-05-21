class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        # TODO: Initialize the superhero's attributes here
        self.name = name
        self.power = power
        self.health = health


# TODO: Create Superhero instances
Batman = SuperHero("Batman", "Intelligence", 100)
Superman = SuperHero("Superman", "Strength", 150)

# TODO: Print out the attributes of each superhero
print(f"{Batman.name}")
print(f"{Batman.power}")
print(f"{Batman.health}")
print(f"{Superman.name}")
print(f"{Superman.power}")
print(f"{Superman.health}")