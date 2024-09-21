#техника 'обратный захват скорпиона' proposed by Chat GPT

#классов много, моделей тоже
#но возможных значений мощности всего 1 000
#можно пробежаться по массиву всех возможных мощностей
#для каждой определить оптимальную цену

#но как это сделать?

#техника обратного захвата:
#создаём массив, где индекс - мощность, а значение - цена
#для начала цены ставим макс + 1 (или Inf, но не во всех языках есть Inf)
#для доступных моделей заполняем массив фактическими ценами

#затем, начиная с предпоследнего элемента массива,
#для каждой пары цен i и i+1
#смотрим min, это и есть оптимальная цена для мощности i


n = int(input())
rooms_list = list(map(int, input().split()))
m = int(input())

cond_list = list()
for _ in range(m):
    power, price = map(int, input().split())
    cond_list.append((power, price))

power_price_list = [1001 + 1]*1001

#0 игнорим для простоты
for power, price in cond_list:
    power_price_list[power] = min(price, power_price_list[power])

for i in range(999, 0 ,-1):
    power_price_list[i] = min(power_price_list[i], power_price_list[i+1])

result = 0
for req_power in rooms_list:
    result = result + power_price_list[req_power]

print(result)