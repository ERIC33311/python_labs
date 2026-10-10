"""
Скрипт для анализа частоты слов в тексте.

Читает текст из стандартного потока ввода (stdin), обрабатывает его
с помощью библиотечных функций (очистка, токенизация) и выводит
статистику по топ-5 самым частым словам в виде текста или таблицы.
"""

import sys
from src.lib.text import normalize, tokenize, count_freq, top_n

# True — выводить таблицу, False — обычные строки
USE_TABLE_MODE: bool = True


def main():
    """
    Основная функция управления конвейером обработки текста.
    
    1. Переконфигурирует stdin на UTF-8 для корректной работы с кириллицей.
    2. Считывает входные данные до символа конца файла (EOF).
    3. Очищает текст, разбивает на токены, подсчитывает частоту слов.
    4. Выводит метрики (всего/уникальных слов) и топ-5 слов в выбранном режиме.
    """
    sys.stdin.reconfigure(encoding='utf-8')
    
    raw_text = sys.stdin.read()
    
    normalized = normalize(raw_text)
    tokens = tokenize(normalized)
    freq_dict = count_freq(tokens)
    top_5_words = top_n(freq_dict, n=5)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq_dict)}")
    print("Топ-5:")

    if not USE_TABLE_MODE:
        for word, count in top_5_words:
            print(f"{word}:{count}")
    else:
        max_word_len = max([len(word) for word, _ in top_5_words], default=5)
        
        print(f"{'слово':<{max_word_len}} | частота")
        print("-" * (max_word_len + 10))  # Рисуем идеальную разделительную линию
        
        for word, count in top_5_words:
            print(f"{word:<{max_word_len}} | {count}")


if __name__ == "__main__":
    main()
