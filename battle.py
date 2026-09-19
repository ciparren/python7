from ex0 import FlameFactory, AquaFactory, CreatureFactory


def try_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolve = factory.create_evolved()
    print(evolve.describe())
    print(evolve.attack())


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")
    b1 = factory1.create_base()
    b2 = factory2.create_base()
    print(b1.describe())
    print(" vs.")
    print(b2.describe())
    print(" fight!")
    print(b1.attack())
    print(b2.attack())


if __name__ == "__main__":
    try_factory(FlameFactory())
    print()
    try_factory(AquaFactory())
    print()
    battle(FlameFactory(), AquaFactory())
