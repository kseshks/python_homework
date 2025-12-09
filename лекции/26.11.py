'''#используется вместо итератора 

def fn():
    yield 1
    yield 2
    yield 3
    
for i in fn():
    print(i)
    
def fn2():
    for i in [1, 2, 3]:
        yield i
    a = yield
    
#регулярные выражения - способ поиска подстроки в строке'''

'''
abcde
"[bde]c"  - bc, dc, ec

import re
if re.match("[bde]c"):

. - любой символ
".c"

"^a" - в начале строки а
"e$" - e в конце
"a[5]" - a пять раз подряд 
"a+" - a 1 и больше раз 
"a*" - любое количество а (0 или больше)

пример:

строка hello, world
^.+,?   *.+$

^ = начало строки
.+ = hello
,? = запятая
 * = сколько то пробелов
.+ = world
$ = конец строки 

m = re.match(".x..", s)
if m:
    m[1] = hello 
    m[2] = world

задание!
написать генераторную функцию которая матчит регулярные выражения
есть лог файл - 1.txt такого вида
[2025-11-12 14:30:01] INFO User "alice" logged in from 192.168.0.4
[2025-11-12 14:30:12] WARNING Suspicious activity detected for "eve"
..


парсим все 
проверям регулярным выражением 
нужно возрващать обьект yield
распарсить текст, вытащить имя полльзователя и проблему
'date' 'level' 'text'
второе name И error
yield {
    date ='..'
    level = '..'
    text = '..'
}

'''

'''lines = open('1.txt').readlines()

import re
expr = "\[([0-9]{4}-[0-9]{2}-[0-9]{2}) 14:30:01\] INFO (.*)"
m = re.match(expr, lines[0])
print(m)
print(m[1])'''

import re

def parse_log(filename):
    reg = r'\[(.*?)\] (INFO|WARNING|ERROR) (.*)'

    with open(filename) as file:
        for line in file:
            line = line.strip()
            match = re.match(reg, line)
            if match:
                yield {
                    'date': match[1].split()[0],
                    'level': match[2],
                    'text': match[3]
                }

def parse_log_with_user(filename):
    reg = r'\[(.*?)\] (INFO|WARNING|ERROR) (.*)'

    with open(filename) as file:
        for line in file:
            line = line.strip()
            match = re.match(reg, line)
            if match:
                user_match = re.search(r'"([^"]+)"', match[3])
                user_name = user_match[1] if user_match else None

                yield {
                    'date': match[1].split()[0],
                    'level': match[2],
                    'text': match[3],
                    'user_name': user_name,
                }

print("Первая функция:")
for text in parse_log('1.txt'):
    print(f"date: {text['date']}")
    print(f"level: {text['level']}")
    print(f"text: {text['text']}")
    print()

print("Вторая функция:")
for text in parse_log_with_user('1.txt'):
    print(f"name: {text['user_name']}")
    print(f"error: {text['text']}")
    print()