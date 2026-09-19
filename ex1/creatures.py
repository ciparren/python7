from ex0.creatures import Creature
from .capabilities import HealCapability, TransformCapability


class Sproutling(Creature, HealCapability):
    def heal(self, target: str = "") -> str:
        return "Sproutling heals itself for a small amount"

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"


class Bloomelle(Creature, HealCapability):
    def heal(self, target: str = "") -> str:
        return "Bloomelle heals itself and others for a large amount"

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"


class Shiftling(Creature, TransformCapability):
    def transform(self) -> str:
        self._transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        self._transformed = False
        return "Shiftling returns to normal."

    def attack(self) -> str:
        if self._transformed:
            return "Shiftling performs a boosted strike!"
        else:
            return "Shiftling attacks normally."


class Morphagon(Creature, TransformCapability):
    def transform(self) -> str:
        self._transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        self._transformed = False
        return "Morphagon stabilizes its form."

    def attack(self) -> str:
        if self._transformed:
            return "Morphagon unleashes a devastating morph strike!"
        else:
            return "Morphagon attacks normally."
