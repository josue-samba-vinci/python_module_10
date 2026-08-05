from collections.abc import Callable

def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[str, str]:
        result1 = spell1(target, power)
        result2 = spell2(target, power)
        return (result1, result2)
    return combined

def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} HP"

def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"

if __name__ == "__main__":
    combined = spell_combiner(fireball, heal)
    print(combined("creature1", 10))
    print(combined("creature2", 50))
    print(combined("creature3", 80))
    print(combined("creature4", 100))