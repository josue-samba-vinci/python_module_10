from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count = 0

    def increment() -> int:
        nonlocal count
        count += 1
        return count
    return increment


def spell_accumulator(initial_power: int) -> Callable:
    def accumulated(power_added: int) -> int:
        nonlocal initial_power
        initial_power += power_added
        return initial_power
    return accumulated


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment_item(item: str) -> str:
        return enchantment_type + " " + item
    return enchantment_item


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any:
        return memory.get(key, "Memory not found")
    return {"store": store, "recall": recall}


if __name__ == "__main__":
    counter_a = mage_counter()
    print("counter 1")
    print(counter_a())
    print(counter_a())
    print(counter_a())
    counter_b = mage_counter()
    print("counter 2")
    print(counter_b())
    print(counter_b())
    print(counter_b())
    accumulator1 = spell_accumulator(10)
    print("accumulator 1")
    print(accumulator1(20))
    print(accumulator1(20))
    print(accumulator1(20))
    accumulator2 = spell_accumulator(10)
    print("accumulator 2")
    print(accumulator2(20))
    print(accumulator2(20))
    print(accumulator2(20))
    enchantment1 = enchantment_factory("Flaming")
    print(enchantment1("Sword"))
    print(enchantment1("Axe"))
    enchantment1 = enchantment_factory("Steel")
    print(enchantment1("Axe"))
    vault1 = memory_vault()
    vault1['store']('bank_balance', 100000)
    vault1['store']('bank_creation', "10/02/3033")
    print(vault1['recall']('bank_balance'))
    print(vault1['recall']('bank_creation'))
    print(vault1['recall']('blabla'))
