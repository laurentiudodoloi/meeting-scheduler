from database.connection import DatabaseConnection
import psycopg2.extras

connection = DatabaseConnection.get()
cursor = connection.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)

TABLE_NAME = "users"


class Users:
    @staticmethod
    def all():
        all_command = """
                SELECT * FROM {0}
            """.format(TABLE_NAME)

        cursor.execute(all_command)

        return cursor.fetchall()

    @staticmethod
    def find(id):
        find_command = """
                    SELECT * FROM {0} WHERE id = {1}
                """.format(TABLE_NAME, id)

        cursor.execute(find_command)

        return cursor.fetchone()

    @staticmethod
    def create(first_name, last_name):
        create_command = """
            INSERT INTO {0}(first_name, last_name) VALUES('{1}', '{2}')
        """.format(TABLE_NAME, first_name, last_name)

        cursor.execute(create_command)
        connection.commit()

        return True

    @staticmethod
    def destroy(id):
        create_command = """
                DELETE FROM {0} WHERE id = {1}
            """.format(TABLE_NAME, id, id)

        cursor.execute(create_command)
        connection.commit()

        return True
