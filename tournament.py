from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy, InvalidStrategyError,
    NormalStrategy, AggressiveStrategy, DefensiveStrategy,
)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    print()

    fighters = []
    for factory, strategy in opponents:
        creature = factory.create_base()
        fighters.append((creature, strategy))

    for i in range(len(fighters)):
        for j in range(i + 1, len(fighters)):
            creature1, strategy1 = fighters[i]
            creature2, strategy2 = fighters[j]

            print("* Battle *")
            print(creature1.describe())
            print(" vs.")
            print(creature2.describe())
            print(" now fight!")

            try:
                print(strategy1.act(creature1))
                print(strategy2.act(creature2))
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    print("Tournament 0 (basic)")
    battle([
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ])
    print()

    print("Tournament 1 (error)")
    battle([
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ])
    print()

    print("Tournament 2 (multiple)")
    battle([
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ])
