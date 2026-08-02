def fio(initials: list[str]) -> str:
    result = initials[0][0] + initials[1][0] + initials[2][0]
    return result

def words_count(phrase: str) -> int:
    result = len(phrase.split(' '))
    return result

def encrypt(text: str) -> str:
    length = len(text)
    if length % 2 == 0:
        mid = length // 2
        part_1 = text[:mid]
        part_2 = text[mid:]
        result = part_2 + part_1
    else:
        part_1 = text[::2]
        part_2 = text[1::2]
        result = part_1 + part_2
    return result
