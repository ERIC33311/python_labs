def format_record(inicial):
    inicials = list(inicial)
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