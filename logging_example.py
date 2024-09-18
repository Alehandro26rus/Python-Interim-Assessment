import logging

# Создаем логгер
logger = logging.getLogger('MyLogger')
logger.setLevel(logging.DEBUG)  # Устанавливаем минимальный уровень логирования

# Создаем обработчик для записи логов уровня DEBUG и INFO
debug_info_handler = logging.FileHandler('debug_info.log')
debug_info_handler.setLevel(logging.DEBUG)  # Обрабатываем DEBUG и INFO

# Создаем обработчик для записи логов уровня WARNING и выше
warnings_errors_handler = logging.FileHandler('warnings_errors.log')
warnings_errors_handler.setLevel(logging.WARNING)  # Обрабатываем WARNING, ERROR и CRITICAL

# Создаем форматтер для настройки формата сообщений
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Применяем форматтер к обработчикам
debug_info_handler.setFormatter(formatter)
warnings_errors_handler.setFormatter(formatter)

# Добавляем обработчики к логгеру
logger.addHandler(debug_info_handler)
logger.addHandler(warnings_errors_handler)

# Примеры логирования разных уровней сообщений
logger.debug('Это сообщение уровня DEBUG')
logger.info('Это сообщение уровня INFO')
logger.warning('Это сообщение уровня WARNING')
logger.error('Это сообщение уровня ERROR')
logger.critical('Это сообщение уровня CRITICAL')