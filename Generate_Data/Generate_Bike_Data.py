import random

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

brands = ("Giant", "Scott", "Aspect", "Stinger", "Stels", "Format", "Atom", "Welt", "Polygon", "Stark")

statuses = ['Доступен', 'Занят', 'На ремонте', 'Забронирован']

def generate_bike_data(cursor, count):
    print("Начало генерации", count, "Bike")
    cursor.execute('SELECT parking_id FROM "Parking"')
    parking_ids = []
    for parking in cursor.fetchall():
        parking_ids.append(parking[0])
    parking_ids.append(None)
    bikes = []
    for i in range(count):
        city_of_use, width, longitude = random.choice(cities)
        width = round(width + random.uniform(-0.2, 0.2), 6)
        longitude = round(longitude + random.uniform(-0.2, 0.2), 6)
        status = random.choice(statuses)
        current_charge = random.randint(0, 100)
        brand = random.choice(brands)
        maximum_speed = random.randint(15, 45)
        parking_id = random.choice(parking_ids)
        bikes.append((width, longitude, status, current_charge, brand, maximum_speed, city_of_use, parking_id))
    cursor.executemany('INSERT INTO "Bike" (width, longitude, status, current_charge, brand, maximum_speed, city_of_use, parking_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',bikes)
    print("Генерация Bike успешна")