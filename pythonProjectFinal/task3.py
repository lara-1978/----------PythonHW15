# Задача 3. Планирование задач
# Напишите функцию, которая принимает количество дней от текущей даты и
# возвращает дату, которая наступит через указанное количество дней. Дополнительно,
# выведите эту дату в формате YYYY-MM-DD.
from datetime import datetime, timedelta

def get_future_date(days_from_now):
    current_date = datetime.now()

    future_date = current_date + timedelta(days=days_from_now)
    formatted_date = future_date.strftime('%Y-%m-%d')

    return formatted_date

if __name__ == '__main__':
    days = int(input("Введите количество дней от текущей даты: "))
    future_date = get_future_date(days)
    print(f"Дата через {days} дней: {future_date}")

#Если нам надо подсчитать дату в обратную сторону, то в запросе пишем число отрицательное. Пример: Дата через -1 дней: 2024-10-31, Дата через -3 дней: 2024-10-29



