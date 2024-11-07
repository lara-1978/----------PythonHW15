# Задача 2. Работа с текущим временем и датой
# Напишите скрипт, который получает текущее время и дату, а затем выводит их в
# формате YYYY-MM-DD HH:MM:SS. Дополнительно, выведите день недели и номер
# недели в году.
# Подсказка № 1
# Используйте from datetime import datetime, чтобы получить доступ к текущему
# времени и дате, а также к методам для их форматирования.
# Подсказка № 2
# Используйте datetime.now() для получения объекта datetime, содержащего
# текущее время и дату.
# Подсказка № 3
# Примените метод strftime() для форматирования даты и времени в строку с
# нужным форматом, например, '%Y-%m-%d %H:%M:%S'.
# Подсказка № 4
# Используйте strftime('%A') для получения полного названия дня недели.
# Используйте isocalendar()[1] для получения номера недели в году

from datetime import datetime

def datetime_now():
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d_%H:%M:%S')
    day_of_week = now.strftime('%A')
    week_number = now.isocalendar()[1]
    print(f'Date & time:{formatted_date}')
    print(f'Day of week:{ day_of_week}')
    print(f'Week_number:{week_number}')

if __name__ == '__main__':
    datetime_now()











