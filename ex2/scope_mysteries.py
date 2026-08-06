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
    def accumulated(power_added: int) -> int:
        nonlocal initial_power
        initial_power += power_added
        return initial_power
    return accumulated

def enchantment_factory(enchantment_type: str) -> Callable:
    ...

def memory_vault() -> dict[str, Callable]:
    ...


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
