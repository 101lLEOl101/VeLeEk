import random
from datetime import timedelta

from faker import Faker

statuses = ['Завершена', 'Отменена', 'В процессе']

comments = (
    "Отличная поездка!",
    "Велосипед немного скрипел",
    "Удобный маршрут",
    "Всё понравилось",
    "Сломалось сиденье",
    "Быстро и удобно",
    "Дорогие тарифы",
)

def generate_ride_data(cursor, count):
    print("Начало генерации", count, "Ride")
    fake = Faker('ru_RU')

    cursor.execute('SELECT user_id FROM "User"')
    user_ids = []
    for user in cursor.fetchall():
        user_ids.append(user[0])

    cursor.execute('SELECT bike_id FROM "Bike"')
    bike_ids = []
    for bike in cursor.fetchall():
        bike_ids.append(bike[0])

    rides = []
    for i in range(count):
        start_time = fake.date_time_between(start_date='-1000d', end_date='now')
        time_in_ride = timedelta(minutes=random.randint(5, 300))
        distance = random.uniform(0.1, 50)
        status = random.choice(statuses)
        user_id = random.choice(user_ids)
        bike_id = random.choice(bike_ids)
        ride_mark_1_5 = None
        comment = None
        time_comment = None
        if random.random() < 0.5:
            ride_mark_1_5 = random.randint(1, 5)
            comment = random.choice(comments)
            time_comment = start_time + time_in_ride + timedelta(minutes=random.randint(1, 60))
        rides.append((start_time, time_in_ride, distance, status, user_id, bike_id, ride_mark_1_5, comment, time_comment))

    cursor.executemany('INSERT INTO "Ride" (start_time, time_in_ride, distance, status, user_id, bike_id, ride_mark_1_5, comment_feedback, time_comment) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', rides)
    print("Генерация Ride успешна")

