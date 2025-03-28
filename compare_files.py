def read_lines_from_file(filepath: str) -> set:
    """
    Зчитує лінії з файлу і повертає множину рядків (без переносів).
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
    return set(lines)