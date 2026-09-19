from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1.capabilities import TransformCapability, HealCapability


class BattleStrategy(ABC):

    @abstractmethod
    def act(self, creature: Creature):
        ...

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...


class InvalidStrategyError(Exception):
    ...


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> str:
        if self.is_valid(creature):
            return f"{creature.attack()}"
        else:
            raise InvalidStrategyError("Invalid Creature"
                                       f"'{creature.get_name()}'"
                                       " for this normal strategy")


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> str:
        if isinstance(creature, TransformCapability) \
                and self.is_valid(creature):
            return (f"{creature.transform()}\n"
                    f"{creature.attack()}\n"
                    f"{creature.revert()}")
        else:
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.get_name()}'"
                " for this aggressive strategy")


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> str:
        if isinstance(creature, HealCapability) and self.is_valid(creature):
            return f"{creature.attack()}\n{creature.heal()}"
        else:
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.get_name()}'"
                " for this defensive strategy")
