roles = [
    ('Администратор', 'CRUD_ALL'),
    ('Пользователь', 'READ_RIDE'),
    ('Модератор', 'CRUD_REVIEWS'),
    ('Техподдержка', 'READ_ALL'),
    ('Гость', 'READ_ONLY'),
]

def generate_role_data(cursor):
    print("Начало генерации Role")
    for role in roles:
        cursor.execute('INSERT INTO "Role" (name, rights) VALUES (%s, %s)', (role[0], role[1]))
    print("Генерация Role успешна")
