str= '1, 3, 5, 7, 9'
str = str.replace(' ', '')
num = ''
sp = []
for i in str:
    if i != ',':
        num += i
    else:
        sp.append(int(num))
        num = ''
# Добавляем последнее число
if num:
    sp.append(int(num))

sr = sp
sp = sorted(sp)

print('min', min(sp))
print('max', max(sp))

# Подсчет количества повторений каждого числа
from collections import Counter
counter = Counter(sp)

# Вывод результатов
for number, count in sorted(counter.items()):
    print(f"Число {number}: {count} повторений")
    
print('Объем выборки:', len(sp))

sum_val = 0
for i in sp:
    sum_val += i
sred = sum_val / len(sp)

print('sred', sred)

disper = 1
sum_kv = 0
for i in sp:
    sum_kv += i**2
disper = sum_kv/ len(sp) - sred**2
sco = disper**0.5
print('disper', disper)
print('sco', sco)