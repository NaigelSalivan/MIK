import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class DBconnect:
    def __init__(self, user, password, host, port, db_name):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.db_name =db_name
        print("asdsadsa")

    # def createTable(self):
    #     try:
    #         connection = psycopg2.connect(
    #             user=self.user,
    #             password=self.password,
    #             host=self.host,
    #             port=self.port,
    #             database=self.db_name

    def connectPG(self):
        try:
            connection = psycopg2.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.db_name
            )
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT version();"
                )
                print(f"Server version: {cursor.fetchone()}")
#                print(connection.get_dsn_parameters(), "\n")
        except Exception as _ex:
            print("[INFO] Ошибка при работе с PostgreSQL", _ex)
        finally:
            if not connection:
                pass
            else:
                connection.close()
                print("[INFO] Соединение с PostgreSQL закрыто")

    def connectPG(self):
        try:
            connection = psycopg2.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.db_name
            )
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT version();"
                )
                print(f"Server version: {cursor.fetchone()}")
#                print(connection.get_dsn_parameters(), "\n")
        except Exception as _ex:
            print("[INFO] Ошибка при работе с PostgreSQL", _ex)
        finally:
            if not connection:
                pass
            else:
                connection.close()
                print("[INFO] Соединение с PostgreSQL закрыто")
    def crateTable(self):
        try:
            connection = psycopg2.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.db_name)
            cursor = connection.cursor()
            create_table_query = '''CREATE TABLE mobile
                          (ID INT PRIMARY KEY     NOT NULL,
                          MODEL           TEXT    NOT NULL,
                          PRICE         REAL); '''
            cursor.execute(create_table_query)
            connection.commit()
            print("Таблица успешно создана")
        except (Exception, Error) as eror:
            print("Erorr table creates")
        finally:
            if connection:
                cursor.close()
                connection.close()
                print("соединение закрыто")
