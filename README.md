# python7 — DataDeck: Abstract Card Architecture

42 project. Practicing abstract classes and three design patterns
(Abstract Factory, Capabilities/mixins, Strategy) through a
creature-card system.

## Requirements

- Python 3.10+
- flake8 (no errors)
- mypy (full type hints)
- No external libraries

## Structure

```
ex0/            Creature, CreatureFactory and the Flame/Aqua families
ex1/            HealCapability, TransformCapability and two new families
ex2/            BattleStrategy and the three concrete strategies
battle.py       ex0 demo: describe/attack, then a base-vs-base fight
capacitor.py    ex1 demo: capabilities inserted into the attack flow
tournament.py   ex2 demo: battle() runs a round-robin tournament
```

Each exercise package only exposes its factories (or strategies)
through `__init__.py` — concrete Creature and capability classes stay
internal.

## Usage

```bash
python3 battle.py
python3 capacitor.py
python3 tournament.py
```

## Checks

```bash
flake8 .
mypy .
```
