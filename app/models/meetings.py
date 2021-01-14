from database.connection import DatabaseConnection
import psycopg2.extras

connection = DatabaseConnection.get()
cursor = connection.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor)

TABLE_NAME = "meetings"
USERS_TABLE = "users"
MEETING_USERS_TABLE = "meeting_users"


class Meetings:
    @staticmethod
    def all():
        command = """
                SELECT * FROM {0}
            """.format(TABLE_NAME)

        cursor.execute(command)

        return cursor.fetchall()

    @staticmethod
    def all_sorted():
        command = """
            SELECT * FROM {0} ORDER BY start_date DESC
        """.format(TABLE_NAME)

        cursor.execute(command)

        return cursor.fetchall()

    @staticmethod
    def participants(meeting):
        command = """
                    SELECT u.id, u.first_name, u.last_name FROM {0} u
                    LEFT JOIN {1} mu ON u.id = mu.user_id
                    WHERE mu.meeting_id = {2}
                """.format(USERS_TABLE, MEETING_USERS_TABLE, meeting.id)

        cursor.execute(command)

        return cursor.fetchall()

    @staticmethod
    def find_by_name(name):
        command = """
            SELECT * FROM {0} WHERE name = '{1}'
        """.format(TABLE_NAME, name)

        cursor.execute(command)

        return cursor.fetchone()

    @staticmethod
    def find(id):
        command = """
                    SELECT * FROM {0} WHERE id = {1}
                """.format(TABLE_NAME, id)

        cursor.execute(command)

        return cursor.fetchone()

    @staticmethod
    def create(name, start_date, end_date):
        command = """
            INSERT INTO {0}(name, start_date, end_date) VALUES('{1}', to_timestamp({2}), to_timestamp({3}))
        """.format(TABLE_NAME, name, start_date, end_date)

        cursor.execute(command)
        connection.commit()

        select_command = """
            SELECT * FROM {0} WHERE name='{1}'
        """.format(TABLE_NAME, name)

        cursor.execute(select_command)

        return cursor.fetchone()

    @staticmethod
    def assign_user(meeting, user):
        command = """
                INSERT INTO {0}(meeting_id, user_id) VALUES({1}, {2})
            """.format(MEETING_USERS_TABLE, meeting.id, user.id)

        cursor.execute(command)
        connection.commit()

        return True

    @staticmethod
    def destroy(id):
        command = """
            DELETE FROM {0} WHERE id = {1}
        """.format(TABLE_NAME, id, id)

        cursor.execute(command)
        connection.commit()

        return True
