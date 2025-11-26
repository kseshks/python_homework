#калькулятор валюты https://cbr.ru/currency_base/daily
#программа должна запрашивать сумму в usd, получать курс сайта выводить сумму в рублях 
#import requests

#r = requests.get(url)
#r.text = ищем "доллар сша" и парсим следующую 
#дальше отрефакторми, выделив класс для веб запросов отдельно
#нажать тестирующий метод, подсовывающие "фальшие данные"

import requests
from typing import Optional

class CurrencyParser:    
    def __init__(self):
        self.base_url = "https://cbr.ru/currency_base/daily/"
    
    def get_usd_rate(self) -> Optional[float]:
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()

            lines = response.text.split('\n')
            for i, line in enumerate(lines):
                if 'доллар сша' in line.lower():
                    return self._parse_rate_from_line(lines[i+1])
            
            return None
        except Exception as e:
            return None
    
    def _parse_rate_from_line(self, line: str) -> Optional[float]:
        try:
            import re
            matches = re.findall(r'\d+,\d+', line)
            if matches:
                rate_str = matches[0].replace(',', '.')
                return float(rate_str)
            return None
        except Exception as e:
            return None


class CurrencyCalculator:
    def __init__(self, parser: CurrencyParser):
        self.parser = parser
    
    def convert_usd_to_rub(self, usd_amount: float) -> Optional[float]:
        usd_rate = self.parser.get_usd_rate()
        if usd_rate is None:
            return None
        
        rub_amount = usd_amount * usd_rate
        return rub_amount
    
    def display_conversion(self, usd_amount: float):
        rub_amount = self.convert_usd_to_rub(usd_amount)
        if rub_amount is not None:
            print(f"{usd_amount} USD = {rub_amount:.2f} RUB")
        else:
            print("ошибка")


class MockCurrencyParser:
    def get_usd_rate(self) -> float:
        return 80.50  # курс для тестирования


def test_calculator():
    print('тестирование вычислений')
    mock_parser = MockCurrencyParser()
    test_calculator = CurrencyCalculator(mock_parser)
    
    test_amounts = [1, 10, 50, 1000]
    for amount in test_amounts:
        test_calculator.display_conversion(amount)


def main():
    test_calculator()

    parser = CurrencyParser()
    calculator = CurrencyCalculator(parser)
    
    try:
        usd_input = input("Введите сумму в USD: ")
        usd_amount = float(usd_input.replace(',', '.'))
        
        if usd_amount <= 0:
            print("Сумма должна быть положительной")
            return
        
        calculator.display_conversion(usd_amount)
        
    except ValueError:
        print("Ошибка")



if __name__ == "__main__":
    main()