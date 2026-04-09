# Створіть абстрактний клас Character, атрибути
#  name – ім’я
#  max_hp – максимальний рівень здоров’я
#  hp – нинішній рівень здоров’я
#  level – рівень персонажа(від 1 до 20)
#  intelligence – стат інтелекту
#  strength – стат сили
#  dexterity – стат спритності
#  mana – стат мани
#  defense – стат захисту
# Методи:
#  attack() – абстрактний метод
#  take_damage(damage) – отримує урон, зменшений на
# захист
#  level_up() – збільшує рівень
#  increase_stat(stat) – збільшує один з статів на 1
#  rest() – відпочинок(відновлює hp до максимального)
#  heal(heal_hp) – збільшує hp на heal_hp

from abc import ABC, abstractmethod
from enum import Enum


class Stat(Enum):
    intelligence = "intelligence"
    strength = "strength"
    dexterity = "dexterity"
    mana = "mana"
    defense = "defense"


class Character(ABC):
    def __init__(
        self,
        name: str,
        max_hp: int,
        intelligence: int,
        strength: int,
        dexterity: int,
        mana: int,
        defense: int,
        level: int = 1,
    ):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.intelligence = intelligence
        self.strength = strength
        self.dexterity = dexterity
        self.mana = mana
        self.defense = defense
        self.level = level

    @abstractmethod
    def attack(self) -> int:
        pass

    def take_damage(self, damage: int):
        actual_damage = damage - self.defense
        if actual_damage < 0:
            actual_damage = 0
        self.hp -= actual_damage
        if self.hp < 0:
            self.hp = 0

    def level_up(self):
        if self.level < 20:
            self.level += 1

    def increase_stat(self, stat: Stat):
        if stat == Stat.intelligence:
            self.intelligence += 1
        elif stat == Stat.strength:
            self.strength += 1
        elif stat == Stat.dexterity:
            self.dexterity += 1
        elif stat == Stat.mana:
            self.mana += 1
        elif stat == Stat.defense:
            self.defense += 1
        else:
            print("Unknown stat")

    def rest(self):
        self.hp = self.max_hp

    def heal(self, heal_hp: int):
        self.hp += heal_hp
        if self.hp > self.max_hp:
            self.hp = self.max_hp


# Створіть дочірній клас Paladin
# Методи:
#  attack() – наносить 4*strength урону та зменшує mana на
# 5, якщо недостатньо, то наносить strength урону
#  shield() – збільшує стат defense на 4+level
#  unshield() – зменшує стат defense на 4+level
#  heal_ally(ally) – лікує союзника на 5 + 2*level + 0.5*mana


class Paladin(Character):
    def attack(self) -> int:
        if self.mana >= 5:
            self.mana -= 5
            return 4 * self.strength

        return 1 * self.strength

    def shield(self):
        self.defense += 4 + self.level

    def unshield(self):
        self.defense -= 4 + self.level

    def heal_ally(self, ally: Character):
        heal_hp = int(5 + 2 * self.level + 0.5 * self.mana)
        ally.heal(heal_hp)


paladin1 = Paladin("ally", 5, 5, 5, 5, 5, 5)
paladin1.unshield()
paladin1.take_damage(6)
paladin1.unshield()

print(paladin1.hp)

paladin2 = Paladin("Paladin", 100, 10, 10, 10, 10, defense=1)
paladin2.level_up()
paladin2.shield()
paladin2.take_damage(20)

# print(character.hp)

paladin2.heal_ally(paladin1)

print(paladin1.hp)
