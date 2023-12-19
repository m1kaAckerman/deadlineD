"для запуска программы через командную строку, можно использовать аргпарс"


import argparse

parser = argparse.ArgumentParser(description='генератор случайных паролей')
parser.add_argument('length', type=int, help='длинна пароля')

args = parser.parse_args()

password_length = args.length
password = generate_password(password_length)

print("сгенерированный пароль:", password)

"запуск через смд"

python password_generator.py 8

"число 8 это длиннаа пароля"