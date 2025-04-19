import re
from decimal import Decimal
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[Decimal, None, None]:   # Генератор, який знаходить дійсні числа відокремлені пробілами
    
    pattern = r'\s(\d+\.\d+)\s'    # Регулярний вираз, знаходить числа згідно шаблону
    
    matches = re.findall(pattern, text)   # Повертає список рядків згідно шаблону



    for number in matches:
        yield Decimal(number)  # Знайдені числа повертаємо по черзі




def sum_profit(text: str, func: Callable[[str], Generator[Decimal, None, None]]) -> Decimal:   # Функція, яка обчислює загальну суму чисел, використовуючи генератор чисел.


    return sum(func(text), start=Decimal('0'))



text = "Дохід працівника: 1000.01 зарплата, 27.45 бонус, 324.00 премія."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

