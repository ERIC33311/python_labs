import argparse
import pathlib
import sys


def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd", help="Доступные подкоманды")

    def add_io_args(sub_parser):
        sub_parser.add_argument("--in", dest="input", required=True, help="Путь к исходному файлу")
        sub_parser.add_argument("--out", dest="output", required=True, help="Путь для сохранения результата")

    p1 = sub.add_parser("json2csv", help="Конвертация JSON в CSV")
    add_io_args(p1)

    p2 = sub.add_parser("csv2json", help="Конвертация CSV в JSON")
    add_io_args(p2)

    p3 = sub.add_parser("csv2xlsx", help="Конвертация CSV в XLSX")
    add_io_args(p3)

    args = parser.parse_args()

    if not args.cmd:
        parser.print_help()
        sys.exit(0)

    in_path = pathlib.Path(args.input)
    out_path = pathlib.Path(args.output)

    if not in_path.exists():
        parser.error(f"Входной файл не найден: '{in_path.absolute()}'")

    out_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        if args.cmd == "json2csv":
            from src.lab05.json_csv import json_to_csv
            json_to_csv(str(in_path), str(out_path))
            
        elif args.cmd == "csv2json":
            from src.lab05.json_csv import csv_to_json
            csv_to_json(str(in_path), str(out_path))
            
        elif args.cmd == "csv2xlsx":
            from src.lab05.csv_xlsx import csv_to_xlsx  
            csv_to_xlsx(str(in_path), str(out_path))
            
        print(f"Конвертация успешно выполнена ({args.cmd}).")
    except Exception as e:
        print(f"Что-то пошло не так при работе конвертера: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
