"""Перевести дату в текстовое представление
      0123456789 11     18
Вход: 2025-09-17 13:21:53
Выход: семьнадцатое сентября две тысячи двадцать пятого года тринадцать часов двадцать одна минут пятьдесят три секунды"""

# Воронина Ксения

date = "2025-09-17 13:21:53"
#date = input("Введите дату в формате ГГГГ-ММ-ДД ЧЧ:ММ:СС: ")

thousand = [' ', 'тысяча', 'две тысячи', 'три тысячи', 'четыре тысячи', 'пять тысяч', 'шесть тысяч', 'семь тысяч', 'восемь тысяч', 'девять тысяч']
hundred =  [' ', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
ten = [' ', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
ten_year = [' ', 'десятого', 'двадцатого', 'тридцатого', 'сорокового', 'пятидесятого', 'шестидесятого', 'семидесятого', 'восьмидесятого', 'девяностого']
ten1 = [' ', 'одиннадцатого', 'двенадцатого', 'тринадцатого', 'четырнадцатого', 'пятнадцатого', 'шестнадцатого', 'семнадцатого', 'восемнадцатого', 'девятнадцатого']
ten1_day = [' ', 'одиннадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое', 'семнадцатое', 'восемнадцатое', 'девятнадцатое']
ten2 = [' ', ' ', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
units = [' ', 'первого', 'второго', 'третьего', 'четвертого', 'пятого', 'шестого', 'седьмого', 'восьмого', 'девятого']
units_day = [' ', 'первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое']
units_hour = [' ', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
units_min_sec = [' ', 'одна', 'две', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']

months = [
    'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']

def number_to_word(number, word_list): 
    if 0 <= number < len(word_list):
        return word_list[number]
    return ""

# День
day_num = int(date[8:10])
if 10 < day_num < 20:
    day_word = number_to_word(day_num % 10, ten1_day)
else:
    tens_day = number_to_word(int(date[8]), ten2)
    units_day_word = number_to_word(int(date[9]), units_day)
    day_word = f"{tens_day} {units_day_word}".strip()

# Месяц
month_num = int(date[5:7])
month_word = months[month_num - 1] if 1 <= month_num <= 12 else ""

# Год
year_thousand = number_to_word(int(date[0]), thousand)
year_hundred = number_to_word(int(date[1]), hundred)

year_last_two = int(date[2:4])
if year_last_two % 10 == 0:
    year_word = number_to_word(int(date[2]), ten_year)
elif 10 < year_last_two < 20:
    year_word = number_to_word(year_last_two % 10, ten1)
else:
    tens_year = number_to_word(int(date[2]), ten)
    units_year = number_to_word(int(date[3]), units)
    year_word = f"{tens_year} {units_year}".strip()

# Время
hour_num = int(date[11:13])
minute_num = int(date[14:16])
second_num = int(date[17:19])

# Часы
if 10 < hour_num < 20:
    hour_word = f"{number_to_word(hour_num % 10, ten1).replace('того', 'ть')}"
else:
    tens_hour = number_to_word(int(date[11]), ten)
    units_hour_word = number_to_word(int(date[12]), units_hour)
    hour_word = f"{tens_hour} {units_hour_word}".strip()

# Минуты
if 10 < minute_num < 20:
    minute_word = f"{number_to_word(minute_num % 10, ten1).replace('того', 'ть')}"
else:
    tens_minute = number_to_word(int(date[14]), ten)
    units_minute_word = number_to_word(int(date[15]), units_min_sec)
    minute_word = f"{tens_minute} {units_minute_word}".strip()

# Секунды
if 10 < second_num < 20:
    second_word = f"{number_to_word(second_num % 10, ten1).replace('того', 'ть')}"
else:
    tens_second = number_to_word(int(date[17]), ten)
    units_second_word = number_to_word(int(date[18]), units_min_sec)
    second_word = f"{tens_second} {units_second_word}".strip()

# Склонения
hour_form = "часов" if 5 <= hour_num <= 20 or hour_num % 10 in [0, 5, 6, 7, 8, 9] else "час" if hour_num % 10 == 1 else "часа"

minute_form = "минут"
if minute_num % 10 == 1 and minute_num != 11:
    minute_form = "минута"
elif minute_num % 10 in [2, 3, 4] and not (12 <= minute_num <= 14):
    minute_form = "минуты"

second_form = "секунд"
if second_num % 10 == 1 and second_num != 11:
    second_form = "секунда"
elif second_num % 10 in [2, 3, 4] and not (12 <= second_num <= 14):
    second_form = "секунды"


date_part = f"{day_word} {month_word} {year_thousand} {year_hundred} {year_word} года".replace("  ", " ").strip()
time_part = f"{hour_word} {hour_form} {minute_word} {minute_form} {second_word} {second_form}".replace("  ", " ").strip()

print(f"{date_part} {time_part}")