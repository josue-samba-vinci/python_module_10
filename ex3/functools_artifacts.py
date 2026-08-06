from functools import reduce
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
    ...

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
