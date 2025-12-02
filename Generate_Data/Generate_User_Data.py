from datetime import timedelta
import random

from faker import Faker

def generate_user_data(cursor, count):
    print("Начало генерации",count,"User")
    fake = Faker('ru_RU')

    cursor.execute('SELECT role_id FROM "Role"')
    role_ids = []
    for role_id in cursor.fetchall():
        role_ids.append(role_id[0])

    cursor.execute('SELECT type_of_subscription_id FROM "Type_Of_Subscription"')
    sub_ids = []
    for type_of_subscription_id in cursor.fetchall():
        sub_ids.append(type_of_subscription_id[0])

    users = []
    for i in range (count):
        name = fake.name()
        login = fake.user_name()
        hash_password = fake.sha256()
        saved_card = None
        if random.random() < 0.5:
            saved_card = fake.credit_card_number()
        end_of_subscription = fake.future_date(end_date=timedelta(days=365))
        role_id = random.choice(role_ids)
        type_of_subscription_id = random.choice(sub_ids)
        if type_of_subscription_id == 5:
            end_of_subscription = None
        users.append((name, login, hash_password, saved_card, end_of_subscription, role_id, type_of_subscription_id))

    cursor.executemany('INSERT INTO "User" (name, login, hash_password, saved_card, end_of_subscription, role_id, type_of_subscription_id) VALUES (%s, %s, %s, %s, %s, %s, %s)', users)
    print("Генерация User успешна")

