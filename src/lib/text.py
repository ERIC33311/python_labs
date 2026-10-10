import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    r"""
    Нормализует текст: приводит к нижнему регистру, заменяет 'ё' и убирает лишние пробелы.

    Args:
        text (str): Исходный сырой текст для обработки.
        casefold (bool, optional): Если True, использует метод casefold() для Юникода. 
            Если False, использует стандартный lower(). По умолчанию True.
        yo2e (bool, optional): Если True, заменяет все буквы 'ё'/'Ё' на 'е'/'Е'. 
            По умолчанию True.

    Returns:
        str: Очищенная строка, где все управляющие символы (\t, \n, \r) заменены на пробелы, 
        а повторяющиеся пробелы схлопнуты в один.
    """
    if yo2e and casefold:
        text = text.casefold().replace('ё', 'е')
    elif yo2e and not casefold:
        text = text.lower().replace('ё', 'е')
    elif not yo2e and casefold:
        text = text.casefold()
    else:
        text = text.lower()
    return ' '.join(text.split())


def tokenize(text: str) -> list[str]:
    """
    Разбивает текст на отдельные слова (токены) по небуквенно-цифровым разделителям.

    Словами считаются последовательности букв, цифр и знаков подчеркивания (_), 
    а также слова со встроенным дефисом (например, 'по-настоящему'). 
    Отдельные числа (например, '2025') также признаются словами. Знаки препинания и эмодзи игнорируются.

    Args:
        text (str): Нормализованный текст.

    Returns:
        list[str]: Список выделенных слов.
    """
    return re.findall(r"\w+(?:-\w+)*", text)


def count_freq(tokens: list[str]) -> dict[str, int]: 
    """
    Подсчитывает частоту встречаемости каждого слова в списке.

    Args:
        tokens (list[str]): Список слов (токенов).

    Returns:
        dict[str, int]: Словарь, где ключи — это уникальные слова, 
        а значения — количество их упоминаний в тексте.
    """
    freq = {}
    for i in tokens: freq[i] = freq.get(i, 0) + 1 
    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """
    Возвращает N самых часто встречающихся слов.

    Сортировка выполняется по убыванию частоты. Если у нескольких слов частота одинаковая 
    (ситуация тай-брейка), они сортируются строго по алфавиту.

    Args:
        freq (dict[str, int]): Словарь частот слов.
        n (int, optional): Количество слов для вывода в топе. По умолчанию 5.

    Returns:
        list[tuple[str, int]]: Список кортежей формата (слово, частота) длиной не более N.
    """
    sorted_items = sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
    return sorted_items[:n]  


# === БЛОК АВТОМАТИЧЕСКОГО ТЕСТИРОВАНИЯ ПО ТЗ ===
if __name__ == "__main__":
    print("Запуск контрольных мини-тестов...")
    
    # 1. Тесты функции normalize
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("ёжик, Ёлка") == "ежик, елка"
    assert normalize("Hello\r\nWorld") == "hello world"
    assert normalize("  двойные   пробелы  ") == "двойные пробелы"

    # 2. Тесты функции tokenize
    assert tokenize("привет мир") == ["привет", "мир"]
    assert tokenize("hello,world!!!") == ["hello", "world"]
    assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
    assert tokenize("2025 год") == ["2025", "год"]
    assert tokenize("emoji 😀 не слово") == ["emoji", "не", "слово"]

    # 3. Тесты функций count_freq + top_n
    freq = count_freq(["a", "b", "a", "c", "b", "a"])
    assert freq == {"a": 3, "b": 2, "c": 1}
    assert top_n(freq, 2) == [("a", 3), ("b", 2)]

    # 4. Тест тай-брейка по слову при равной частоте
    freq2 = count_freq(["bb", "aa", "bb", "aa", "cc"])
    assert freq2 == {"aa": 2, "bb": 2, "cc": 1}
    assert top_n(freq2, 2) == [("aa", 2), ("bb", 2)]

    print("Все тесты пройдены УСПЕШНО! Ошибок нет.")
