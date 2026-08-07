from functools import wraps
from collections.abc import Callable
from typing import Any
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> str:
        print(f"Casting {func.__name__}")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        duration = end - start
        print(f"Spell completed in {duration:.7f} seconds")
        return result
    return wrapper


@spell_timer
def fireball() -> str:
    return "Result: Fireball cast!"

@spell_timer
def waterfall() -> str:
    return "Result: Waterfall cast!"


def power_validator(min_power: int) -> Callable:
    ...


def retry_spell(max_attempts: int) -> Callable:
    ...


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        ...

    def cast_spell(self, spell_name: str, power: int) -> str:
        ...


if __name__ == "__main__":
    print("Testing spell timer...")
    print(fireball())
    print(waterfall())
