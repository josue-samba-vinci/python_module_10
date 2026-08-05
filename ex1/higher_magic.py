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

def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        amplified_power = power * multiplier
        return base_spell(target, amplified_power)
    return amplified

if __name__ == "__main__":
    combo1 = spell_combiner(fireball, heal)
    print(combo1("creature1", 10))
    combo2 = spell_combiner(fireball, fireball)
    print(combo2("creature2", 50))
    combo3 = spell_combiner(heal, heal)
    print(combo3("creature3", 20))
    amplified_fireball = power_amplifier(fireball, 2)
    print(amplified_fireball("creature4", 50))