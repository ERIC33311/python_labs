def format_record(rec: tuple[str, str, float]) -> str:
    """
    Форматирует запись студента (ФИО, группа, GPA) в строку вида
    "Иванов И.И., гр. BIVT-25, GPA 4.60".

    ФИО и группа не могут быть пустыми, GPA должен быть в диапазоне [0.0, 5.0] -> ValueError.
    """
    if not isinstance(rec, tuple):
        raise TypeError("rec должен быть кортежем")
    
    if len(rec) != 3:
        raise ValueError("rec должен содержать ровно 3 элемента")

    if not isinstance(rec[0], str) or not isinstance(rec[1], str):
        raise TypeError("ФИО и группа должны быть строками")
    
    if not isinstance(rec[2], (float)):
        raise TypeError("GPA должен быть числом")
    
    inicials = list(rec)
    gpa = inicials[2]
    fio1 = inicials[0].split()
    class_stud = inicials[1].strip()
    
    if not (0.0 <= gpa <= 5.0):
        raise ValueError("GPA должен быть от 0.0 до 5.0")
        
    if not fio1 or not class_stud:
        raise ValueError("ФИО и группа не могут быть пустыми")
        
    if len(fio1) == 3:
        fio = f'{fio1[0].capitalize()} {fio1[1][0].upper()}.{fio1[2][0].upper()}.'
    else:
        fio = f'{fio1[0].capitalize()} {fio1[1][0].upper()}.'
        
    return f'{fio}, гр. {class_stud}, GPA {gpa:.2f}'

# Тест-кейсы
try:
    print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
except ValueError:
    print("format_record -> ValueError")

try:
    print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
except ValueError:
    print("format_record -> ValueError")

try:
    print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
except ValueError:
    print("format_record -> ValueError")

try:
    print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
except ValueError:
    print("format_record -> ValueError")

try:
    print(format_record(("", "IKBO-12", 5.0)))
except ValueError:
    print("format_record с пустым ФИО -> ValueError")

try:
    print(format_record(("Иванов Иван", "   ", 4.5)))
except ValueError:
    print("format_record с пустой группой -> ValueError")

try:
    print(format_record(("Иванов Иван", "BIVT-25", 6.0)))
except ValueError: 
    print("format_record с GPA вне диапазона -> ValueError")

try:
    print(format_record(("Иванов Иван", "BIVT-25", 6.0, 'Лишний')))
except ValueError: 
    print("format_record с 4 элементами -> ValueError")

try:
    print(format_record(["Иванов Иван", "BIVT-25", 6.0]))
except TypeError: 
    print("format_record, вместо кортежа — список -> TypeError")