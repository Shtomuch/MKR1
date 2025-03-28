def read_lines_from_file(filepath: str) -> set:
    """
    Зчитує лінії з файлу і повертає множину рядків (без переносів).
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
    return set(lines)


def compare_sets(set_a: set, set_b: set) -> (set, set):
    """
    Порівнює дві множини та повертає:
    1) Множину спільних елементів
    2) Множину унікальних елементів (лише в одній із множин)
    """
    same = set_a.intersection(set_b)
    diff = set_a.symmetric_difference(set_b)
    return same, diff
