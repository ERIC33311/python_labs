import csv
import json
import sys
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """Преобразует JSON-файл в CSV.

    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля
    пустыми строками. Кодировка UTF-8. Порядок колонок — как в первом объекте.
    """
    j_path = Path(json_path)
    c_path = Path(csv_path)

    if not j_path.exists():
        raise FileNotFoundError(f"Файл не найден: {json_path}")

    try:
        with open(j_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"битый JSON: {e.msg}, строка {e.lineno}", file=sys.stderr)
        sys.exit(1)

    if not data or not isinstance(data, list):
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    fieldnames = []
    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Элементы списка JSON должны быть словарями")
        for key in item.keys():
            if key not in fieldnames:
                fieldnames.append(key)

    if not fieldnames:
        raise ValueError("В объектах JSON отсутствуют ключи для заголовка")

    c_path.parent.mkdir(parents=True, exist_ok=True)

    with open(c_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    c_path = Path(csv_path)
    j_path = Path(json_path)

    if not c_path.exists():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")

    with open(c_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader) 
    if not rows or reader.fieldnames is None or not rows[0]:
        raise ValueError("CSV без заголовка или пустой")

    j_path.parent.mkdir(parents=True, exist_ok=True)

    with open(j_path, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2) 



if __name__ == "__main__":
    print("Запуск взаимных конвертаций JSON <-> CSV...")
    try:
        json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
        print("Успешно: JSON -> CSV выполнен")

        csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")
        print("Успешно: CSV -> JSON выполнен")
    except Exception as error:
        print(f"Ошибка выполнения демо-сценария: {error}", file=sys.stderr)
        sys.exit(1)
