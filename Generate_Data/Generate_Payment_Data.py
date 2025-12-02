import random

from faker import Faker

statuses = ['Успешно', 'Ошибка', 'Ожидание', 'Возврат']

def generate_payment_data(cursor, count):
    print("Начало генерации", count, "Payment")
    fake = Faker('ru_RU')

    cursor.execute('SELECT user_id FROM "User"')
    users = []
    for user in cursor.fetchall():
        users.append(user[0])

    cursor.execute('SELECT type_of_subscription_id FROM "Type_Of_Subscription"')
    type_of_subscriptions = []
    for type_of_subscription in cursor.fetchall():
        type_of_subscriptions.append(type_of_subscription[0])

    payments = []
    for i in range(count):
        date = fake.date_time_between(start_date = "-1000d", end_date = "now")
        status = random.choice(statuses)
        saved_card = fake.credit_card_number()
        user_id = random.choice(users)
        type_of_subscription_id = random.choice(type_of_subscriptions)
        payments.append((date, status, saved_card, user_id, type_of_subscription_id))

    cursor.executemany('INSERT INTO "Payment" (date, status, saved_card, user_id, type_of_subscription_id) VALUES (%s, %s, %s, %s, %s)', payments)
    print("Генерация Payment успешна")