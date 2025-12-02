import random
from faker import Faker

cities = (
    ('Москва', 55.755826, 37.617300),
    ('Санкт-Петербург', 59.934280, 30.335099),
    ('Новосибирск', 55.008355, 82.935732),
    ('Екатеринбург', 56.838926, 60.605702),
    ('Казань', 55.796289, 49.108795),
    ('Нижний Новгород', 56.326887, 44.005986),
    ('Красноярск', 56.015283, 92.893248),
    ('Челябинск', 55.164442, 61.436843),
    ('Самара', 53.195533, 50.101801),
    ('Омск', 54.989342, 73.368212)
)

def generate_parking_data(cursor, count):
    print("Начало генерации", count, "Parking")
    fake = Faker('ru_RU')
    parkings = []
    for i in range(count):
        city, width, longitude = random.choice(cities)
        width = round(width + random.uniform(-0.1, 0.1), 6)
        longitude = round(longitude + random.uniform(-0.1, 0.1), 6)
        address = f"{city}, {fake.street_address()}"
        count_places = random.randint(5, 50)
        parkings.append((address, width, longitude, count_places))
    cursor.executemany('INSERT INTO "Parking" (address, width, longitude, count_parking_places) VALUES (%s, %s, %s, %s)', parkings)
