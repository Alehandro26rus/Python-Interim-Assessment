import os
import logging
from collections import namedtuple
import sys

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(message)s', filename='directory_contents.log')

# Определение namedtuple для хранения информации о файлах и каталогах
DirectoryContent = namedtuple('DirectoryContent', ['name', 'extension', 'is_directory', 'parent_directory'])

def gather_directory_info(directory):
    if not os.path.isdir(directory):
        logging.error(f'{directory} не является директорией.')
        return

    parent_directory = os.path.basename(directory)
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        
        if os.path.isdir(item_path):
            # Если это каталог
            content = DirectoryContent(name=item, extension='', is_directory=True, parent_directory=parent_directory)
        else:
            # Если это файл
            name, extension = os.path.splitext(item)
            content = DirectoryContent(name=name, extension=extension.lstrip('.'), is_directory=False, parent_directory=parent_directory)

        # Логируем информацию о текущем объекте
        logging.info(content)

def main():
    if len(sys.argv) != 2:
        print("Использование: python directory_info.py <путь_до_директории>")
        sys.exit(1)
    
    directory = sys.argv[1]
    gather_directory_info(directory)
    print(f"Информация о содержимом директории '{directory}' записана в 'directory_contents.log'.")

if __name__ == '__main__':
    main()