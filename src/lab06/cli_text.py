import argparse
import pathlib
import sys

from src.lab03.text_stats import normalize, tokenize, count_freq, top_n

def main():
    parser = argparse.ArgumentParser(
        description="CLI-утилиты лабораторной №6 для работы с текстом"
    )
    subparsers = parser.add_subparsers(dest="command", help="Доступные подкоманды")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов в тексте")
    stats_parser.add_argument("--input", required=True, help="Путь к txt файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Сколько слов вывести")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    in_path = pathlib.Path(args.input)
    if not in_path.exists():
        parser.error(f"Входной файл не найден: '{in_path.absolute()}'")
    if not in_path.is_file():
        parser.error(f"Указанный путь является директорией, а не файлом: '{in_path.absolute()}'")

    if args.command == "cat":
        try:
            with open(in_path, "r", encoding="utf-8") as f:
                for idx, line in enumerate(f, 1):
                    if args.n:
                        print(f"{idx:6}\t{line}", end="")
                    else:
                        print(line, end="")
            print()
        except UnicodeDecodeError:
            parser.error("Не удалось прочитать файл в кодировке UTF-8.")

    elif args.command == "stats":
        if args.top <= 0:
            parser.error("Параметр --top должен быть больше нуля.")
        
        try:
            raw_text = in_path.read_text(encoding="utf-8")
            normalized = normalize(raw_text)
            tokens = tokenize(normalized)
            freq_dict = count_freq(tokens)
            ranking = top_n(freq_dict, args.top)

            if not ranking:
                print("Текст не содержит слов для анализа.")
                return

            print(f"--- Топ-{args.top} самых частых слов ---")
            for rank, (word, count) in enumerate(ranking, 1):
                print(f"{rank}. {word}: {count}")
        except Exception as e:
            print(f"Ошибка при анализе текста: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
