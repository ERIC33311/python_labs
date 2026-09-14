m = int(input('Минуты: '))
hour = m // 60
mins = m - hour * 60
print(f'{hour}:{mins:02d}')