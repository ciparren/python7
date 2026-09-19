from ex0 import CreatureFactory
from ex1.capabilities import HealCapability, TransformCapability
from ex1 import HealingCreatureFactory, TransformCreatureFactory


def try_factory(factory: CreatureFactory) -> None:
    print("Testing Creature with healing capability")
    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    if isinstance(base, HealCapability):
        print(base.heal())
    print(" evolved:")
    evolve = factory.create_evolved()
    print(evolve.describe())
    print(evolve.attack())
    if isinstance(evolve, HealCapability):
        print(evolve.heal())


def try_factory2(factory: CreatureFactory) -> None:
    print("Testing Creature with transform capability")
    print(" base:")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    if isinstance(base, TransformCapability):
        print(base.transform())
        print(base.attack())
        print(base.revert())
    print(" evolved:")
    evolve = factory.create_evolved()
    print(evolve.describe())
    print(evolve.attack())
    if isinstance(evolve, TransformCapability):
        print(evolve.transform())
        print(evolve.attack())
        print(evolve.revert())


if __name__ == "__main__":
    try_factory(HealingCreatureFactory())
    try_factory2(TransformCreatureFactory())
