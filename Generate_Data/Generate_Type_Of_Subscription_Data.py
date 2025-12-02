subscriptions = [
    ('1 month', 299, 10, 'Активна'),
    ('3 months', 799, 30, 'Активна'),
    ('6 months', 1499, 60, 'Активна'),
    ('1 year', 2499, 120, 'Активна'),
    ('+infinity', 0, 3, 'Неактивна'),
]

def generate_type_of_subscription_data(cursor):
    print("Генерация Type_Of_Subscription")
    for subscription in subscriptions:
        cursor.execute('INSERT INTO "Type_Of_Subscription" (duration, price, hours_of_ride, status) VALUES (%s, %s, %s, %s)', (subscription[0], subscription[1], subscription[2], subscription[3]))
    print("Генерация Type_Of_Subscription успешна")