per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму вклада: '))

tkb = money * per_cent['ТКБ'] / 100  # Годовая прибыль по процентам в ТКБ
skb = money * per_cent['СКБ'] / 100  # Годовая прибыль по процентам в СКБ
vtb = money * per_cent['ВТБ'] / 100  # Годовая прибыль по процентам в ВТБ
sber = money * per_cent['СБЕР'] / 100  # Годовая прибыль по процентам в СБЕР

deposit = [tkb, skb, vtb, sber]

print('Максимальная сумма, которую вы можете заработать за год —', max(deposit))