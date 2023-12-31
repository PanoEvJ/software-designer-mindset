import random
from dataclasses import dataclass
from enum import StrEnum


class EnemyType(StrEnum):
    KNIGHT = "knight"
    ARCHER = "archer"
    WIZARD = "wizard"


@dataclass
class Enemy:
    enemy_type: EnemyType
    health: int
    attack_power: int
    defense: int


SPAWN_FACTORY: dict[str, Enemy] = {
    "easy": Enemy(EnemyType.KNIGHT, health=100, attack_power=10, defense=5),
    "medium": Enemy(EnemyType.KNIGHT, health=100, attack_power=10, defense=5),
    "hard": Enemy(EnemyType.KNIGHT, health=100, attack_power=10, defense=5),
}


def read_choice():
    while True:
        spawn_points = input(f"Enter desired difficulty ({', '.join(SPAWN_FACTORY)}):")
        try:
            return SPAWN_FACTORY[spawn_points]
        except KeyError:
            print(f"Unknown difficulty level: {spawn_points}")


def main() -> None:
    enemies = read_choice()
    # enemy = Enemy(EnemyType.KNIGHT, health=100, attack_power=10, defense=5)
    print(enemies)


if __name__ == "__main__":
    main()
