from collections.abc import Callable
import sys

def mage_counter() -> Callable:
    count = 0
    def increment() -> int:
        nonlocal count
        count += 1
        return count
    return increment

def spell_accumulator(initial_power: int) -> Callable:
    ...

def enchantment_factory(enchantment_type: str) -> Callable:
    ...

def memory_vault() -> dict[str, Callable]:
    ...


if __name__ == "__main__":
    number = mage_counter()
    print(number())
    print(number())
    print(number())
