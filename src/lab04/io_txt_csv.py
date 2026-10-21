"""Ввод/вывод для ЛР4: чтение текста и запись CSV.

Обеспечивает строгое выполнение требований ТЗ ЛР4, включая автоматическое
создание родительских папок и валидацию структуры таблиц.
"""

import csv
from pathlib import Path


def ensure_parent_dir(path: str | Path) -> None:
    """Создаёт родительские директории для path, если их нет."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Читает файл целиком и возвращает содержимое одной строкой.

    Чтобы выбрать другую кодировку, передайте её явно, например: encoding="cp1251".
    """
    return Path(path).read_text(encoding=encoding)


def write_csv(rows: list, path: str | Path, header: tuple | None = None) -> None:
    """Создаёт или перезаписывает CSV-файл (разделитель запятая, UTF-8).

    Raises:
        ValueError: если строки (или заголовок) имеют разную длину.
    """
    p = Path(path)
    ensure_parent_dir(p)

    data_rows = [list(r) for r in rows]

    if data_rows:
        first_row_len = len(data_rows[0])
        for idx, r in enumerate(data_rows):
            if len(r) != first_row_len:
                raise ValueError(
                    f"Ошибка валидации CSV: строка на индексе {idx} "
                    f"имеет длину {len(r)}, ожидалось {first_row_len}."
                )

    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        for r in data_rows:
            writer.writerow(r)


# === БЛОК АВТОМАТИЧЕСКОГО ТЕСТИРОВАНИЯ ПО ТЗ ===
if __name__ == "__main__":
    import shutil

    print("Запуск контрольных мини-тестов...")

    # Создаем изолированную директорию для временных тестов
    test_dir = Path("data/lab04_tests")
    if test_dir.exists():
        shutil.rmtree(test_dir)

    # 1. Проверка функции read_text
    test_file = test_dir / "input.txt"
    ensure_parent_dir(test_file)
    test_file.write_text("Привет, мир!", encoding="utf-8")
    assert read_text(test_file) == "Привет, мир!"

    # 2. Проверка краевых случаев write_csv (Пустые списки и заголовки)
    empty_file = test_dir / "empty.csv"
    only_header_file = test_dir / "only_header.csv"

    # rows пустой, header=None -> абсолютно пустой файл (0 строк)
    write_csv([], empty_file, header=None)
    assert empty_file.read_text(encoding="utf-8") == ""

    # rows пустой, header=("word", "count") -> только заголовок
    write_csv([], only_header_file, header=("word", "count"))
    assert only_header_file.read_text(encoding="utf-8").strip() == "word,count"

    # 3. Проверка валидной матрицы (ширина != высота)
    normal_csv = test_dir / "normal.csv"
    valid_data = [("привет", 2), ("мир", 1), ("тест", 5)]
    write_csv(valid_data, normal_csv, header=("word", "count"))
    assert normal_csv.exists()

    # 4. Проверка ловушки ValueError (разная длина строк данных)
    invalid_data = [("привет", 2), ("мир", 1, "лишний_элемент")]
    try:
        write_csv(invalid_data, test_dir / "should_fail.csv")
        assert False, "Ошибка: код пропустил строки разной длины!"
    except ValueError:
        pass  # Ошибка успешно поймана, тест пройден!

    print("Все тесты пройдены УСПЕШНО! Ошибок нет.")
