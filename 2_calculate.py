import logging

logging.basicConfig(filename='calculator.log', level=logging.INFO)

def add(x, y):
    result = x + y
    logging.info(f"сложение: {x} + {y} = {result}")
    return result

def subtract(x, y):
    result = x - y
    logging.info(f"вычитание: {x} - {y} = {result}")
    return result

def multiply(x, y):
    result = x * y
    logging.info(f"умножение: {x} * {y} = {result}")
    return result

def divide(x, y):
    try:
        result = x / y
        logging.info(f"деление: {x} / {y} = {result}")
        return result
    except ZeroDivisionError:
        logging.error("попытка деления на ноль")
        print("ошибка: ропытка деления на ноль")
        return None

def main():
    try:
        x = float(input("введите первое число: "))
        operator = input("введите оператор (+, -, *, /): ")
        y = float(input("введите второе число: "))

        if operator == '+':
            result = add(x, y)
        elif operator == '-':
            result = subtract(x, y)
        elif operator == '*':
            result = multiply(x, y)
        elif operator == '/':
            result = divide(x, y)
        else:
            logging.error(f"неизвестный оператор: {operator}")
            print("ошибка: неизвестный оператор")
            return

        if result is not None:
            print("результат:", result)

    except ValueError:
        logging.error("введено некорректное число")
        print("ошибка: введено некорректное число")

if __name__ == "__main__":
    main()

    "классические функции умножение, сложение, деление, вычитание, так же все операции записываются в лог файл calculator"

    "настроил базовую конфигурацию логирования с указанием имени файла и уровнем логирования"

    