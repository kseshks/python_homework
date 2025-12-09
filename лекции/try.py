import datetime

def log(level, date, text):
    print(level,date,text)

def log2(level):
    return lambda date: lambda text: log(level, date, text)

log_text = log2("WARN")(datetime.datetime.now())
log_text('hello')