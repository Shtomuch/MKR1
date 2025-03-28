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

def write_lines_to_file(filepath: str, lines: set) -> None:
    """
    Записує множину рядків у текстовий файл (по одному рядку на файл).
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        for line in sorted(lines):
            f.write(line + "\n")

def main(file1: str, file2: str) -> None:
    """
    Основна логіка:
     1) зчитати файли
     2) порівняти
     3) записати у same.txt і diff.txt
    """
    set1 = read_lines_from_file(file1)
    set2 = read_lines_from_file(file2)

    same_lines, diff_lines = compare_sets(set1, set2)

    write_lines_to_file('same.txt', same_lines)
    write_lines_to_file('diff.txt', diff_lines)


if __name__ == "__main__":

    import sys
    if len(sys.argv) != 3:
        print("Usage: python compare_files.py <file1.txt> <file2.txt>")
        sys.exit(1)

    file1_path = sys.argv[1]
    file2_path = sys.argv[2]
    main(file1_path, file2_path)