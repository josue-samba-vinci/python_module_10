def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: '* ' + x + ' *', spells))


def mage_stats(mages: list[dict]) -> dict:
    minimum = min(mages, key=lambda x: x['power'])
    maximum = max(mages, key=lambda x: x['power'])
    average = round(sum(map(lambda x: x['power'], mages))/len(mages), 2)
    return {'max_power': maximum, 'min_power': minimum, 'avg_power': average}


if __name__ == "__main__":
    artifact1 = {'name': "a", 'power': 95, 'type': "Earth"}
    artifact2 = {'name': "b", 'power': 75, 'type': "Air"}
    artifact3 = {'name': "c", 'power': 85, 'type': "Fire"}
    artifact4 = {'name': "d", 'power': 100, 'type': "Water"}
    artifacts = [artifact1, artifact2, artifact3, artifact4]
    print("Testing artifact sorter...")
    print(artifact_sorter(artifacts))
    mage1 = {'name': "a", 'power': 95, 'element': "Earth"}
    mage2 = {'name': "b", 'power': 75, 'element': "Air"}
    mage3 = {'name': "c", 'power': 85, 'element': "Fire"}
    mage4 = {'name': "d", 'power': 100, 'element': "Water"}
    mages = [mage1, mage2, mage3, mage4]
    print("Testing power filter...")
    print(power_filter(mages, 85))
    spells = ["spell1", "spell2", "spell3", "spell4"]
    print("Testing spell transformer...")
    print(spell_transformer(spells))
    print("Testing mage stats...")
    print(mage_stats(mages))
