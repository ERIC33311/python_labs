import csv
import sys
from pathlib import Path
from openpyxl import Workbook


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """Конвертирует CSV в XLSX.

    Первая строка CSV — заголовок. Лист называется "Sheet1". Колонки —
    автоширина по длине текста (не менее 8 символов).
    """
    c_path = Path(csv_path)
    x_path = Path(xlsx_path)

    if not c_path.exists():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")

    with open(c_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    if not rows:
        raise ValueError("CSV без заголовка или пустой")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for row in rows:
        ws.append(row)

    for col in ws.columns:
        max_len = 0
        col_letter = col[0].column_letter  
        for cell in col:
            if cell.value is not None:
                max_len = max(max_len, len(str(cell.value)))
        ws.column_dimensions[col_letter].width = max(max_len + 3, 8)



if __name__ == "__main__":
    print("Запуск сценария конвертации CSV -> XLSX...")
    try:
        csv_to_xlsx("data/samples/people.csv", "data/out/people.xlsx")
        print("Успешно: people.csv -> people.xlsx")

        csv_to_xlsx("data/samples/cities.csv", "data/out/cities.xlsx")
        print("Успешно: cities.csv -> cities.xlsx")
    except Exception as error:
        print(f"Ошибка выполнения сценария XLSX: {error}", file=sys.stderr)
        sys.exit(1)
