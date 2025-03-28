import pytest
from compare_files import (read_lines_from_file, compare_sets,
                           write_lines_to_file)


@pytest.fixture
def temp_file(tmp_path):
    """
    Фікстура, що створює тимчасовий файл і повертає шлях до нього.
    """

    def _create_temp_file(filename, content):
        file_path = tmp_path / filename
        file_path.write_text(content, encoding="utf-8")
        return file_path

    return _create_temp_file


@pytest.mark.parametrize(
    "content_a, content_b, expected_same, expected_diff",
    [
        (
            "apple\nbanana\norange",
            "banana\npear\napple",
            {"apple", "banana"},
            {"orange", "pear"},
        ),
        ("cat\ndog\nmouse", "dog\nlion\nmouse", {"dog", "mouse"},
         {"cat", "lion"}),
        ("", "test\nexample", set(), {"test", "example"}),
    ],
)
def test_compare_sets(content_a, content_b, expected_same, expected_diff,
                      temp_file):
    file_a = temp_file("file_a.txt", content_a)
    file_b = temp_file("file_b.txt", content_b)

    set_a = read_lines_from_file(str(file_a))
    set_b = read_lines_from_file(str(file_b))

    same, diff = compare_sets(set_a, set_b)

    assert same == expected_same
    assert diff == expected_diff


def test_write_lines_to_file(temp_file):
    lines = {"apple", "banana", "cherry"}
    out_file = temp_file("output.txt", "")  # поки пустий

    write_lines_to_file(str(out_file), lines)
    # перевіримо, що вийшло
    result_lines = out_file.read_text(encoding="utf-8").splitlines()
    # оскільки при записі ми робимо sorted(lines),
    # очікуємо ["apple", "banana", "cherry"]
    assert result_lines == sorted(lines)
