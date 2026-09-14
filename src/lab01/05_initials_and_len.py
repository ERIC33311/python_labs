raw = input("ФИО: ")
words = raw.split()

initials = "".join(i[0].upper() for i in words)
without_space = " ".join(words)

print(f"Инициалы: {initials}.")
print(f"Длина (символов): {len(without_space)}")