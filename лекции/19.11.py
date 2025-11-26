'''class ABC:
    def __getattr__(self, name):
        print(name)
        return 123
    
    def __setattr__(self, name, value):
        print(name, '=', value)
        
a = ABC()
print(a.hello)
a.abcde = 12345

class Log:
    def __init__(self, min_level):
        self.min_level = min_level
        
    def __call__(self, *args):
        print(args[0])
        return 456
    
log = Log(LogLevel.WARN)

def func(a, b, log):
    log('this is func')
    
class Ghi:
    def __getitem__(self, i):
        return 1 
    
    def __setitem__(self):
        return 2
    
a = Ghi()
print(a[5])'''
'''print("Все курсы:")
    all_rates = curr.get_all_rates()
    for currency, rate in list(all_rates.items())[:5]:
        print(f"{currency}: {rate}")'''


#страница с курсами валют "https://cbr.ru/currency_base/daily/". сохранить все валюты в словарь, использовать __getattr__
#curr = DailyRates()
#print(curr.USD)

import requests
from bs4 import BeautifulSoup
from datetime import datetime

class DailyRates:
    def __init__(self):
        self.url = "https://cbr.ru/currency_base/daily/"
        self.rates = {}
        self._load_rates()
    
    def _load_rates(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')

            table = soup.find('table', {'class': 'data'})
            
            if table:
                for row in table.find_all('tr')[1:]:
                    columns = row.find_all('td')
                    if len(columns) >= 5:
                        currency_code = columns[1].text.strip()
                        rate = float(columns[4].text.strip().replace(',', '.'))
                        self.rates[currency_code] = rate
            
            self.rates['RUB'] = 1.0
            
        except requests.RequestException as e:
            print(e)
        except Exception as e:
            print(e)
    
    def __getattr__(self, name):
        currency_code = name.upper()
        
        if currency_code in self.rates:
            return self.rates[currency_code]
        else:
            raise AttributeError(f"Курс для валюты '{currency_code}' не найден")
    
    def __dir__(self):
        return super().__dir__() + list(self.rates.keys())
    
    def get_all_rates(self):
        return self.rates.copy()
    

if __name__ == "__main__":
    curr = DailyRates()

    print(f"USD: {curr.USD}")
    print(f"EUR: {curr.EUR}")
    print(f"GBP: {curr.GBP}")
    print(f"CNY: {curr.CNY}")
    print(f"JPY: {curr.JPY}")

  
  
#2 курс доллара за месяц
# https://cbr.ru/currency_base/dynamics?UniDbQuery.Posted=True&UniDbQuery.so=1&UniDbQuery.mode=1&UniDbQuery.date_req1=&UniDbQuery.date_req2=&UniDbQuery.VAL_NM_RQ=R01235&UniDbQuery.From=19.10.2025&UniDbQuery.To=19.11.2025

print('')
import requests
from bs4 import BeautifulSoup

class Rates:
    def get_month(self):
        try:
            url = "https://cbr.ru/currency_base/dynamics?UniDbQuery.Posted=True&UniDbQuery.so=1&UniDbQuery.mode=1&UniDbQuery.date_req1=&UniDbQuery.date_req2=&UniDbQuery.VAL_NM_RQ=R01235&UniDbQuery.From=19.10.2025&UniDbQuery.To=19.11.2025"
            
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find('table', {'class': 'data'})
            
            print("Курс USD")
            
            if table:
                for row in table.find_all('tr')[1:]:
                    columns = row.find_all('td')
                    if len(columns) >= 3:
                        date = columns[0].text.strip()
                        rate = columns[2].text.strip()
                        print(date, rate)
                        
        except Exception as e:
            print(e)

r = Rates()
usd_rates = r.get_month()

        
