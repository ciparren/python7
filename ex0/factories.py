import abc
from .creatures import Creature, Flameling, Aquabub, Torragon, Pyrodon


class CreatureFactory(abc.ABC):
    @abc.abstractmethod
    def create_base(self) -> Creature:
        ...

    @abc.abstractmethod
    def create_evolved(self) -> Creature:
        ...


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling("Flameling", "Fire")

    def create_evolved(self) -> Creature:
        return Pyrodon("Pyrodon", "Fire/Flying")


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub("Aquabub", "Water")

    def create_evolved(self) -> Creature:
        return Torragon("Torragon", "Water")
