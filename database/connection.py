import settings
import os
import psycopg2


class DatabaseConnection:
    __instance = None

    @staticmethod
    def get():
        if DatabaseConnection.__instance == None:
            DatabaseConnection.__instance = psycopg2.connect(
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT"),
                database=os.getenv("DB_DATABASE"),
                user=os.getenv("DB_USERNAME"),
                password=os.getenv("DB_PASSWORD")
            )
        return DatabaseConnection.__instance

    def __init__(self):
        if DatabaseConnection.__instance is None:
            raise Exception("Singleton class.")
