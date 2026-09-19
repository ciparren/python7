import abc


class Creature(abc.ABC):
    def __init__(self, name: str, creature_type: str) -> None:
        super().__init__()
        self._name: str = name
        self._type: str = creature_type

    @abc.abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        msg = f"{self._name} is a {self._type} type Creature"
        return msg

    def get_name(self) -> str:
        return self._name


class Flameling(Creature):
    def attack(self) -> str:
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    def attack(self) -> str:
        return "Aquabub uses Water Gun!"


class Torragon(Creature):
    def attack(self) -> str:
        return "Torragon uses Hydro Pump!"
