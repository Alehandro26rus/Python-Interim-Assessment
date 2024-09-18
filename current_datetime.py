from datetime import datetime

# Получаем текущее время и дату
now = datetime.now()

# Форматируем дату и время
formatted_datetime = now.strftime('%Y-%m-%d %H:%M:%S')

# Получаем день недели и номер недели в году
day_of_week = now.strftime('%A')  # Полное название дня недели
week_number = now.isocalendar()[1]  # Номер недели в году

# Выводим результаты
print(f'Текущая дата и время: {formatted_datetime}')
print(f'День недели: {day_of_week}')
print(f'Номер недели в году: {week_number}')