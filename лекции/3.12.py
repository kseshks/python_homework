def log(level, date, text):
    print(f"[{level}] {date}: {text}")


def get_logger_for(level):
    return lambda date, text: log(level, date, text)


# Пример частичного применения
import datetime

logger_warn = get_logger_for("WARN")
logger_warn(datetime.date.today(), "hello")


# Каррирование
def log_curried(level):
    return lambda date: lambda text: log(level, date, text)


log_curried("WARN")(datetime.date.today())
log_curried('hello')

class Maybe:
    def __init__(self, value):
        self.value = value

    def bind(self, func):
        if self.value is None:
            return Maybe(None)
        return Maybe(func(self.value))
    
def div(val):
    if val == 0:
        return None
    return 1 / val

def print_val(val):
    print(val)
    return val

Maybe(5).bind(div).bind(print_val)

def log(level, date, text):
    print(f"[{level}] {date}: {text}")


def get_logger_for(level):
    return lambda date, text: log(level, date, text)

# этот код должен заработать:
#either - возвращает либо знаение, если вычисления прошли успешно, либо монаду с признаком ошибки


class Either:
    def __init__(self, value=None, error=None):
        self.value = value
        self.error = error 

    def bind(self, func):
        if self.error:
            return self
        try:
            result = func(self.value)
            return Either(result, None)

        except Exception as e:
            return Either(None, str(e))

def parse_int(x):
    if isinstance(x, int):
        return x

    if not x.isdigit():
        raise ValueError("error! not integer")

    return int(x)

def div(x):
    if x == 0:
        raise ZeroDivisionError("error! division by zero")
    return 1 / x

print(Either('10').bind(parse_int).bind(div).value) # 0.1
print(Either('10').bind(parse_int).bind(div).error) # none
print(Either('hello').bind(parse_int).bind(div).error) #  not integer
print(Either('0').bind(parse_int).bind(div).error) # division by zero 


#каррирование
import datetime

def log(level, date, text):
    print(level,date,text)

def log2(level):
    return lambda date: lambda text: log(level, date, text)

log_text = log2("WARN")(datetime.datetime.now())
log_text('hello')

