def caching_fibonacci():    # Створюємо функцію, яка повертає внутрішню функцію fibonacci(n)
    cache = {}              # Створюємо порожній словник


    def fibonacci(n):   # Створюємо функцію, яка буде обчислювати числа з ряду Фібоначчі
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)    # Обчислення числа з ряду Фібоначчі
            return cache[n]       # Повернення числа

    return fibonacci      




fib = caching_fibonacci()
print(fib(10)) 
print(fib(15))  


