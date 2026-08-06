from functools import reduce, partial
import operator
from collections.abc import Callable
from typing import Any

def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    spells_dict = {"add": operator.add,
                   "multiply": operator.mul,
                   "max": max,
                   "min": min}
    if operation in spells_dict:
        return reduce(spells_dict[operation], spells)
    else:
        raise ValueError("Unknow operation")

def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    enchantment_dict: dict[str, Callable] = {}
    enchantment_dict["Earth"] = partial(base_enchantment, power=50, element="Earth")
    enchantment_dict["Air"] = partial(base_enchantment, power=50, element="Air")
    enchantment_dict["Fire"] = partial(base_enchantment, power=50, element="Fire")
    return enchantment_dict

def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element} element hits {target} with {power} power"

def memoized_fibonacci(n: int) -> int:
    ...

def spell_dispatcher() -> Callable[[Any], str]:
    ...

if __name__ == "__main__":
    print(spell_reducer([1,2,3], "add"))
    print(spell_reducer([1,2,3], "multiply"))
    print(spell_reducer([1,2,3], "min"))
    print(spell_reducer([1,3,2], "max"))
    try:
        print(spell_reducer([1,2,3], "bla"))
    except ValueError as e:
        print(e)
    enchantment = partial_enchanter(base_enchantment)
    print(enchantment["Earth"](target="creature1"))
    print(enchantment["Air"](target="creature2"))
    print(enchantment["Fire"](target="creature3"))
