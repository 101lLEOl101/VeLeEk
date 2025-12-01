import psycopg2
from Generate_Data.Generate_Parking_Data import *
from Generate_Data.Generate_Role_Data import *
from Generate_Data.Generate_User_Data import *
from Generate_Data.Generate_Ride_Data import *
from Generate_Data.Generate_Payment_Data import *
from Generate_Data.Generate_Bike_Data import *
from Generate_Data.Generate_Type_Of_Subscription_Data import *

DB_CONFIG = {
    'dbname': 'VeLeEk',
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'port': '5432'
}

def create_connection():
    try:
        connection_ = psycopg2.connect(**DB_CONFIG)
        connection_.autocommit = False
        print("Подключение к БД Успешно")
        return connection_
    except Exception as e:
        print("Ошибка подключения:",e)

if __name__ == "__main__":
    connection = create_connection()
    if not connection:
        exit(0)
    cursor = connection.cursor()
    try:
        print("Начало Генерации:")
        generate_role_data(cursor)
        generate_type_of_subscription_data(cursor)
        generate_user_data(cursor, 10000)
        generate_parking_data(cursor, 10000)
        generate_bike_data(cursor, 10000)
        generate_ride_data(cursor, 10000)
        generate_payment_data(cursor, 10000)
    except Exception as e:
        print("Ошибка заполнения:",e)
        connection.rollback()
    if cursor:
        cursor.close()
    if connection:
        connection.close()
    print("Подключение к БД закрыто")