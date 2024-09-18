import argparse

def main():
    # Создание объекта парсера
    parser = argparse.ArgumentParser(description='Повторение строки.')
    
    # Добавление обязательных аргументов
    parser.add_argument('number', type=int, help='Число - сколько раз вы хотите повторить строку')
    parser.add_argument('text', type=str, help='Строка, которую необходимо повторить')
    
    # Добавление опций
    parser.add_argument('--verbose', action='store_true', help='Выводить дополнительную информацию')
    parser.add_argument('--repeat', type=int, default=1, help='Количество повторений строки (по умолчанию 1)')
    
    # Считывание аргументов
    args = parser.parse_args()
    
    # Обработка аргументов
    if args.verbose:
        print(f'Число: {args.number}')
        print(f'Строка: "{args.text}"')
        print(f'Повторений: {args.repeat}')
    
    # Формирование результата
    result = (args.text + ' ') * (args.repeat)
    
    # Ограничиваем количество выводимых символов
    result = result.strip()  # Удаляем лишний пробел в конце
    
    # Вывод результата
    print(result)

if __name__ == '__main__':
    main()