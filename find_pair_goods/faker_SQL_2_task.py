from faker import Faker
import psycopg2
from psycopg2 import Error
from random import randint

fake = Faker()
try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user="root",
                                  # пароль, который указали при установке PostgreSQL
                                  password="toor",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="test")

    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    # Распечатать сведения о PostgreSQL
    print("Информация о сервере PostgreSQL")
    print(connection.get_dsn_parameters(), "\n")
    # Выполнение SQL-запроса
    cursor.execute("SELECT version();")
    events = []
    for _ in range(100):
        date_tt = fake.date_between(start_date='-8w')
        id_tt = randint(1, 3)
        id_tov = randint(1, 20)
        qty = randint(1, 5)
        cursor.execute(f"INSERT INTO DTT (date_tt, id_tt, id_tov, qty) VALUES {date_tt.isoformat(), id_tt, id_tov, qty};")
    connection.commit()
    print('commit_done')
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")