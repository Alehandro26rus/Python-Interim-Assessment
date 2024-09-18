from datetime import datetime, timedelta

def get_future_date(days):
    # Получаем текущую дату и время
    current_date = datetime.now()
    
    # Создаем объект timedelta с указанным количеством дней
    time_delta = timedelta(days=days)
    
    # Вычисляем будущую дату
    future_date = current_date + time_delta
    
    # Форматируем дату в строку YYYY-MM-DD
    formatted_future_date = future_date.strftime('%Y-%m-%d')
    
    return formatted_future_date

# Пример использования функции
days_to_add = 10  # Например, 10 дней
future_date = get_future_date(days_to_add)
print(f'Дата через {days_to_add} дней: {future_date}')