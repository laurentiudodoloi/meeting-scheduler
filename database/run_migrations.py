from database.migrations.create_users_table import CreateUsersTable
from database.migrations.create_meetings_table import CreateMeetingsTable
from database.migrations.create_meeting_users_table import CreateMeetingUsersTable

migrations = [
    CreateUsersTable,
    CreateMeetingsTable,
    CreateMeetingUsersTable
]

for migration in migrations:
    migration.up()
