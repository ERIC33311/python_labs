"""Скрипт автоматического сбора текстовой статистики и генерации CSV-отчетов.

Работает строго на базовых системных потоках и модуле sys (без argparse).
Использует переиспользуемые функции обработки текста из библиотеки src.lib.text.
"""

from pathlib import Path
import sys

from src.lab04.io_txt_csv import read_text, write_csv
from src.lib.text import count_freq, normalize, tokenize, top_n


def main() -> None:
    """Главная точка входа в скрипт отчета."""
    in_path = Path("data/lab04/input.txt")
    out_path = Path("data/lab04/report.csv")
    encoding = "utf-8"

    try:
        content = read_text(in_path, encoding=encoding)

        tokens = tokenize(normalize(content))
        total_freqs = count_freq(tokens)

    except FileNotFoundError:
        print(f"ошибка: файл не найден: {in_path.name}", file=sys.stderr)
        sys.exit(1)
    except UnicodeDecodeError:
        print(
            f"ошибка: кодировка не подходит для файла: {in_path.name}",
            file=sys.stderr,
        )
        sys.exit(1)

    total_words_count = len(tokens)
    unique_words_count = len(total_freqs)

    # Получаем Топ-5 через твою библиотечную функцию top_n
    top_5_pairs = top_n(total_freqs, n=5)

    print(f"Всего слов: {total_words_count}")
    print(f"Уникальных слов: {unique_words_count}")
    print("Топ-5:")
    for word, count in top_5_pairs:
        print(f"  {word}:{count}")

    sorted_rows = top_n(total_freqs, n=len(total_freqs))
    write_csv(sorted_rows, out_path, header=("word", "count"))


if __name__ == "__main__":
    main()
