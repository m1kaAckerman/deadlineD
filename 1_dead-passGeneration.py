import random
import string
import logging

logging.basicConfig(filename='password_generator.log', level=logging.INFO)

def generate_password(length):
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    logging.info(f"генерация нового пароля: {password}")
    return password

def main():
    try:
        password_length = int(input("введите длину пароля: "))
        password = generate_password(password_length)
        print("сгенерированный пароль:", password)
    except ValueError:
        logging.error("неправильное значение длины пароля.")
        print("ошибка: введено некорректное значение длины пароля.")

if __name__ == "__main__":
    main()

"полезная информация"

"я импортировал модули рендом стрин и логин, создал базовый конфиг логирования с указанием имени файла и уровнем логирования"

"определил функцию женирейт пасворд, которая генерирует пароль заданой длинны и записывает инфу в созданном лог файле"

"пароли и ошибки будут записываться в лдог файл, так же можно изменить имя файла и уровень логирования"

