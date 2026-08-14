from functools import wraps
from collections.abc import Callable
from typing import Any
import time


class SpellFailedError(Exception):
    def __init__(self, message="Spell failed, retrying..."):
        super().__init__(message)
        self.message = message


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
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            power = kwargs.get('power') or args[-1]
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


@power_validator(50)
def thunderstorm(power: int) -> str:
    return f"The thunderstorm hit the tree with {power} power !"


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            for attempts in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except SpellFailedError as e:
                    print(f"{e.message}(attempt {attempts}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


@retry_spell(3)
def unvalid_spell() -> str:
    raise SpellFailedError()


@retry_spell(3)
def valid_spell() -> str:
    return "Waaaaaaagh spelled !"


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if (len(name) >= 3
           and all(char.isalpha() or char.isspace() for char in name)):
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")
    print(fireball())
    print(waterfall())
    print("Testing power validator...")
    print(thunderstorm(70))
    print(thunderstorm(power=30))
    print("Testing unvalid spell...")
    print(unvalid_spell())
    print("Testing valid spell...")
    print(valid_spell())
    mage = MageGuild()
    print("Testing MageGuild...")
    print(mage.validate_mage_name("abron"))
    print(mage.validate_mage_name("ab"))
    print(mage.cast_spell("Lightning", power=15))
    print(mage.cast_spell("Sorcerer", power=5))
