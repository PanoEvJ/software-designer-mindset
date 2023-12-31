import random
from dataclasses import dataclass
from enum import StrEnum
from typing import Protocol


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


class EnemyFactory(Protocol):
    def spawn_enemy(self) -> list[Enemy]:
        ...


@dataclass
class HardEnemy:
    health = random.randint(70, 100)
    attack_power = random.randint(70, 100)
    defense = random.randint(70, 100)

    def spawn_enemy(self) -> list[Enemy]:
        return [
            Enemy(
                EnemyType.WIZARD,
                health=self.health,
                attack_power=self.attack_power,
                defense=self.defense,
            )
        ]


@dataclass
class MediumEnemy:
    health = random.randint(30, 70)
    attack_power = random.randint(30, 70)
    defense = random.randint(30, 70)

    def spawn_enemy(self) -> list[Enemy]:
        return [
            Enemy(
                enemy_type,
                health=self.health,
                attack_power=self.attack_power,
                defense=self.defense,
            )
            for enemy_type in EnemyType
        ]


@dataclass
class EasyEnemy:
    health = random.randint(1, 30)
    attack_power = random.randint(1, 30)
    defense = random.randint(1, 30)

    def spawn_enemy(self) -> list[Enemy]:
        return [
            Enemy(
                enemy_type,
                health=self.health,
                attack_power=self.attack_power,
                defense=self.defense,
            )
            for enemy_type in [EnemyType.KNIGHT, EnemyType.ARCHER]
        ]


FACTORY: dict[str, EnemyFactory] = {
    "easy": EasyEnemy(),
    "medium": MediumEnemy(),
    "hard": HardEnemy(),
}


def read_choice():
    while True:
        spawn_points = input(f"Enter desired difficulty ({', '.join(FACTORY)}):")
        try:
            return FACTORY[spawn_points]
        except KeyError:
            print(f"Unknown difficulty level: {spawn_points}")


def main() -> None:
    enemies = read_choice()
    # enemy = Enemy(EnemyType.KNIGHT, health=100, attack_power=10, defense=5)
    new_enemies = enemies.spawn_enemy()
    print(new_enemies)


if __name__ == "__main__":
    main()
