from database.connection import DatabaseConnection

connection = DatabaseConnection.get()
cursor = connection.cursor()

TABLE_NAME = "meeting_users"


class CreateMeetingUsersTable:
    @staticmethod
    def up():
        check_exists = """
            SELECT EXISTS(SELECT * FROM information_schema.tables WHERE table_name = '{0}')
        """.format(TABLE_NAME)
        cursor.execute(check_exists, TABLE_NAME)
        exists = bool(cursor.fetchone()[0])

        if not exists:
            create_command = """
                        CREATE TABLE {0} (
                            id SERIAL PRIMARY KEY,
                            meeting_id INTEGER NOT NULL,
                            user_id INTEGER NOT NULL
                        );
                    """.format(TABLE_NAME)

            cursor.execute(create_command, TABLE_NAME)
            connection.commit()

    @staticmethod
    def down():
        drop_command = """
            DROP TABLE IF EXISTS {0};
        """.format(TABLE_NAME)

        cursor.execute(drop_command)
        connection.commit()

