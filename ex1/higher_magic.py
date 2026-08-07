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


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int) -> str:
        if condition(target, power):
            casted = spell(target, power)
        else:
            casted = "Spell fizzled"
        return casted
    return caster


def enough_power(target: str, power: int) -> bool:
    return power >= 20


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequenced(target: str, power: int) -> list[str]:
        spell_list = []
        for spell in spells:
            spell_list.append(spell(target, power))
        return spell_list
    return sequenced


if __name__ == "__main__":
    combo1 = spell_combiner(fireball, heal)
    print(combo1("creature1", 10))
    combo2 = spell_combiner(fireball, fireball)
    print(combo2("creature2", 50))
    combo3 = spell_combiner(heal, heal)
    print(combo3("creature3", 20))
    amplified_fireball = power_amplifier(fireball, 2)
    print(amplified_fireball("creature4", 50))
    casted_fireball = conditional_caster(enough_power, fireball)
    print(casted_fireball("creature5", 30))
    print(casted_fireball("creature6", 5))
    casted_heal = conditional_caster(enough_power, heal)
    print(casted_heal("creature5", 30))
    print(casted_heal("creature6", 5))
    spell_list = [fireball, fireball, heal, combo1]
    sequence = spell_sequence(spell_list)
    print(sequence("creature1", 10))
