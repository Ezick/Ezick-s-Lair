tickets = int(input("Введите количество билетов: "))
SUM = 0
for i in range(tickets):
    age = int(input(f'Введите возраст посетителя {i+1}: '))
    if age < 18:
        cost = 0
    elif 18 <= age < 25:
        cost = 990
    elif age >= 25:
        cost = 1390
    SUM += cost

if tickets > 3:
    SUM = SUM * 0.9

print(f'Итоговая стоимость билетов к оплате: {int(SUM)} руб.')